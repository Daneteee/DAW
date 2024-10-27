class Cafetera:
    def __init__(self, aigua, llet, cafe):
        # Inicialització dels ingredients i el diccionari de stock
        self.aigua = aigua
        self.llet = llet
        self.cafe = cafe
        self.stock = {
            "aigua": aigua,
            "llet": llet,
            "cafe": cafe
        }

    def __str__(self):
        # Mostrem l'stock
        text = "Stock:\n"
        for item in self.stock:
            text += f"      {item}: {self.stock[item]}\n"
        return text

    def hi_ha_recursos(self, beguda):
        # Verifica si hi ha prou recursos per fer una beguda específica
        for ingredient in beguda.ingredients:
            if self.stock[ingredient] < beguda.ingredients[ingredient]:
                print(f"ERROR: Recursos insuficients.")
                return False
        return True

    def fer_beguda(self, beguda):
        # Prepara una beguda reduint els recursos de la cafetera
        for ingredient in beguda.ingredients:
            self.stock[ingredient] -= beguda.ingredients[ingredient]
        print(f"{beguda.nom} fet amb èxit!\n")

    def afegir_recurs(self, recurs, quantitat):
        # Afegeix una quantitat específica d'un recurs al stock
        self.stock[recurs] += quantitat
