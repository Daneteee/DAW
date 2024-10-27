"""
Joc “Pesca MINES”
Lliurament examen_uf2.py (o més arxius) amb el codi funcional. 
No cal comentar el codi.

Les funcions que es demanen cal implementar-les segons indica l’enunciat. 
No es pot utilitzar break, ni cap estructura de control que no formi part 
de la programació estructurada. 

Podeu definir més funcions de les indicades que fan coses petites 
per fer un codi més modular i fàcil de seguir, per exemple:

def coloca_mina(x,y,matriu):
    matriu[x][y]["n"] = -1

"""


import random

# definició de constants
MINES = 5
MIDA = 5


""" 1. (1 punt) 
Fes una funció en Python anomenada crea_matriu, 
que rep 1 paràmetre, que correspon al número de files i al número 
de columnes, per defecte de valor MIDA , i que retorna una llista de dues dimensions 
on l’element i , j està format per un diccionari amb aquests valors {"n":0,"t":True} 
on:
    - "n" és un sencer inicialitzat a 0  (serà el nombre de mines veines que té la casella)
    - "t" és un booleà que indica si la casella està tapada

    (resultat)

    [   [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}]]

"""
def crea_matriu(n=MIDA):
        matriu = [[{'n': 0, 't': True} for i in range(n)] for j in range(n)]
        return matriu


""" 2. (2 punts) 
Fes una funció en Python anomenada print_matriu, 
que rep 3 paràmetres:
    - la matriu
    - la llista de mines marcades pel jugador (inicialment considera que és una llista buida)
    - dev mode desenvolupament, que per defecte està a True

si dev = True
imprimeix la matriu en format de manera similar al que es veu,

- si la posició correspon a una mina imprimeix un *
- si la posició correspon a una casella imprimeix el valor n del diccionari

per exemple si matriu té aquest contingut
[
    [{'n': 1, 't': True}, {'n': -1, 't': True}, {'n': 1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}], 
    [{'n': 1, 't': True}, {'n': 1, 't': True}, {'n': 2, 't': True}, {'n': 1, 't': True}, {'n': 1, 't': True}], 
    [{'n': 2, 't': True}, {'n': 2, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 1, 't': True}], 
    [{'n': -1, 't': True}, {'n': -1, 't': True}, {'n': 2, 't': True}, {'n': 1, 't': True}, {'n': 1, 't': True}], 
    [{'n': -1, 't': True}, {'n': 3, 't': True}, {'n': 1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}]
]

imprimirà en mode dev

1  *  1  0  0  
1  1  2  1  1  
2  2  2  *  1  
*  *  2  1  1  
*  3  1  0  0

en mode joc ( amb el paràmetre dev a False)

les coordenades x,y que durant el joc el jugador ha marcat com a mines,
és a dir estan en la llista_mines, 
    
    mostra @,

i les que el jugador hagi destapat mostrarà el valor n 
del diccionari, en cas que no les hagi destapat mostrarà el punt volat (·)
per exemple si la matriu té aquest contingut 

[
    [{'n': 1, 't': False}, {'n': -1, 't': False}, {'n': 1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}], 
    [{'n': 1, 't': False}, {'n': 1, 't': False}, {'n': 2, 't': False}, {'n': 1, 't': True}, {'n': 1, 't': True}], 
    [{'n': 2, 't': True}, {'n': 2, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 1, 't': True}], 
    [{'n': -1, 't': True}, {'n': -1, 't': True}, {'n': 2, 't': True}, {'n': 1, 't': True}, {'n': 1, 't': True}], 
    [{'n': -1, 't': True}, {'n': 3, 't': True}, {'n': 1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}]
]
i llista_mines [(0,1)]

mostrarà

1  @  ·  ·  ·   
1  1  2  ·  ·  
·  ·  ·  ·  ·  
·  ·  ·  ·  ·  
·  ·  ·  ·  · 

"""

def print_matriu(matriu,llista_mines,dev=True):
    for i in range(MIDA):
        for y in range(MIDA):
            if dev:
                if matriu[i][y]['n'] == -1:
                    print("*", end=" ")
                    
                else:
                    print(matriu[i][y]['n'], end=" ")
                    
            else:
                if (i,y) in llista_mines:
                    print("@", end=" ")
                    
                elif matriu[i][y]['t'] == True:
                    print("·", end=" ")
                    
                else:
                    print(matriu[i][y]['n'], end=" ")
        print()


