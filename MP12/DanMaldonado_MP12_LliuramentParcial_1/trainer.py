from routine import Routine
from user import User
from utils import Utils
from datetime import datetime, timedelta

class Trainer(User):
    def __init__(self, name, password, role="trainer", userID=None):
        super().__init__(name, password, role, userID)
        self.routines_collection = Utils.getDb("routines")
    
    def printMenu(self):
        options = ['Crear rutina.', 'Assignar horari.', 'Llistar usuaris.', 'Gestionar usuaris.']
        Utils.print_menu(options)

    def createRoutine(self):
        name = input("Nom de la rutina: ")
        exercises = input("Llista d'exercicis: ")
        duration = Utils.secure_int("Durada de la rutina (en minuts): ", min=1)
        recommendations = input("Recomanacions per la rutina: ")

        rutina = Routine(name, exercises, duration, recommendations, self.userID)
        rutina.createRoutine()
 
 
    def listRoutines(self):
        routines = self.routines_collection.find()
        
        print("Llista de rutines:")
        for routine in routines:
            print(f"    Nom: {routine['name']}")
    
    
    def addSchedule(self):
        self.listRoutines()

        routine_name = input("Introdueix el nom de la rutina: ")
        
        selected_routine = self.routines_collection.find_one({"name": routine_name})

        if selected_routine:
            room = Utils.input_option("Sala: ", {"1": "Activitats dirigides", "2": "Musculació"}, "Quina sala s'utilitzara? ") 
            
            # Agafem la hora amb tipus datetime
            start_time = Utils.validate_time() 
            
            if "horari" in selected_routine:
                existing_schedules = selected_routine["horari"]
            else:
                existing_schedules = []

            # A aquesta part, primerament verifiquem que hi hagin més horaris a la sala per saber si continuar verificant o no
            # després veriquem que per cada horari que hagi, no es solapin les clases, amb el time delta afegim temps per verificar
            # que passa mínim una hora entre dues classes.
            conflict_found = any(
                schedule["room"] == room and
                (start_time < (datetime.strptime(schedule["start_time"], "%H:%M") + timedelta(minutes=60)) and
                datetime.strptime(schedule["start_time"], "%H:%M") < (start_time + timedelta(minutes=60)))
                for schedule in existing_schedules)

            if not conflict_found:
                # Agregar el horario a la rutina
                self.routines_collection.update_one(
                    {"name": routine_name},
                    {"$push": {"horari": {"room": room, "start_time": start_time.strftime("%H:%M"), "duration": 60}}}
                )
                print("Horari assignat correctament a la rutina.")
            
            else:
                print("ERROR: Ja hi ha una rutina a la mateixa sala i hora.")
        else:
            print("ERROR: La rutina no existeix.")