from pymongo import MongoClient

class Utils():
    
    @staticmethod
    def print_menu(menu, title="Menu", leave_option=True):
        """Mostrem el menú d'opcions.

        Args:
            menu (list): Llista de cada funció
        """
        mida = len(menu)
        
        print(f"""
               *:･ﾟ✧*:･ﾟ--| {title} |--･ﾟ:*✧･ﾟ:*\n """)
        
        for i in range(mida):
            print(f"{i+1}. {menu[i]}")
        
        if leave_option:
            print(f"{mida+1}. Sortir")

    @staticmethod
    def check_int(num, enter_valid=False):
        """Comprovem que el nombre sigui numeric o permetem retorn si enter_valid és True.

        Args:
            num (int): Nombre
            enter_valid (bool, optional): Booleà per permetre entrar retorns. Defaults to False.

        Returns:
            Si permetem enters i hi han enters el retornem, sinó retornem el nombre i si dona error, False.
        """
        try:
            return "" if enter_valid and num == "" else int(num)
        except ValueError:
            return False

    @staticmethod
    def correct_range(num, minim=None, maxim=None):
        """Comprovem que el nombre es trobi entre els valors seleccionats.

        Args:
            num (int): Nombre
            minim (int, optional): Valor mínim. Defaults to None.
            maxim (int, optional): Valor màxim. Defaults to None.

        Returns:
            int: Retorna e nombre si es troba entre els minims i maxims
        """
        # Té un mínim però no té un màxim
        if minim is not None and maxim is None:
            return num >= minim
        # No té un mínim però sí que hi ha un màxim
        elif minim is None and maxim is not None:
            return num <= maxim
        # Hi ha un mínim i un màxim
        elif minim is not None and maxim is not None:
            return num >= minim and num <= maxim
        # No té ni mínim ni màxim
        else:
            return True

    @staticmethod
    def secure_int(text, min=None, max=None, enter_valid=False):
        """Comprovem que un nombre sigui valid i es trobi entre els valors especificats.
        També comprovem si pot haver-hi retorns.

        Args:
            text (str): Text que es mostrarà al input
            min (int, optional): Valor mínim. Defaults to None.
            max (int, optional): Valor màxim. Defaults to None.
            enter_valid (bool, optional): Si permetem els enters. Defaults to False.

        Returns:
            int: Nombre introduit
        """
        correct_num = False
        while not correct_num:
            num = input(text)
            num = check_int(num, enter_valid)
            correct_num = correct_range(num, min, max) if num != '' else True
        return num
    
    def valid_input(text, options):
        """ Comprovem que l'usuari introdueixi opcions vàlides a un input.

        Args:
            text (_type_): _description_
            options (list): Llista d'opcions vàlides

        Returns:
            str: El valor introduit, si es incorrecte tornem a demanar.
        """
        option = input(text)
        if option not in options:
            print("ERROR: Opció invàlida.")
            return Utils.valid_input(text, options)
        else:
            return option
    
    @staticmethod
    def getDb(collection=None):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['gym']
        
        if collection:
            db = db[collection]
            
        return db
    