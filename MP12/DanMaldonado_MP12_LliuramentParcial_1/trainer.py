from user import User
from pymongo.collection import Collection

class Trainer(User):
    
    # Creació de Rutines de Classe: L'entrenador pot crear rutines específiques per a les classes que imparteix, 
    # incloent exercicis, durada i recomanacions.
    def __init__(self, name, password, role="trainer"):
        super().__init__(name, password, role)
        
    
    
        
    
    