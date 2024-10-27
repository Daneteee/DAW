class User:
    def __init__(self, name, password, role="user", userID="None"):
        """_summary_

        Args:
            name (str): Nom de l'usuari
            password (str): Contrasenya de l'usuari
        """
        self.name = name
        self.password = password
        self.role = role
        self.userID = userID
        
    def __str__(self):
        return self.name
    
    def printMenu(self):
        pass    
    