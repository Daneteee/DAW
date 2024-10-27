from pyfiglet import Figlet


class PrintTitle:
    @staticmethod
    def print_title(text, selected_font="roman"):
        """Mostrem un texto en format títol.

        Args:
            text (str): Text a escriure.
            selected_font (str, optional): Font de la lletra. Defaults to "roman".
        """
        f = Figlet(font=selected_font, width=200, justify="center")
        return f.renderText(text)
