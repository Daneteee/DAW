# Sistema de llibreria, el qual simula una llibreria en línia on els usuaris poden navegar pels llibres, afegir-los al
# carro i fer compres.
# Autor: Dan Maldonado
# Data: 01-04-2024

from library import Library
from user import User
from input_ import Input_
from book_command import BookCommand
from print_title import PrintTitle

BOOKS_FILE = "./csvs/books.csv"
USERS_FILE = "./csvs/users.csv"
COMMANDS_FILE = "./csvs/comandes.csv"


# Aquesta funció comprova si les llibreries necessàries estan instal·lades al sistema. Si alguna d'elles falta, mostra
# un missatge d'error.
def check_libraries():
    """Comprova que l'usuari tingui instal·lades les llibreries necessaries.
    """
    valid_libraries = True
    try:
        from prettytable import PrettyTable
        from tempfile import NamedTemporaryFile
        from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
        from InvoiceGenerator.pdf import SimpleInvoice

    except ImportError:
        print("""
                Has d'instal·lar les llibreries per continuar:
                NamedTemporaryFile, InvoiceGenerator, PrettyTable.
            """)
        valid_libraries = False

    return valid_libraries


def main():
    library = Library(BOOKS_FILE)
    user = User(USERS_FILE)

    library.import_books()
    library.search_categories()

    PrintTitle.print_title("Llibreria Dan", "calgphy2")

    leave = False

    while not leave:
        print_catalog = Input_.input_ok("Vols imprimir tot el catàleg (S/N)? ")
        if print_catalog:
            library.print_book_category()

        buy = Input_.input_ok("\nVols comprar algun llibre (S/N)? ")
        if buy:
            PrintTitle.print_title("Comprant.")

            library.buy_book()

            if library.cart.check_cart():
                PrintTitle.print_title("Pagament Comanda")

                if user.authentication():

                    if user.is_major():
                        command = BookCommand(
                            user=user,
                            cart=library.cart,
                            file=COMMANDS_FILE)
                        command.payment()
                        library.cart.empty_cart()

                    else:
                        print("Només poden comprar online els majors d'edat")
                        library.cart.empty_cart()
                    user.logout()
                else:
                    print("Carro buit")
                    library.cart.empty_cart()
                    library.cart.print_cart()
                    leave = True
            else:
                leave = True
        else:
            leave = True

    print("Fins la propera!!!")
    if user.is_logged():
        user.logout()
    library.cart.empty_cart()


if __name__ == "__main__" and check_libraries():
    main()
