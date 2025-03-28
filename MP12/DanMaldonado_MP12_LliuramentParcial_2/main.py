from user_manager import UserManager
from pymongo import MongoClient
from trainer import Trainer
from utils import Utils
from user import User

def main():
    # Conectem amb pymongo i seleccionem BBDD i col·lecció
    db = Utils.getDb()
    user_collection = Utils.getDb('users')

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
                
            #  Si no hi ha cap usuari connectat iniciem sessióa
            else:
                username = input("Usuari: ")
                password = input("Contrasenya: ")
                
                
                if user_manager.login(username, password):
                    print("Sessió iniciada correctament")
                    role = user_manager.getRole(username)
                    userID = user_manager.getUserID(username)

                    # Creem la instancia de l'usuari depenent del seu rol
                    if role == "Usuari":
                        current_user = User(username, password, role)
                    elif role == "Entrenador":
                        current_user = Trainer(username, password, role)
                    
                        while current_user:
                    
                            current_user.printMenu()
                            user_options = Utils.valid_input("Selecciona una opció: ", ["1", "2", "3", "4", "5", "6"])
                            
                            if user_options == '1':
                                current_user.createRoutine()
                            
                            elif user_options == '2':
                                current_user.addSchedule()
                            
                            elif user_options == '3':
                                current_user.listAttendants()
                            
                            elif user_options == '4':
                                current_user.addUserToRoutine()

                            elif user_options == '5':
                                current_user.removeUserFromRoutine()
                                
                            else:
                                current_user = None

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
