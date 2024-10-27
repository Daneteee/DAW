from datetime import *


class Person:

    # El constructor de la classe que inicialitza els atributs nom, cognoms i data_naixament de la persona.
    def __init__(self, name, lastname, birth_date):
        self.name = name
        self.lastname = lastname
        self.birth_date = birth_date

    # Un mètode especial que retorna una representació en cadena de la persona, en aquest cas, el nom i els cognoms de
    # la persona.
    def __str__(self):
        """Mostrem el nom del usuari i el seu cognom.

        Returns:
            str: Nom i cognom de l'usuari.
        """
        return f"Nom: {self.name}\nCognoms: {self.lastname}"

    # Un mètode que calcula i retorna l'edat de la persona basada en la data de naixement proporcionada.
    def age(self):
        """ Calculem l'edat del usuari.

        Returns:
            int: L'edat.
        """
        today = datetime.now()
        
        # Transformem la data a objecte
        date_obj = datetime.strptime(self.birth_date, "%d-%m-%Y")
        # Comprovem si ja a complert els anys.
        if (today.month, today.day) < (date_obj.month, date_obj.day):
            age = today.year - date_obj.year - 1
        else:
            age = today.year - date_obj.year
        return age

    def is_major(self):
        """Calculem si l¡usuari és major d'edat.

        Returns:
            bool: True si és major d'edat.
        """
        return self.age() >= 18
