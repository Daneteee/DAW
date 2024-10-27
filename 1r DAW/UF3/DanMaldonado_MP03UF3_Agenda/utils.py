from prettytable import PrettyTable

# Creem una funció per mostrar el menú
def print_menu(menu):
    """Mostrem el menú d'opcions.

    Args:
        menu (list): Llista de cada funció
    """
    mida = len(menu)

    taula = PrettyTable()
    taula.field_names = ["*:･ﾟ✧*:･ﾟ--| Funcions |--･ﾟ:*✧･ﾟ:*"]

    for i in range(len(menu)):
        taula.add_row([f"{i+1}. {menu[i]}"])

    taula.add_row([f"{mida+1}. SORTIR"])

    print(taula)

def manage_lines(arxiu, dades_persona, mod=False, arxivar=False):
    """Utilitzem aquesta funció per crear arxius i afegir dades a un arxiu ja creat.

    Args:
        arxiu (str): Arxius a crear o al qual afegirem.
        dades_persona (list): Llista de les dades de la persona
        arxivar (bool, optional): Creem arxiu en cas que volguema arxivar. Defaults to False.
    """
    try:
        # Si anem a modificar o arxivar farem una acció diferent amb el fitxer.
        if mod or arxivar:
            print(dades_persona)
            with open(f"{'txt/' if arxivar else ''}"+arxiu, "w", encoding="utf-8") as f:
                f.write("".join(str(dada) for dada in dades_persona))
            print(f"{'Cerca' if arxivar else 'Modificació'} desada correctament.")
        
        else:
            with open(arxiu, "a", encoding="utf-8") as f:
                f.write(", ".join(str(dada) for dada in dades_persona))
            print("Entrada afegida correctament.")

    except IOError:
        print(f"No s'ha pogut escriure a l'arxiu {arxiu}.")
    except:
        print(f"Alguna cosa no ha funcionat bé.")

def read_lines(arxiu):
    """Passem l'arxiu a una llista de línies

    Args:
        arxiu (str): Arxiu que passarem a llista.

    Returns:
        list: Llista de l'inies de l'arxiu
    """
    arxiu = f"{arxiu}"
    lines = []
    try:
        with open(arxiu,"r", encoding="utf-8") as f:
            lines = f.readlines()
    
    except IOError:
        print(f"No s'ha pogut llegir a l'arxiu {arxiu}")
    except:
        print("Alguna cosa no ha funcionat bé.")
    
    return lines

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
        return valid_input(text, options)
    else:
        return option      
      
def nom_cognom_valid(text, mod=False):
    """Comprovem que el nom o cognom introduits siguin valids.

    Args:
        text (str): Text introduit.
        mod (bool, optional): En cas que estiguem modificant acceptem retorn. Defaults to False.

    Returns:
        _type_: _description_
    """
    entrada_valida = False
    while not entrada_valida:
        entrada = input(text)
        if entrada.isalpha() or (mod and entrada == "") or " " in entrada:
            entrada = entrada.strip().title()
            entrada_valida = True
    return entrada

def telegram_valid(text, mod=False):
    """Comprovem que el telegram introduit sigui vàlid.

    Args:
        text (str): Telegram introduit
        mod (bool, optional): En cas que estiguem modificant acceptem retorn. Defaults to False.

    Returns:
        str: El telegram
    """
    es_valid = False
    while not es_valid:
        telegram = input(text)
        if mod and telegram == "":
            es_valid = True
            
        elif telegram and all(c.isalnum() or c == '_' for c in telegram[1:]) and telegram[0] == "@":
            es_valid = True
            
        else:
            print("ERROR: Entrada inválida.")
    return telegram
 
def file_by_dictionary(cognom, persones):
    """Creem fixters basant-nos en el cognom de la persona per cada clau d'un diccionari.

    Args:
        cognom (str): Cognom de la persona
        persones (str): Dades de la persona
    """
    try:
        ruta = f"txt/{cognom}.txt"
        with open(ruta, "w", encoding="utf-8") as f:
            for linia in persones:
                f.write(linia)
        print(f"Arxiu {ruta} creat correctament.")
    except IOError:
        print(f"No s'ha pogut escriure a l'arxiu {ruta}.")
    except:
        print(f"Alguna cosa no ha funcionat bé." )