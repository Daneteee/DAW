class Moneder:
    MONEDA = "€"
    VALORS_MONEDES = {
        "10c": 0.1,
        "20c": 0.2,
        "50c": 0.5,
        "1€": 1,
        "2€": 2,
    }

    def __init__(self):
        # Inicialització dels atributs del moneder
        self.benefici = 0
        self.diners_introduits = 0
        self.canvi = 10

    def __str__(self):
        # Mostrem benefici actual
        return f"El benefici és de: {self.benefici}{self.MONEDA}\n"

    def processa_monedes(self):
        # Processament de les monedes introduïdes per l'usuari
        for moneda, valor_moneda in self.VALORS_MONEDES.items():
            entrada_valida = False
            while not entrada_valida:
                try:
                    entrada_usuari = input(f"Quantes monedes de {moneda} (Enter: 0)? ")
                    if entrada_usuari == "":
                        n_monedes = 0
                    else:
                        n_monedes = int(entrada_usuari)
                    self.diners_introduits += (valor_moneda * n_monedes)
                    entrada_valida = True
                except ValueError:
                    print("ERROR: Valor incorrecte.")

    def torna_canvi(self, beguda_preu):
        # Càlcul i retorn del canvi per l'usuari
        self.benefici += beguda_preu
        canvi_usuari = self.diners_introduits - beguda_preu
        self.diners_introduits = 0
        self.canvi -= canvi_usuari
        print(f"Canvi: {canvi_usuari}{self.MONEDA}\n")
        return canvi_usuari

    def fer_pagament(self, preu):
        # Processament del pagament de l'usuari
        self.processa_monedes()
        if self.diners_introduits >= preu:
            if self.canvi < self.torna_canvi(preu):
                print("ERROR: Canvi de la màquina insuficient.\n")
                self.canvi = 10
                return False
            return True
        else:
            print("ERROR: Diners insuficients.")
            return False

    def fer_caixa(self):
        # Mostrem el benefici recaptat i reiniciem el benefici
        print(f"\nBenefici recaptat: {self.benefici}{self.MONEDA}\n")
        self.benefici = 0
