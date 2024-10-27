from cart import Cart
from file_ import File_
from book import Book
from input_ import Input_
from prettytable import PrettyTable


class Library:

    # Aquest és el constructor de la classe. Rep un paràmetre: arxiu, que és la ruta de fitxer, i a més té els següents
    # atributs: llibres, una llista d'objectes Llibre inicialment llista buida, i categories, una llista de cadenes de
    # text que representen les categories dels llibres, inicialment llista buida. També hi ha els atributs linia0,
    # inicialment “” cadena buida i carro que és una instància de la classe Carro. De moment pots definir la classe
    # carro amb pass
    def __init__(self, file):
        self.file = file
        self.books = []
        self.categories = []
        self.line0 = ""
        self.cart = Cart()

    # Aquest mètode importa els llibres des d'un fitxer, utilitzant la classe Arxiu. Llegeix cada línia del fitxer,
    # analitza les dades de cada llibre i els afegeix a la llista llibres. També assigna la primera línia de l’arxiu a
    # l’atribut linia0.
    def import_books(self):
        """Agafa els llibres des d'un fitxer i els transforma a objectes de llibres.
        """
        books = File_.read_lines_(self.file)
        self.line0 = books.pop(0)
        for book in books:
            book = book.split(",")
            title = book[0]
            author = book[1]
            price = book[2]
            ISBN = book[3]
            category = book[4]
            book = Book(title, author, price, ISBN, category)
            self.books.append(book)
        self.line0 = books[0]

    # Aquest mètode recorre la llista de llibres i afegeix les categories úniques a l’atribut categories.
    def search_categories(self):
        """Recorre la llista de llibres i afegeix les categories úniques a l’atribut categories.
        """
        for book in self.books:
            if book.category not in self.categories:
                self.categories.append(book.category)

    # Mostra a l'usuari les opcions de categoria i sol·licita la selecció d'una, retorna la categoria seleccionada
    def input_category(self):
        """Mostra a l'usuari un seguit de categories i sol·licita una.

        Returns:
            str: La categoría seleccionada.
        """
        options = {}
        self.search_categories()
        for category in self.categories:
            options[category[:3]] = category.rstrip()
        return Input_.input_option("Categories:", options)

    # A partir de l’atribut llibres, i el paràmetre categoria retorna una llista de llibres que pertanyen a una
    # categoria específica.
    def create_category_books(self, category):
        """Crea un llistat de llibres que pertanyen a la categoría especificada.

        Args:
            category (str): Categoria a trobar.

        Returns:
            list: Llista de llibres que pertanyen a la categoria seleccionada.
        """
        category_books = []
        for book in self.books:
            if book.category.rstrip() == category:
                category_books.append(book)
        return category_books

    # Imprimeix la llista de llibres, paginant-los si és necessari per defecte de 20 en 20. La categoria de llibres a
    # imprimir es pot proporcionar com a argument opcional. Utilitza la biblioteca PrettyTable per mostrar les dades
    # tabulars de manera organitzada. Cada llibre ha de tenir un id per poder identificar-lo
    def print_book_category(self, pagination=20, category=""):
        """Mostra tots els llibres per columnes.

        Args:
            pagination (int, optional): Paginació amb la qual mostrar els llibres. Defaults to 20.
            category (str, optional): Categoria especifica dels llibres mostrats.. Defaults to "".
        """
        table = PrettyTable()
        c = 0
        categorized_books = self.create_category_books(category) if category != "" else self.books
        table.field_names = ["ID", "Títol", "Autor", "Preu", "ISBN", "Categoria"]
        for i in range(1, len(categorized_books) + 1):
            book = categorized_books[i - 1]
            table.add_row([i, book.title, book.author, book.price, book.ISBN, book.category[:-1]])
            if i % pagination == 0:
                print(table)
                input("Enter para continuar: ")
                c = i
        if len(categorized_books) % pagination != 0:
            print(table[c:])

    # Aquest mètode permet al client seleccionar quin llibre vol comprar d'una categoria específica. Primer crea una
    # llista de llibres disponibles en la categoria especificada. L'usuari selecciona un llibre mitjançant un índex
    # numèric. Retorna el llibre seleccionat o 0 si l'usuari vol sortir de la selecció de llibres.
    def input_book(self, books_category):
        """Permet al client seleccionar quin llibre vol comprar d'una categoria específica.

        Args:
            books_category (str): Categoria especifica que han de tenir els llibres.

        Returns:
            obj: El llibre
        """
        categorized_books = self.create_category_books(books_category)
        self.print_book_category(category=books_category)
        book_id = Input_.input_int("Quina fila vols? (enter per sortir)",
                                   min_=1,
                                   max_=len(categorized_books),
                                   not_limit=False,
                                   valid_return=True)
        selected_book = categorized_books[book_id - 1]
        print(f"Has seleccionat el llibre: {selected_book.title}" if book_id != 0 else "Has sortit de la selecció")
        if book_id != 0:
            self.cart.add_book(selected_book)
        return selected_book if book_id != 0 else 0

    # Aquest mètode permet a l'usuari seleccionar un llibre per eliminar-lo del carro.
    # L'usuari introdueix un índex numèric corresponent al llibre que vol eliminar.
    # Retorna el llibre seleccionat per eliminar-lo o None si l'usuari vol sortir sense eliminar res.
    def ask_delete(self):
        """Pregunta a l'usuari quin llibre vol eliminar.
        """
        print("Aquest és el teu carret:")
        self.cart.print_cart()
        book_id = Input_.input_int("Quin llibre vols eliminar? (enter per sortir)",
                                   1,
                                   len(self.cart.books),
                                   valid_return=True)
        if book_id != 0:
            print(f"Llibre: {self.cart.books[book_id - 1]} Eliminat correctament")
            self.cart.delete_book(self.cart.books[book_id - 1])
            print("Aquest és el teu carret:")
            self.cart.print_cart()

    # Aquest mètode guia l'usuari a través del procés de compra.
    def buy_book(self):
        """Procés de compra.
        """
        stay = True
        while stay:
            book_category = self.input_category()
            self.input_book(book_category)
            self.cart.print_cart()
            stay = Input_.input_ok("Vols seguir comprant (S/N)? ")

        stay = True
        while stay and self.cart.check_cart():
            stay = Input_.input_ok("Vols eliminar algun llibre (S/N)?")
            if stay:
                self.ask_delete()
