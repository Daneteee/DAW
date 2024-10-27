import utils
from prettytable import PrettyTable
from datetime import datetime

# Menú d'inici
menu = ("Llistat", "Alta", "Modificació", "Baixa", "Consulta", "Generar arxius per cognom")

ARXIU = "/home/dan/Documents/VSCode/UF3/DanMaldonado_MP03UF3_Agenda/agenda.txt"

# 1. Fer un llistat de dades. Mostrarà la informació amb paginació, per defecte de 10 en 10, o bé per un valor que li passem com a paràmetre, 
# és a dir mostra 10 i espera a que es premi intro per seguir, i 10 més, fixeu-vos en la captura de pantalla.
def show_table(ll_arxiu, n, mod=False):
    """Mostrem la taula cada "n" nombre de línies.

    Args:
        ll_arxiu (list): Llista de línies de l'arxiu
        n (int): Nombre de salts de línia
        mod (bool, optional): En cas  que estiguem fem modificacions al arxiu. Defaults to False.
        eliminar (bool, optional): En cas que volguem eliminar alguna entrada. Defaults to False.

    Returns:
        fila, dades: La fila que es vol modificar i les dades d'aquesta
    """
    n = 10 if n == "" else n
    print("Llistat\n--------------------")

    taula = PrettyTable()
    taula.field_names = ["ID", "Nom", "Cognoms", "Telèfon", "@telegram"]
    for i in range(1, len(ll_arxiu) + 1):
        # Retalla les línies del arxiu per quedar-se només amb les dades
        dades_persones = ll_arxiu[i - 1][:-1].split(", ")
        taula.add_row([i, *dades_persones])
        if i % n == 0:
            # Imprimeix la taula desde on va acabar la última iteració per no repetir dades.
            print(taula[i-n:i])

            if mod:
                fila = utils.secure_int("Quina fila vols? (enter per continuar): ", int(str(i)[0]), i, True)
                if fila != "" and mod:
                    dades = ll_arxiu[fila - 1]
                    show_person_data(fila, ll_arxiu[fila - 1])
                    return fila, dades

            else:
                input("Enter para continuar: ")
            c = i
    if len(ll_arxiu) % n != 0:
        print(taula[c:])
        if mod:
            fila = utils.secure_int("Quina fila vols? (enter per continuar): ", int(str(i)[0]), i, True)
            if fila != "" and mod:
                dades = ll_arxiu[fila - 1]
                show_person_data(fila, ll_arxiu[fila - 1])
                return fila, dades
     
     
def show_person_data(fila, dades_persona):
    """Mostra les dades d'una persona en format PrettyTable
    Args:
        fila (int): Fila corresponent
        dades_persona (list): Dades de la persona
    """
    taula_persona = PrettyTable()
    taula_persona.field_names = ["ID", "Nom", "Cognoms", "Telèfon", "@telegram"]

    dades_persones = dades_persona[:-1].split(", ")
    taula_persona.add_row([fila, *dades_persones])
    
    print(taula_persona)


# 2. Afegir entrada (amb validació utilitzant try except), i comprovant que les dades siguin correctes per cada camp.
def add_entry(arxiu, mod=False, ll_arxiu=None, dades=None, fila=None):
    """Afegim una entrada a la agenda, utilitzem aquesta funció també en cas que volguem
       modificar dades.

    Args:
        arxiu (str): Ruta de l'arxiu
        mod (bool, optional): En cas que es vulgui modificar dades. Defaults to False.
        ll_arxiu (list, optional): Llista de línia de l'arxiu. Defaults to None.
        dades (list, optional): Llista de dades de la persona. Defaults to None.
        fila (int, optional): Fila per modificar en cas que modifiquem. Defaults to None.
    """
    if mod:
        nom, cognom, telefon, telegram = (dada for dada in dades.split(", "))
    
    # si la funció utils.nom_cognom_valid() no retorna un valor vàlid, la variable mantindrà el seu valor anterior. 
    nom = utils.nom_cognom_valid(f"Introdueix el nom{(' (' + nom + ')') if mod else ''}: ", mod) or nom
    cognom = utils.nom_cognom_valid(f"Introdueix el cognom{(' ('+ cognom +')') if mod else ''}: ", mod) or cognom

    telefon = utils.secure_int(f"Introdueix telèfon{(' ('+ telefon +')') if mod else ''}: ", 600000000, 799999999, True if mod else False) or int(telefon)
    telegram = utils.telegram_valid(f"Introdueix el telegram{(' ('+ telegram[:-1]+')') if mod else ''}: ", True if mod else False ) or telegram

    if not mod:
        utils.manage_lines(arxiu, ["\n"+nom, cognom, str(telefon), telegram])
    else:
        # Si estem modificant, editem a l'agenda els valors introduits
        ll_arxiu[fila - 1] = f"{nom}, {cognom}, {telefon}, {telegram}"
        utils.manage_lines(arxiu, ll_arxiu, True)

