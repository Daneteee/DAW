from utils import Utils

class Routine:
    
    def __init__(self, name, exercises, duration, recommendations):
        self.name = name
        self.exercises = exercises
        self.duration = duration
        self.recommendations = recommendations
        self.collection = Utils.getDb("routines")
        
    def createRoutine(self):
        # Creem un nou usuari i l'afegim
        routine_data = {
            "name": self.name,
            "exercises": self.exercises,
            "duration": self.duration,
            "recommendations": self.recommendations
        }
        self.collection.insert_one(routine_data)
        
        
    def addSchedule(self, room, start_time):
        # Verifiquem si ja existeix una rutina a la mateixa sala i hora
        conflicting_routine = self.collection.find_one({
            "horari.room": room,
            "horari.start_time": start_time
        })

        ok = True
        
        if conflicting_routine:
            print("ERROR: Ja hi ha una rutina a la mateixa sala i hora.")
            ok = False
        
        else:
            # Afegim el nou horari
            schedule_data = {
                "room": room,
                "start_time": start_time,
                "duration": 60  
            }

            # Afegim l'horari a la rutina
            self.collection.update_one(
                {"name": self.name}, 
                {"$push": {"horari": schedule_data}}  # Usa $push per afegir a la col·lecció "horari"
            )
            
            print("Horari afegit correctament.")
            ok = True
            
        return ok
        
        