from input_ import Input_
from person import Person
from file_ import File_
from print_title import PrintTitle
import bcrypt


class User(Person):

    # El constructor de la classe que inicialitza els atributs de l'usuari.
    def __init__(self, file, name="", lastname="", birth_date="", email="", password=""):
        super().__init__(name, lastname, birth_date)
        self.file = file
        self.user = "user"
        self.email = email
        self.__password = password

    # Demana una contrasenya i l'encripta utilitzant l'algorisme bcrypt
    def __input_hash_passwd(self):
        """Agafem la contrasenya de l'usuari i la codifiquem.

        Returns:
            str: La contrasenya codificada.
        """
        self.__password = Input_.input_password("Introdueix la contrasenya")
        hashed_password = bcrypt.hashpw(self.__password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        return hashed_password

    # Comprova si la contrasenya introduïda correspon amb la contrasenya emmagatzemada (encriptada).
    def __check_password(self, input_password, hashed_password):
        """Comprovem si la contrasenya introduida correspon amb la contrasenya encriptada.

        Args:
            input_password (str): Contrasenya introduida.
            hashed_password (str): Contrasenya encriptada.

        Returns:
             bool: True si la contrasenya coincideix.
        """
        return bcrypt.checkpw(input_password.encode("utf-8"), hashed_password.encode("utf-8"))

    # Sol·licita a l'usuari que introdueixi una adreça de correu electrònic única, és a dir no hi pot haver cap altre
    # usuari que tingui aquest mail, per això utilitza comprova_es_unic, que hauràs de definir més avall.
    def __input_mail(self):
        """Sol·licitem a l'usuari que introdueixi una adreça de correu electrònic única.

        Returns:
            str: L'email.
        """
        is_unique = False
        email = ""
        while not is_unique:
            email = Input_.input_email("Introdueix email")
            is_unique = self.__check_unique(email)
            if not is_unique:
                print("ERROR: Email ja registrat.")
        return email

    # Registra un nou usuari emmagatzemant les seves dades en el fitxer corresponent.
    def __register(self):
        """Canviem tots els atributs als quals introdueixi l'usuari i els escrivim al fitxer corresponent.
        """
        self.name = Input_.input_text("Introdueix nom")
        self.lastname = Input_.input_text("Introdueix cognoms")
        self.email = self.__input_mail()
        self.__password = self.__input_hash_passwd()
        self.birth_date = Input_.input_date("Introdueix data (dd-mm-aaaa)")
        line = f"\n{self.name},{self.lastname},{self.email},{self.__password},{self.user},{self.birth_date}"
        File_.append_(self.file, content=line)

    # Inicia sessió amb les credencials proporcionades per l'usuari.
    def __login(self):
        """Donem 3 oportunitats per iniciar sessió i assignem els atributs als de l'usuari corresponent.
        """
        opportunities = 3
        while opportunities > 0 and not self.is_logged():
            opportunities -= 1
            
            email = Input_.input_email("Introdueix email")
            input_password = Input_.input_password("Introdueix contrasenya")
            users = File_.read_lines_(self.file)
            email_line = self.__find_line(email)
            
            if email_line != 0:
                user = users[email_line]
                user = user.split(",")
                saved_password = user[3]
                
                if self.__check_password(input_password, saved_password):
                    self.name = user[0]
                    self.lastname = user[1]
                    self.email = user[2]
                    self.__password = user[3]
                    self.user = user[4]
                    self.birth_date = user[5].rstrip()
                else:
                    print("ERROR: Credencials incorrectes.")
                    
            else:
                print("ERROR: Credencials incorrectes.")

    # Comprova si l'adreça de correu electrònic és única.
    def __check_unique(self, email):
        """Comprovem si l'adreça introduida és única.

        Args:
            email (str): Email a comprovar.

        Returns:
            bool: True si el correu és únic.
        """
        users = File_.read_lines_(self.file)
        for user in users:
            if email in user:
                return False
        return True

    # Troba la línia corresponent a l'adreça de correu electrònic de l'usuari al fitxer.
    def __find_line(self, email):
        """Trobem la línia que correspon l'email actual.

        Args:
            email (str): Email de l'usuari.

        Returns:
            int: La línia de l'usuari (0 si no es troba).
        """
        users = File_.read_lines_(self.file)
        for i in range(len(users)):
            if email in users[i]:
                return i
        return 0

    # Verifica si l'usuari està connectat al sistema.
    def is_logged(self):
        """Verifiquem si l'usuari està connectat.

        Returns:
            bool: True si segueix connectat.
        """
        return self.email != ""

    # Tanca la sessió de l'usuari.
    def logout(self):
        """Reiniciem tots els atributs.
        """
        self.name = ""
        self.lastname = ""
        self.email = ""
        self.__password = ""
        self.birth_date = ""
        print("T'has desconnectat.")

    # Gestiona el procés d'autenticació de l'usuari, permetent el registre, inici de sessió i sortida.
    def authentication(self):
        """Mostrem un menú d'autenticació on l'usuari pot iniciar sessió, registre o sortir.
        """
        leave = False
        while not self.is_logged() and not leave:
            print("T'has d'autentificar, ets nou? registra’t o sinó fes login ")
            options = {"R": "Registre", "L": "Login"}
            op = Input_.input_option("Opcions", options)
            if op == "Registre":
                self.__register()
                self.__login()
            elif op == "Login":
                self.__login()
            elif op == "0":
                leave = True
        PrintTitle.print_title(f"Benvingut\n{self.name} {self.lastname}", "roman")
        return True
