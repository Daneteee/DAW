class Book:
    # El constructor de la classe que inicialitza els atributs del llibre.
    def __init__(self, title, author, price, ISBN, category):
        self.title = title
        self.author = author
        self.price = price
        self.__ISBN = ISBN
        self.category = category

    @property
    def ISBN(self):
        return self.__ISBN

    # Un mètode que retorna una cadena amb els detalls complets del llibre, incloent-hi el títol, autor, categoria, preu
    # i ISBN.
    def detail(self):
        """Mostrem els detalls del llibre

        Returns:
            str: Detalls del llibre.
        """
        return f"""
        Title: {self.title}
        Author: {self.author}
        Category: {self.category}
        Price: {self.price}
        ISBN: {self.__ISBN}
        """

    # Un mètode especial que retorna una representació en cadena del llibre, en aquest cas, només el títol, autor i
    # categoria.
    def __str__(self):
        """Representació en cadena del llibre.
        
        Returns:
            str: Titol, autor i any.
        """
        return f"""
        Títol: {self.title}
        Autor: {self.author}
        Any:  {self.category}
        """
