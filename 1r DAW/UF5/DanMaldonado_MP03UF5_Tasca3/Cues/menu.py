from prettytable import PrettyTable


class Menu:
    def __init__(self, menu_functions):
        self.menu_functions = menu_functions

    def print_menu(self):
        # Mostra el menú
        mida = len(self.menu_functions)

        taula = PrettyTable()
        taula.field_names = ["*:･ﾟ✧*:･ﾟ--| Funcions |--･ﾟ:*✧･ﾟ:*"]

        for i in range(len(self.menu_functions)):
            taula.add_row([f"{i + 1}. {self.menu_functions[i]}"])

        taula.add_row([f"{mida + 1}. SORTIR"])

        print(taula)

    def get_choice(self):
        # Demana la selecció del usuari
        length = len(self.menu_functions) + 1
        leave = False

        while not leave:
            try:
                choice = int(input("Selecciona una opció: "))
                if choice == length:
                    leave = True
                elif 0 < choice < length:
                    return choice
                else:
                    print("ERROR: Entrada invàlida.")
            except ValueError:
                print("ERROR: Entrada invàlida.")

        return length

