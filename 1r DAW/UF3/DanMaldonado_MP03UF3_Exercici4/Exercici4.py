# Haureu d’implementar un programa robust i modular amb la següent sintaxi:
#               $python3 ex4.py file [c] [-i -p -w -f] [--help]

import sys

# 1. Escriviu un programa en Python per comptar el nombre de línies d'un fitxer de text que passeu com a 1r argument.
def n_linies(ll_arxiu):
    """Retorna la quantitat de línies d'un fitxer

    Args:
        ll_arxiu (list): Arxiu a comptar.

    Returns:
        int: Longitud de línies de l'arxiu.
    """
    return len(ll_arxiu)


# 2. Afegiu un segon argument opcional c, que compta les línies que contenen el caràcter especificat en c.
def n_caracter(arxiu, c):
    """Compta les línies que tenen el caràcter especificat.

    Args:
        arxiu (str): Arxiu al qual es buscarà.
        c (str): Caràcter a buscar.

    Returns:
        int: Nombre de línies que contenen el caràcter especificat.
    """
    conte_c = sum(1 for linia in arxiu if c in linia)
    return conte_c

# 3. Si s’especifica l’argument opcional -i, el comportament és al contrari, compta totes les línies que no contenen el caràcter c, 
# evidenment cal haver posat l’argument c.
def invertir(ll_arxiu, comptador):
    """ Inverteix el resultat dels paràmetres. Ex: text.txt e -i (Compta les línies que NO tenen e.)

    Args:
        ll_arxiu (list): Llista de línies de l'arxiu.
        comptador (int): Resultat dels paràmetres ficats anteriorment.

    Returns:
        int: Resultat invertit dels paràmetres ficats.
    """
    comptador = len(ll_arxiu) - comptador
    return comptador

# 4. Afegiu al programa anterior l’argument opcional -p, que farà que compti les línies de l’arxiu que comencen pel caràcter c. +
# Recordeu que si s’especifica -i farà el contrari. 
def comenca_p(ll_arxiu, c):
    """Compta el nombre de línies que començen pel caràcter especificat, si s'especifica -i fa el contrari.   

    Args:
        ll_arxiu (list): Llista de les línies de l'arxiu
        c (str): Caràcter a buscar.

    Returns:
        int: Nombre de línies que començen pel caràcter especificat.
    """
    return sum(1 for linia in ll_arxiu if linia[0] == c)

# 5. Si en comptes d’una p minúscula és una P majúscula, és fixarà en l’últim caràcter de la línia (aneu amb compte amb el “\n” final 
# de línia que no considerem últim caràcter en aquest cas). Els arguments -p i -P no es poden posar a la vegada, en aquest cas s’ha 
# de mostrar error.
def acaba_P(ll_arxiu, c):
    """Compta el nombre de línies que acaben pel caràcter especificat, si s'especifica -i fa el contrari.   

    Args:
        ll_arxiu (list): Llista de les línies de l'arxiu
        c (str): Caràcter a buscar.

    Returns:
        int: Nombre de línies que acaben pel caràcter especificat.
    """
    return sum(1 for linia in ll_arxiu if linia.rstrip("\n")[-1] == c)

# 6.Si a més hi ha l’argument opcional -w comptarà, a part de les línies, les paraules que contenen el caràcter c. Si no s’especifica c 
# haurà de comptar totes les paraules. Recordeu que si hi ha -i el comportament és al contrari i -p/-P miren el primer o l’últim caràcter,
# respectivament.
def comptar_paraules(ll_arxiu, args, c=None):
    """Fa el recompte dels argument -p o -P pero per a cada paraula, si no s'especifiquen els arguments -p o -P, 
    compta només el nombre de paraules. Si el paràmetre -i es actiu, inverteix els resultat i canvia el missatge.

    Args:
        ll_arxiu (list): Llista de línies del arxiu.
        args (dicc): Diccionari de arguments per comprovar si l'usuari els ha introduit.
        c (str, optional): Caràcter especificat, por no haver-hi i comptar només el nombre de paraules. Defaults to None.

    Returns:
        str: Missatge corresponent per a cada argument i opcions especificades.
    """
    ll_paraules = [paraula for linia in ll_arxiu for paraula in linia.split()]
    
    if args["-p"]:
        c_paraules = comenca_p(ll_paraules, c) if not args["-i"] else invertir(ll_paraules, comenca_p(ll_paraules, c))
        return f"Hi ha {c_paraules} paraules que {'NO ' if args['-i'] else ''}començen amb {c}."

    elif args["-P"]:
        c_paraules = acaba_P(ll_paraules, c) if not args["-i"] else invertir(ll_paraules, acaba_P(ll_paraules, c))
        return f"Hi ha {c_paraules} paraules que {'NO ' if args['-i'] else ''}acaben amb {c}."

    if c is not None:
        n_paraules = (1 for linia in ll_arxiu for paraula in linia.split() if c in paraula)
        c_paraules = sum(n_paraules) if not args["-i"] else invertir(ll_paraules, sum(n_paraules))
        return f"Hi ha {c_paraules} paraules que {'NO ' if args['-i'] else ''}contenen {c}."
    
    else:
        c_paraules = sum(len(linia.split()) for linia in ll_arxiu)
        return f"Hi ha {c_paraules} paraules."
    
