from tkinter import *


class Calculator:
    BUTTONS = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ]

    def __init__(self, master):
        # Creem la calculadora
        self.master = master
        master.title("Calculator")
        master.minsize(width=100, height=100)
        master.resizable(False, False)

        # Creem la pantalla i la posicionem
        self.screen = Entry(width=34)
        self.screen.grid(columnspan=4, row=0)

        self.init_buttons()

    def init_buttons(self):
        # Mostrem els botons
        buttons = self.BUTTONS
        for button_text, r, c in buttons:
            # Creem el botó i fiquem un command o un altre depenent de la tecla seleccionada
            button = Button(self.master, text=button_text, width=5, height=2,
                            command=lambda t=button_text: (self.insert_screen(t) if t != "C" and t != "=" else
                                                           (self.calculate() if t == "=" else self.clean_screen())))

            button.grid(row=r, column=c)

    def insert_screen(self, text):
        # Inserim les entrades a la pantalla
        display_text = self.screen.get()
        self.screen.delete(0, END)
        self.screen.insert(0, display_text + text)

    def clean_screen(self):
        # Esborrem la pantalla
        self.screen.delete(0, END)

    def calculate(self):
        expression = self.screen.get()
        # Comprovem que la expressió sigui correcta i mostrem el resultat
        try:
            self.screen.delete(0, END)
            self.screen.insert(0, eval(expression))

        except:
            self.screen.delete(0, END)
            self.screen.insert(0, "Syntax ERROR")


def main():
    root = Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