# 3. Modificar entrada. Primer cal llistar tots, utilitzant la funció que implementa el llistat a l’apartat anterior, 
# i demanar quina fila es vol modificar, (cal verificar que és una fila vàlida) es mostren les dades de la fila corresponen 
# i demana camp per camp si es vol modificar, si es prem intro, s'entén que les dades d’aquell camp no es modifiquen, sinó 
# cal seguir la mateixa validació que en afegir entrada.  Un cop modificada l’entrada, cal que mostreu missatge que l’entrada 
# s’ha modificat correctament, o en cas contrari. que hi ha hagut algun problema
def modify_entry(ll_arxiu, arxiu):
    """Modifiquem una entrada a l'arxiu.

    Args:
        ll_arxiu (list): Llista de línies de l'arxiu.
        arxiu (str): Arxiu a modificar. 
    """

    try:
        fila, dades = show_table(ll_arxiu, 10, True)
        modificar = utils.valid_input("Vols modificar les dades (S/N): ", ["S","s", "N", "s"])
        
        if modificar in "Ss":
            print("Prem retorn per deixar el valor original.")
            add_entry(arxiu, True, ll_arxiu, dades, fila)
            
    except TypeError:
        print("Sortint...")
    
    
def delete_entry(ll_arxiu):
    """Eliminem una entrada de l'agenda.

    Args:
        ll_arxiu (list): Llista de línies de l'arxiu.
    """
    try:
        fila, dades = show_table(ll_arxiu, 10, True)
        
        confirmacio = utils.valid_input("Estàs segur de vols eliminar la fila (S/N)? ", ["S","s", "N", "s"])
        if confirmacio in "Ss":
            try:
                del ll_arxiu[fila-1]
                utils.manage_lines(ARXIU, ll_arxiu, True)
                print("Entrada eliminada amb exit.")

            except:
                print("ERROR: No s'ha pogut esborrar.")
    except TypeError:
        print("Sortint...")


# 5. Cercar dades de l’agenda, segons el valor posat en un camp. Per exemple, demana el nom i mostra les dades de l’entrada que 
# coincideix amb aquell nom, no cal que la coincidència sigui exacta, pot ser una coincidència parcial, finalment demana si volem 
# la sortida en un fitxer a més a més de per la consola, sempre cal implementar la sortida per la consola. El fitxer s’ha de dir
# cerca-XXXXXXXXXX.txt on XXXXXXXXXXX representa el timestamp del moment en que es crea l’arxiu.
def search_entries(ll_arxiu):
    """ Fem una cerca d'un camp en concret i mostrem a l'usuari els resultats, demanant si els vol guardar
        a un fitxer.

    Args:
        ll_arxiu (list): Llista de línies de l'arxiu.
    """
    print("1. Nom, 2. Cognom, 3. Teléfon, 4. Telegram")
    camp_escollit = utils.valid_input("De quin camp vols fer la cerca?  ", ["1", "2", "3", "4"])

    if camp_escollit == "1":
        camp = utils.nom_cognom_valid("Introdueix nom: ")
    
    elif camp_escollit == "2":
        camp = utils.nom_cognom_valid("Introdueix cognom: ")
        
    elif camp_escollit == "3":
        camp = utils.secure_int(f"Introdueix telèfon: ", 600000000, 799999999)

    elif camp_escollit == "4":
        camp = utils.telegram_valid("Introdueix telegram: ")
        
    else:
        print("ERROR: Valor incorrecte.")
        
    cerques = []
    for linia in ll_arxiu:
        # Si el camp es un int el passem a string, també verifiquem que es trobi al camp escollit (dividim la línia per comes
        # i agafem el camp corresponent):skull: :skull: 
        if (camp.lower() if type(camp) != int else str(camp)) in linia.lower().split(", ")[int(camp_escollit)-1]:
            print(linia)
            cerques.append(linia)

    arxivar = utils.valid_input("Vols desar la cerca a un arxiu (S/N)? ", ["S", "s", "N", "n"])
    timestamp = int(datetime.timestamp(datetime.now()))
    
    if arxivar in "Ss":
        utils.manage_lines(str(timestamp)+".txt", cerques, False, True)
    
    
# 6. Genera arxius diferents per cada cognom diferent que hi ha en tots els cognoms, En cada arxiu hi haurà les persones que 
# tinguin aquest cognom (tan pot ser com a primer cognom o com a segon cognom). Els noms dels arxius han de ser cognom.txt. 
def read_lastname(ll_arxiu):
    """Creem arxius per a cada cognom

    Args:
        ll_arxiu (list): Llista de línies de l'arxiu
    """
    dicc = {}
    for linia in ll_arxiu:
        cognoms = linia.split(", ")[1]
        for cognom in cognoms.split():
            if cognom not in dicc:
                dicc[cognom] = [linia for linia in ll_arxiu if cognom in linia]
        
    for cognom, persones in dicc.items():
        utils.file_by_dictionary(cognom, persones)


def main():
    
    sortir = False
    
    while not sortir:
        utils.print_menu(menu)
        eleccio = input("\nQue vols fer? ")
        LL_ARXIU = utils.read_lines(ARXIU)

        if eleccio == "1":
            n = utils.secure_int("Introdueix el nombre de salts (Enter: 10 per defecte): ", None, None, True)
            show_table(LL_ARXIU, n)
    
        elif eleccio == "2":
            add_entry(ARXIU)
            
        elif eleccio == "3":
            modify_entry(LL_ARXIU, ARXIU)
            
        elif eleccio == "4":
            delete_entry(LL_ARXIU)
    
        elif eleccio == "5":
            search_entries(LL_ARXIU)
            
        elif eleccio == "6":
            read_lastname(LL_ARXIU)
    
        elif eleccio == "7":
            print("\n       ・ ゜✭ ・ . ・ ✫ ・゜ ")
            print("       ˚ ○ ◦˚ Fins aviat! ˚◦ ○  ")
            print("        ・ ゜✭ ・ . ・ ✫ ・ ゜ ")
            sortir = True
            
        else:
            print("ERROR: Entrada incorrecta.")
    
    
if __name__ == "__main__":
    main()