from user_manager import UserManager
from pymongo import MongoClient
from utils import Utils
from user import User

def main():
    # Conectem amb pymongo i seleccionem BBDD i col·lecció
    db = Utils.getDb()
    user_collection = db['users']

    # Creem una instancia de UserManager amb la col·lecció especificada
    user_manager = UserManager(collection=user_collection)
    
    leave = False
    current_user = None
    
    while not leave:
        
        # Menú d'opcions
        options = ["Registrar usuari", "Iniciar sessió", "Tancar sessió"]
        Utils.print_menu(options)
        option = input("Selecciona una opció: ")

        if option == '1':
            username = input("Usuari: ")
            password = input("Contrasenya: ")
            
            role_options = ["Usuari", "Entrenador", "Admin", "Gerent"]
            Utils.print_menu(role_options, "Rols", leave_option=False)
            role_num = Utils.valid_input(f"Rol: ", ["1", "2", "3", "4"])
            role = role_options[int(role_num) - 1]

            # Si es registra correctament inciem sessió
            if user_manager.register(username, password, role):
                print("Usuari registrat correctament")
                print("Sessió iniciada correctament")
                current_user = User(username, password, role)
                
            else:
                print("\nERROR: Aquest usuari ja existeix")

        elif option == '2':
            
            # Comprovem si l'usuari está connectat
            if current_user:
                print("\nJa estàs connectat!!")
                print(f"Usuari: {current_user}")
                
            #  Si no hi ha cap usuari connectat iniciem sessió
            else:
                username = input("Usuari: ")
                password = input("Contrasenya: ")
                
                
                if user_manager.login(username, password):
                    print("Sessió iniciada correctament")
                    role = user_manager.getRole(username)
                    
                    if role == "Usuari":
                        current_user = User(username, password, role)
                    elif role == "Entrenador":
                        current_user = Trainer(username, password, role)
                    
                    
                else:
                    print("\nERROR: Credencials incorrectes")
                
        elif option == '3':
            
            # Comprovem si hi han usuaris connectats 
            if current_user is None:
                print("\nNo hi ha cap usuari connectat.")
                
            # Tanquem sessió
            else:
                print(f"\nAdeu, {current_user}...")
                current_user = None

        elif option == '4':
            current_user = None
            print("Sortint...")
            leave = False

        else:
            print("ERROR: Opció invàlida")

if __name__ == '__main__':
    main()
