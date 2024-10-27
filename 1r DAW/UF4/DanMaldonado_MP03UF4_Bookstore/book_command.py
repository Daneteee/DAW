from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from command import Command
from datetime import datetime
from input_ import Input_
from wallet import Wallet
from file_ import File_
from cart import Cart
import os


class BookCommand(Command):

    # S'inicialitzen diversos atributs, incloent-hi l'usuari que ha realitzat la comanda, el carro de la compra associat
    # a la comanda, la data de la comanda (obtinguda com a data i hora actuals formatades com a "dd-mm-YYYY") i el nom
    # de l'arxiu on es desaran les comandes, i l’estat inicialment marcat com a “Pendent”. Evidentment també la id.
    def __init__(self, user, cart, file):
        super().__init__()
        self.user = user
        self.cart = cart
        self.com_date = datetime.now().strftime("%d-%m-%Y")
        self.status = "Pendent"
        self.file = file

    # Mostra el contingut del carro de la compra, calcula el total de la comanda i ofereix l'opció de pagar-la. Per fer
    # el pagament s’utilitza la classe moneder de la tasca de la màquina de cafè(*). Si s'efectua el pagament amb
    # èxit, l'estat de la comanda es canvia a "Pagada", es desa la comanda en format CSV i es genera un albarà en format
    # PDF utilitzant la llibreria InvoiceGenerator.
    def payment(self):
        """Mostra el contingut del carro de la compra
        """
        Cart.print_cart(self.cart)
        pay = Input_.input_ok("Vols pagar (S/N)? ")
        if pay:
            total = self.cart.cart_total()
            wallet = Wallet()
            wallet.do_payment(total)
            self.status = "Pagada"
            self.__save_command_csv()
            print(f"""Ja pots recollir la teva comanda:
            \n{self._id}, {self.com_date}, {self.user.email}, {self.cart.cart_total()}, {self.status}
            """)
            self.__create_invoice()

    # Afegeix una nova línia al fitxer CSV de les comandes, que inclou l'identificador de la comanda, la data, l'email
    # de l'usuari i l'import total de la comanda i l’estat.
    def __save_command_csv(self):
        """Afegeix una nova línia al fitxer CSV de les comandes
        """
        content = f"\n{self._id}, {self.com_date}, {self.user.email}, {self.cart.cart_total()}, {self.status}"
        File_.append_(self.file, content)

    # Genera un albarà en format PDF utilitzant la llibreria InvoiceGenerator. Aquest albarà inclou informació sobre el
    # client, el proveïdor, el número de comanda, els articles comprats i el total de la comanda. El PDF de l'albarà es
    # guarda en el directori de comandes amb el nom albarà-{id_de_la_comanda}.pdf.
    def __create_invoice(self):
        """Crea un document PDF de la comanda
        """
        # Idioma es espanyol
        os.environ["INVOICE_LANG"] = "es"

        client = Client(self.user.name, email=self.user.email)
        provider = Provider("Llibreria OOP")
        creator = Creator("Dan Maldonado")

        invoice = Invoice(client, provider, creator)
        # Fiquem la divisa a euro
        invoice.currency = "€"
        invoice.number = self._id

        for book in self.cart.books:
            invoice.add_item(Item(count=1, price=book.price, description=f"{book.title} - {book.ISBN}"))

        pdf = SimpleInvoice(invoice)
        pdf.gen(f"./commands/albara-{self._id}.pdf")

