from prettytable import PrettyTable
from book import Book


class Cart:

    def __init__(self):
        self.books = []

    # Afegeix un llibre al carro de compra.
    def add_book(self, book):
        """Afegeix un objecte llibre al carro.

        Args:
            book (obj): Objecte llibre
        """
        self.books.append(book)

    # Calcula el total del preu dels llibres continguts al carro de compra.
    def cart_total(self):
        """Calcula el preu total del carro

        Returns:
            float: Preu total del carro.
        """
        total = 0
        for book in self.books:
            total += float(book.price)
        return total

    # Imprimeix el contingut del carro de compra en forma de taula, utilitza prettyTable, cal afegir també el total amb
    # 2 decimals
    def print_cart(self):
        """Mostrem el carro amb els detalls de cada llibre i el total.
        """
        c = 0
        table = PrettyTable()
        table.field_names = ["ID", "Títol", "Autor", "Preu", "ISBN", "Categoria"]
        for i in range(1, len(self.books) + 1):
            book = self.books[i - 1]
            table.add_row([i, book.title, book.author, book.price, book.ISBN, book.category[:-1]])
            if i % 20 == 0:
                print(table)
                input("Enter para continuar: ")
                c = i
        if len(self.books) % 20 != 0:
            table.add_row(["", "", "", "", "", f"Total: {self.cart_total():.2f}"])
            print(table[c:])

    # Elimina un llibre específic del carro de compra.
    def delete_book(self, book):
        """Eliminem un objecte llibre del carro.

        Args:
            book (obj): Llibre a esborrar
        """
        self.books.remove(book)

    #  Elimina tots els llibres del carro de compra.
    def empty_cart(self):
        """Buidem el carro
        """
        self.books.clear()

    # Verifica si hi ha llibres al carro de compra.
    def check_cart(self):
        """Comprovem si hi ha llibres al carro.

        Returns:
            bool: True si el carro no està buit
        """
        return len(self.books) > 0