# Missatge d'ajuda
def ajuda():
    """Mostra un missatge d'ajuda"""
    
    print("""
    Sintaxi: $python3 ex4.py file [c] [-i -p -w -f] [--help]

    Arguments:
        file: Nom de l'arxiu.
        c: caràcter a buscar.
        -i: Invers.
        -p: Principi línia/paraula.
        -P: Final línia/paraula.
        -w: Mira també les paraules.
        -f: Sortida a sortida.txt
        
        --help: Ajuda
        
    Exemple:
        $python3 ex4.py text.txt l -p -w -f
            Totes les línies i paraules de l'arxiu text.txt que començen per l amb la sortida a sortida.txt
              """)

# 9. En cas que la combinació d’arguments no sigui correcta haurà de mostrar el missatge d’error corresponent i mostrar la pantalla d’ajuda.
def args_error():
    """Mostra un missatge d'error, l'ajuda i surt del programa."""
    print("ERROR: Combinació d'arguments invàlida.")
    ajuda()
    sys.exit()

def main():
    args = {
        "-i": False,
        "-p": False,
        "-P": False,
        "-w": False,
        "-f": False,
    }

    # Valida que no hi hagin arguments incorrectes.
    for argument in sys.argv[3::]:
        if argument not in args:
            args_error()

    # Fica a True els arguments introduïts.
    for i in sys.argv:
        args[i] = i in args 

    # Missatge d'error si introdueix paràmetres incompatibles.
    if len(sys.argv) == 4 and args["-w"] and args["-i"]:
        args_error()
    if args["-p"] and args["-P"]:
        print("ERROR: No es poden ficar -p i -P alhora.")
        sys.exit()

# 10. Si no s’especifica cap argument cal que mostri un missatge d’error i indiqui quina és la comanda per obtenir ajuda.
    if len(sys.argv) == 1:
        print("""ERROR: Ha de tenir com a mínim 1 argument. 
              --help per obtenir ajuda.""")
        sys.exit()
    
# 8. Si només hi ha un argument i és --help, mostrarà una pantalla d’ajuda on s’expliqui la funcionalitat de cada argument i mostri 
# alguns exemples.
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        ajuda()
        sys.exit()
    
    try:
        ARXIU = sys.argv[1]

        with open(ARXIU, "r") as f:
            LL_ARXIU = f.readlines()

        # Inicialitzem comptadors i sortida
        comptador = 0
        c_char = 0
        sortida = ""
        
        # Compta les línies de l'arxiu.
        if len(sys.argv) == 2:
            sortida = f"El fitxer {ARXIU} té {n_linies(LL_ARXIU)} línia/es."
            
        elif len(sys.argv) > 2:
            
            # Compta les paraules de l'arxiu.
            if sys.argv[2] == "-w":
                sortida = comptar_paraules(LL_ARXIU, args, c=None)

            else:
                
                # Comprovem que el caràcter sigui vàlid.
                c = sys.argv[2]
                if len(c) != 1:
                    print("ERROR: Longitud del caràcter incorrecta.")
                    sys.exit()
                
                """ Per a cada element, invertim el resultat i la sortida si -i es actiu. """
                # Comptem el nombre de línies amb el caràcter especificat. Tenint en compte l'ordre de paràmetres.
                if len(sys.argv) == 3 or sys.argv[3] == "-i" or sys.argv[3] == "-f":
                    c_char = n_caracter(LL_ARXIU, c) if not args["-i"] else invertir(LL_ARXIU, n_caracter(LL_ARXIU, c))
                    sortida = f"Al fitxer hi han {c_char} línia/es {'amb' if not args['-i'] else 'sense'} {c}'s."
            
                # Comptem les línies que començen pel caràcter especificat.
                if args["-p"]:
                    comptador = comenca_p(LL_ARXIU, c) if not args["-i"] else invertir(LL_ARXIU, comenca_p(LL_ARXIU, c))
                    sortida = f"L'arxiu conté {comptador} línia/es que {'NO ' if args['-i'] else ''}començen per {c}."
                    
                # Comptem les línies que acaben pel caràcter especificat.                    
                if args["-P"]:
                    comptador = acaba_P(LL_ARXIU, c) if not args["-i"] else invertir(LL_ARXIU, acaba_P(LL_ARXIU, c))
                    sortida = f"L'arxiu conté {comptador} línia/es que {'NO ' if args['-i'] else ''}acaben per {c}."

                # A més, comptem el nombre de paraules, o paraules amb els criteris dels paràmetres -p o -P
                if args["-w"]:
                    sortida += f"\n{comptar_paraules(LL_ARXIU, args, c)}"
            
        else:
            print("ERROR: Massa arguments proporcionats.")
            sys.exit()
            
# 7. Si també hi ha l’argument opcional -f, la sortida no serà per pantalla sinó a un arxiu anomenat sortida.txt.
        if args["-f"]:
            try:
                with open("sortida.txt", "w") as f: 
                    f.writelines(sortida)
                    print("Fitxer creat exitosament.")
            except:
                print("ERROR: No s'ha pogut crear el fitxer.")
                
        else:
            print(sortida)
                        
    except FileNotFoundError:
        print("No s'ha trobat el fitxer.")

if __name__ == "__main__":
    main()