""" 3. (1 punts) 
Fes una funció en Python anomenada coloca_mines
que rep 1 paràmetre, la matriu
i coloca n MINES (el que indiqui la constant definida al principi),
en posicions aleatòries de la matriu, 
cal assegurar-se que les mines es col·loquen sempre en caselles buides,

per col·locar una mina posarem en matriu[x][y]["n"] el valor -1
on x,y són dos valors generats aleatòriament, que corresponent a les coordenades de les mines

"""


def coloca_mines(matriu):
    i = 0
    while i < MINES:
        x = random.randint(0,MIDA - 1)
        y = random.randint(0,MIDA - 1)
        
        if matriu[x][y]["n"] == 0:
            matriu[x][y]["n"] = -1
            i += 1
        

""" 4. (2 punts) 
Fes una funció en Python anomenada veins
que rep 2 paràmetres, la x, i la y
i retorna una llista de tuples (x,y) que corresponen al les coordenades dels veins de la casella,

tingues en compte que hi ha caselles que estan a límit, per exemple les crides següents:
    
    veins(0,0) retorna [(0, 1), (1, 0), (1, 1)]

    0  1  2  3  4
  1 x  =  ·  ·  ·  
  2 =  =  ·  ·  ·  
  3 ·  ·  ·  ·  ·  
  4 ·  ·  ·  ·  ·  
  5 ·  ·  ·  ·  ·  


    i 

    veins(1,1) retorna [(0, 0), (0, 1), (0, 2),
                        (1, 0), (1, 2), 
                        (2, 0), (2, 1), (2, 2)]

    0  1  2  3  4
  1 =  =  =  ·  ·  
  2 =  x  =  ·  ·  
  3 =  =  =  ·  ·  
  4 ·  ·  ·  ·  ·  
  5 ·  ·  ·  ·  ·  


"""
def veins(x,y):
    llista_veins_teorics  =  [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x+1),(y+1,x+1),(y+1,x),(y+1,x-1),(y,x-1)]
    llista_veins = [(i,j) for i,j in llista_veins_teorics if i >= 0 and i < MIDA and j >= 0 and j < MIDA]

    return llista_veins

""" 5. (0,5 punt) 
Fes una funció en Python anomenada calcula_nombre_mines_veines_casella
que rep 3 paràmetres x,y que correspon a la posició de la casella i la matriu
i retorna un sencer que indica quantes mines veïnes té aquesta casella, 
utilitza la funció veins
per exemple:

    calcula_nombre_mines_veines_casella(0,0,matriu) retorna 1
    
        1  *  1  0  0  
        1  1  2  1  1  
        2  2  2  *  1  
        *  *  2  1  1  
        *  3  1  0  0  
"""


def calcula_nombre_mines_veines_casella(x,y,matriu):
    nombre_mines = 0
    ll_veins = veins(x,y)

    for coordenades in ll_veins:
        if matriu[coordenades[0]][coordenades[1]]["n"] == -1:
            nombre_mines += 1
            
    return nombre_mines

""" 6. (1 punt) 
Fes una funció en Python anomenada calcula_totes_mines_veins(matriu)
que rep 1 paràmetre: la matriu
i calcula el nombre de mines veines de cada casella si la casella no és una mina,
és a dir modifica el valor n de diccionari de cada casella que no és una mina,
i hi posa el nombre que retorna calcula_nombre_mines_veines_casella
    
        1  *  1  0  0  
        1  1  2  1  1  
        2  2  2  *  1  
        *  *  2  1  1  
        *  3  1  0  0  
"""
def calcula_totes_mines_veins(matriu):
    for i in range(MIDA):
        for j in range(MIDA):
            if matriu[i][j]["n"] != -1:
                matriu[i][j]["n"] = calcula_nombre_mines_veines_casella(i, j, matriu)

""" 7. (0,5 punt) 
Fes una funció en Python anomenada destapa_casella
que rep 3 paràmetres:
    x,y i
    la matriu

i si la casella és una mina imprimeix "BOOOOOM" i retorna False 

altre cas 
    posa la clau "t" del diccionari de la casella x,y a False
    i retorna True

"""
def destapa_casella(x,y,matriu):
    print(matriu[x][y]["n"])
    if matriu[x][y]["n"] == -1:
        print("BOOOOOM")
        return False
    else:
        matriu[x][y]["t"] = False
        return True


