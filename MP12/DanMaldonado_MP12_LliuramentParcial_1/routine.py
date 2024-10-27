from utils import Utils

class Routine:
    
    def __init__(self, name, exercises, duration, recommendations, attendees, userID):
        self.name = name
        self.exercises = exercises
        self.duration = duration
        self.recommendations = recommendations
        self.userID = userID
        self.attendees = attendees
        self.routines_collection = Utils.getDb("routines")
        
        
    # Creem la rutina
    def createRoutine(self):
        routine_data = {
            "name": self.name,
            "exercises": self.exercises,
            "duration": self.duration,
            "recommendations": self.recommendations,
            "userID": self.userID,
            "horari": [],  
            "attendees": []  
        }
        self.routines_collection.insert_one(routine_data)
        print(f"Rutina '{self.name}' creada correctament.")
        

    # Llistem als usuaris apuntats a la rutina
    def listAttendants(self):
        print(f"Usuaris inscrits a la rutina '{self.name}':")
        for attendant in self.attendees:
            print(attendant)
