from utils import Utils

class Routine:
    
    def __init__(self, name, exercises, duration, recommendations, userID):
        self.name = name
        self.exercises = exercises
        self.duration = duration
        self.recommendations = recommendations
        self.userID = userID
        self.routines_collection = Utils.getDb("routines")
        
    def createRoutine(self):
        # Datos de la rutina, incluyendo el ObjectID del entrenador
        routine_data = {
            "name": self.name,
            "exercises": self.exercises,
            "duration": self.duration,
            "recommendations": self.recommendations,
            "userID": self.userID,
            "horari": [],  # Lista para los horarios asignados
            "assistents": []  # Lista para los usuarios inscritos
        }
        self.collection.insert_one(routine_data)
        print(f"Rutina '{self.name}' creada correctament.")
        

    