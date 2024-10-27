from input_ import Input_
from datetime import datetime


class Wallet:
    COIN = "€"
    COIN_VALUES = {
        "10c": 0.1,
        "20c": 0.2,
        "50c": 0.5,
        "1€": 1,
        "2€": 2,
        "5€": 5,
        "10€": 10,
        "20€": 20,
        "50€": 50
    }

    def __init__(self):
        # Inicialització dels atributs del moneder
        self.introduced_coins = 0
        self.change = 1000

    def process_coins(self):
        """Processa els mètodes de pagament.

        Returns:
            bool: True si ha pagat amb targeta. (Ho utilitzarem a altra funció)
        """
        card_payment = Input_.input_ok("Vols pagar amb targeta (S/N)? ")

        if card_payment:
            card_num = Input_.input_digits(16)
            cvv = Input_.input_digits(3)
            valid_date = False
            while not valid_date:
                card_date = Input_.input_date("Introdueix data de caducitat (mm-yy)", True)
                valid_date = datetime.strptime(card_date, "%m-%y") > datetime.now()
                print("ERROR: Data invàlida." if not valid_date else "")
            print("Pagament realitzat correctament.\n")

        else:
            # Processament de les monedes introduïdes per l'usuari
            for coin, coin_value in self.COIN_VALUES.items():
                valid_entry = False
                while not valid_entry:
                    try:
                        user_entry = input(f"Quantes monedes/bitllets de {coin} (Enter: 0)? ")
                        if user_entry == "":
                            n_coins = 0
                        else:
                            n_coins = int(user_entry)
                        self.introduced_coins += (coin_value * n_coins)
                        valid_entry = True
                    except ValueError:
                        print("ERROR: Valor incorrecte.")
        return card_payment

    def return_exchange(self, price):
        # Càlcul i retorn del canvi per l'usuari
        user_change = self.introduced_coins - price
        self.introduced_coins = 0
        self.change -= user_change
        print(f"Canvi: {user_change:.2f}{self.COIN}\n")
        return user_change

    def do_payment(self, price):
        # Processament del pagament de l'usuari
        card_payment = self.process_coins()
        if self.introduced_coins >= price:
            if self.change < self.return_exchange(price):
                print("ERROR: Canvi de la màquina insuficient.\n")
                self.change = 10
                return False
            return True
        else:
            if not card_payment:
                print("ERROR: Diners insuficients.")
            return False