"""
8 (2 punts)
Programa principal:
    - crea la matriu de mida MIDA
    (resultat)
    [
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}]]

    - imprimeix la matriu mode desenvolupador

    (resultat)

        0  0  0  0  0  
        0  0  0  0  0  
        0  0  0  0  0  
        0  0  0  0  0  
        0  0  0  0  0  
    
    - coloca tantes mines com indica MINES

    (resultat)
    [
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': -1, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': -1, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': -1, 't': True}, {'n': 0, 't': True}, {'n': -1, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': -1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}]
    ]
    
    - imprimeix la matriu mode desenvolupador
    (resultat)

            0  0  0  *  0  
            0  0  0  *  0  
            0  0  0  0  0  
            0  0  *  0  *  
            0  0  *  0  0  
    
    - calcula el nombre de mines veïnes que té cada casella
    (resultat) 
    [
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 2, 't': True}],
        [{'n': 0, 't': True}, {'n': 0, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 2, 't': True}],
        [{'n': 0, 't': True}, {'n': 1, 't': True}, {'n': 2, 't': True}, {'n': 3, 't': True}, {'n': 2, 't': True}],
        [{'n': 0, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 3, 't': True}, {'n': -1, 't': True}],
        [{'n': 0, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 3, 't': True}, {'n': 1, 't': True}]
    ]



    - imprimeix la matriu mode desenvolupador
    (resultat) 

        0  0  2  *  2  
        0  0  2  *  2  
        0  1  2  3  2  
        0  2  *  3  *  
        0  2  *  3  1  

    - (0,5 punts) metre el joc no s'hagi acabat 

        - imprimeix la matriu en mode joc

            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  

       
        - (0,5 punts) demana coordenades al jugador (pots utilitzar input_int_segur fet a classe)
        (resultat) 

            Introdueix la coordenada x entre 0 i 5 :0
            Introdueix la coordenada y entre 0 i 5 :0

        - (0,25) demana si vols marcar una mina o destapar la casella que correspon a aquelles coordenades
        (resultat) 
            
            Vols marcar una mina ?? n

          
        - (0,5) comprova si s'ha acabat el joc

            - el jugador ha trobat totes les mines
            - el jugador ha xafat  una mina
        
        - (0,25) si el joc ha acabat mostra missatge corresponent jugador

        (per exemple)

            0  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  
            ·  ·  ·  ·  ·  

            Introdueix la coordenada x entre 0 i 5 :0
            Introdueix la coordenada x entre 0 i 5 :3
            Vols marcar una mina ??n

            BOOOM, has xafat una mina!!

                0  0  2  *  2  
                0  0  2  *  2  
                0  1  2  3  2  
                0  2  *  3  *  
                0  2  *  3  1  



"""

def check_int(num):
    try:
        return int(num)
    except:
        num = input("Introduzca el valor de nuevo: ")
        return check_int(num)
    
def correct_range(num, min=None,max=None):
    if min is not None and max is None:
        return num >= min
    elif min is None and max is not None:
        return num <= max
    elif min is not None and max is not None:
        return num >= min and num <= max
    else:
        return True
    
def secure_int(text, min=None, max=None):
    correct_num = False
    while not correct_num:
        num = input(text)
        num = check_int(num)
        correct_num = correct_range(num, min, max)
    return num

def valid_input(text, options):
    print(f"Opciones válidas: {', '.join(options)}")
    option = input(text)
    if option.upper() not in options:
        return valid_input(text, options)
    else:
        return option


def main():
    #desarem les tuples (x,y) de les posicions marcades com a mines
    llista_mines=[]

    matriu = crea_matriu(MIDA)

    
    coloca_mines(matriu)
    


    calcula_totes_mines_veins(matriu)
    
    print_matriu(matriu, llista_mines, True)
    
    joc_acabat = False
    
    while not joc_acabat:
        print_matriu(matriu, llista_mines, False)
        
        y = secure_int(f"Introdueix la coordenada y entre 1 i {MIDA}: ", 0, MIDA)
        x = secure_int(f"Introdueix la coordenada x entre 1 i {MIDA}: ", 0, MIDA)
        
        marcar = valid_input("Vols marcar la casella? ", ["S","N"])
        
        if marcar.upper() == "S":
            if matriu[x-1][y-1]["n"] == -1:
                llista_mines.append((x-1,y-1))
                if len(llista_mines) == MINES:
                    print("Has guanyat!")
                    joc_acabat = True

        elif marcar.upper() == "N":
            if not destapa_casella(x-1,y-1,matriu):
                print("Has perdut!")
                joc_acabat = True
        
        
        
        
if __name__ == "__main__":
    main()
    