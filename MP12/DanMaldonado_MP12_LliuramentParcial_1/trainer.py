from routine import Routine
from user import User
from utils import Utils
from datetime import datetime, timedelta

class Trainer(User):
    def __init__(self, name, password, role="trainer", userID=None):
        super().__init__(name, password, role, userID)
        self.routines_collection = Utils.getDb("routines")
        self.user_collection = Utils.getDb("users")

    # Menu d'opcions
    def printMenu(self):
        options = [
            'Crear rutina.',
            'Assignar horari.',
            'Llistar usuaris.',
            'Afegir usuari a rutina.',
            'Eliminar usuari de rutina.'
        ]
        Utils.print_menu(options)

    # Agafem les dades per crear la rutina 
    def createRoutine(self):
        name = input("Nom de la rutina: ")
        exercises = input("Llista d'exercicis: ")
        duration = Utils.secure_int("Durada de la rutina (en minuts): ", min=1)
        recommendations = input("Recomanacions per la rutina: ")

        rutina = Routine(name, exercises, duration, recommendations, [], self.userID)
        rutina.createRoutine()
 
    # Llistem totes les rutines
    def listRoutines(self):
        routines = self.routines_collection.find()
        print("Llista de rutines:")
        for routine in routines:
            print(f"    Nom: {routine['name']}")
    
    # Llistem la rutina
    def listAttendants(self):
        self.listRoutines()
        routine_name = input("Introdueix el nom de la rutina: ")

        selected_routine = self.routines_collection.find_one({"name": routine_name})

        # Instanciem la rutina 
        if selected_routine:
            routine = Routine(selected_routine['name'],
                             selected_routine['exercises'],
                             selected_routine['duration'],
                             selected_routine['recommendations'],
                             selected_routine['attendees'],
                             selected_routine['userID'])
            
            routine.listAttendants()  
        else:
            print("ERROR: La rutina no existeix.")
    
    # Afegim l'horari
    def addSchedule(self):
        self.listRoutines()
        routine_name = input("Introdueix el nom de la rutina: ")
        
        # Guardem la posible rutina
        selected_routine = self.routines_collection.find_one({"name": routine_name})

        # Comprovem si existeix 
        if selected_routine:
            room = Utils.input_option("Sala: ", {"1": "Activitats dirigides", "2": "Musculació"}, "Quina sala s'utilitzara? ") 
            
            # Validem el temps i el retornem com a objecte datetime
            start_time = Utils.validate_time() 
            
            if "horari" in selected_routine:
                existing_schedules = selected_routine["horari"]
            else:
                existing_schedules = []
                
            # En aquesta part, primerament verifiquem que hi hagin més horaris a la sala per saber si continuar verificant o no
            # després veriquem que per cada horari que hagi, no es solapin les clases, amb el time delta afegim temps per verificar
            # que passa mínim una hora entre dues classes.
            conflict_found = any(
                schedule["room"] == room and
                (start_time < (datetime.strptime(schedule["start_time"], "%H:%M") + timedelta(minutes=60)) and
                datetime.strptime(schedule["start_time"], "%H:%M") < (start_time + timedelta(minutes=60)))
                for schedule in existing_schedules)

            if not conflict_found:
                self.routines_collection.update_one(
                    {"name": routine_name},
                    {"$push": {"horari": {"room": room, "start_time": start_time.strftime("%H:%M"), "duration": 60}}}
                )
                print("Horari assignat correctament a la rutina.")
            else:
                print("ERROR: Ja hi ha una rutina a la mateixa sala i hora.")
        else:
            print("ERROR: La rutina no existeix.")
            
    # Afegim un usuari a la rutina
    def addUserToRoutine(self):
        self.listRoutines()
        routine_name = input("Introdueix el nom de la rutina: ")
        username = input("Introdueix el nom de l'usuari a afegir: ") 

        selected_routine = self.routines_collection.find_one({"name": routine_name})

        if selected_routine:
            user = self.user_collection.find_one({"username": username}) 
            if user:
                if "attendees" in selected_routine:
                    updated_attendees = selected_routine["attendees"]
                else:
                    updated_attendees = [] 
                    
                if username not in updated_attendees:
                    updated_attendees.append(username)
                    self.routines_collection.update_one(
                        {"name": routine_name},
                        {"$set": {"attendees": updated_attendees}}
                    )
                    print(f"Usuari '{username}' afegit a la rutina '{routine_name}'.")
                else:
                    print("ERROR: Aquest usuari ja està inscrit a la rutina.")
            else:
                print("ERROR: L'usuari no existeix.")
        else:
            print("ERROR: La rutina no existeix.")


    # Eliminem l'usuari
    def removeUserFromRoutine(self):
        self.listRoutines()
        routine_name = input("Introdueix el nom de la rutina: ")
        username = input("Introdueix el nom de l'usuari a eliminar: ") 

        selected_routine = self.routines_collection.find_one({"name": routine_name})

        if selected_routine:
            if "attendees" in selected_routine:
                updated_attendees = selected_routine["attendees"]
            else:
                updated_attendees = [] 
                
            if username in updated_attendees:
                updated_attendees.remove(username)
                self.routines_collection.update_one(
                    {"name": routine_name},
                    {"$set": {"attendees": updated_attendees}}
                )
                print(f"Usuari '{username}' eliminat de la rutina '{routine_name}'.")
            else:
                print("ERROR: Aquest usuari no està inscrit a la rutina.")
        else:
            print("ERROR: La rutina no existeix.")