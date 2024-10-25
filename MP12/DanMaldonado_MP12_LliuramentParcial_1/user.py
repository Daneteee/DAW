class User:
    def __init__(self, name, password, role="user"):
        """_summary_

        Args:
            name (str): Nom de l'usuari
            password (str): Contrasenya de l'usuari
        """
        self.name = name
        self.password = password
        self.role = role
        
    def __str__(self):
        return self.name
    