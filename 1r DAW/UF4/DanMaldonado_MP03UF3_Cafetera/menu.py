class Menu:
    def __init__(self, begudes):
        # Inicialització de la llista de begudes en el menú
        self.begudes = begudes

    def __str__(self):
        # Mostrem el text del menú
        text = "Llistat de begudes:\n"
        for beguda in self.begudes:
            text += f"          {beguda.nom} - {beguda.preu}\n"
        return text

    def troba_beguda(self, beguda):
        # Troba la beguda corresponent pel nom
        for obj_beguda in self.begudes:
            if beguda == obj_beguda.nom.lower():
                return obj_beguda
        print("ERROR: Beguda incorrecta.")
        return False
