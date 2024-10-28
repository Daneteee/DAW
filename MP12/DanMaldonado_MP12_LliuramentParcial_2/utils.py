from pymongo import MongoClient
from datetime import datetime

class Utils():
    
    @staticmethod
    def print_menu(options, title="Menu", leave_option=True):
        """Mostrem el menú d'opcions.

        Args:
            options (list): Llista de cada funció
        """
        mida = len(options)
        
        print(f"""
               *:･ﾟ✧*:･ﾟ--| {title} |--･ﾟ:*✧･ﾟ:*\n """)
        
        for i in range(mida):
            print(f"{i+1}. {options[i]}")
        
        if leave_option:
            print(f"{mida+1}. Sortir")


    @staticmethod
    def check_int(num, enter_valid=False):
        """Comprovem que el nombre sigui numeric o permetem retorn si enter_valid és True.

        Args:
            num (int): Nombre
            enter_valid (bool, optional): Booleà per permetre entrar retorns. Defaults to False.

        Returns:
            Si permetem enters i hi han enters el retornem, sinó retornem el nombre i si dona error, False.
        """
        try:
            return "" if enter_valid and num == "" else int(num)
        except ValueError:
            return False


    @staticmethod
    def correct_range(num, minim=None, maxim=None):
        """Comprovem que el nombre es trobi entre els valors seleccionats.

        Args:
            num (int): Nombre
            minim (int, optional): Valor mínim. Defaults to None.
            maxim (int, optional): Valor màxim. Defaults to None.

        Returns:
            int: Retorna e nombre si es troba entre els minims i maxims
        """
        # Té un mínim però no té un màxim
        if minim is not None and maxim is None:
            return num >= minim
        # No té un mínim però sí que hi ha un màxim
        elif minim is None and maxim is not None:
            return num <= maxim
        # Hi ha un mínim i un màxim
        elif minim is not None and maxim is not None:
            return num >= minim and num <= maxim
        # No té ni mínim ni màxim
        else:
            return True


    @staticmethod
    def secure_int(text, min=None, max=None, enter_valid=False):
        """Comprovem que un nombre sigui valid i es trobi entre els valors especificats.
        També comprovem si pot haver-hi retorns.

        Args:
            text (str): Text que es mostrarà al input
            min (int, optional): Valor mínim. Defaults to None.
            max (int, optional): Valor màxim. Defaults to None.
            enter_valid (bool, optional): Si permetem els enters. Defaults to False.

        Returns:
            int: Nombre introduit
        """
        correct_num = False
        while not correct_num:
            num = input(text)
            num = Utils.check_int(num, enter_valid)
            correct_num = Utils.correct_range(num, min, max) if num != '' else True
        return num
    
    
    @staticmethod
    def valid_input(text, options):
        """ Comprovem que l'usuari introdueixi opcions vàlides a un input.

        Args:
            text (_type_): _description_
            options (list): Llista d'opcions vàlides

        Returns:
            str: El valor introduit, si es incorrecte tornem a demanar.
        """
        option = input(text)
        if option not in options:
            print("ERROR: Opció invàlida.")
            return Utils.valid_input(text, options)
        else:
            return option
    
    
    # Donat un diccionari d’opcions, només permet una opció correcta a més afegeix l’opció 0 per sortir i retorna
    # l’opció.
    @staticmethod
    def input_option(message, options, input_message="\nQue vols fer? "):
        """Validem que s'introdueixi una opció correcta d'un diccionari d'opcions.

        Args:
            message (str): Missatge a mostrar.
            options (dict): Diccionari d'opcions.

        Returns:
            str: La opció si aquesta es correcta o missatge en cas de sortir.
        """
        leave = False
        while not leave:
            print(message)
            for key, value in options.items():
                print(f"    {key} - {value}")

            option = input(input_message).capitalize()

            if option in options:
                return options[option]
            else:
                print("ERROR: Opció invàlida.")
        return "Sortint..."
    
    
    # Només permet lletres i espais
    @staticmethod
    def input_text(message):
        """Introducció de text

        Args:
            message (str): Missatge a mostrar.

        Returns:
            str: Retornem l'string.
        """
        entry = ""
        is_valid = False
        while not is_valid:
            entry = input(message + ": ")
            is_valid = all([c.isalpha() or c.isspace() for c in entry])
            if not is_valid:
                print("ERROR: Només permet lletres i espais.")
        return entry
    
    @staticmethod
    def validate_time():
        is_valid = False
        while not is_valid:
            time_input = input("Hora (HH:MM): ") 
            try:
                time_input = datetime.strptime(time_input, "%H:%M")
                is_valid = True
                
            except ValueError:
                print("ERROR: Hora invàlida (format HH:HH).")  
        
        return time_input 
    
    @staticmethod
    def getDb(collection=None):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['gym']
        
        if collection:
            db = db[collection]
            
        return db
    