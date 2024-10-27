
import random
from inputSegur import input_int_segur
MINES = 5
MIDA = 5


""" 1. (1 punt) 
Fes una funció en Python anomenada crea_matriu, 
que rep 1 paràmetres, que corresponen al número de files i al número 
de columnes, per defecte de valor MIDA , i que retorna una llista de dues dimensions 
on l’element i j està format per un diccionari {"n":0,"t":True} 
on:
    - "n" és un sencer inicialitzat a 0  (serà el nombre de mines veines que té la casella)
    - "t" és un booleà que indica si la casella està tapada

"""
def crea_matriu(n=MIDA):
    return [[{"n":0, "t":True} for j in range(n)] for i in range(n)]


""" 2. (2 punts) 
Fes una funció en Python anomenada print_matriu, 
que rep 3 paràmetres:
    - la matriu
    - la llista de mines marcades pel jugador (inicialment considera que és una llista buida)
    - dev mode desenvolupament, que per defecte està a True

imprimeix la matriu en format dev de manera similar al que es veu,
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
1  *  1  0  0  
1  1  2  1  1  
2  2  2  *  1  
*  *  2  1  1  
*  3  1  0  0

en mode joc ( amb el paràmetre dev a False)
les caselles que durant el joc el jugador ha marcat com a mines 
mostra @, i les que el jugador hagi destapat mostrarà el valor n 
del diccionari
per exemple si la matriu té aquest contingut 
[
    [{'n': 1, 't': False}, {'n': -1, 't': False}, {'n': 1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}], 
    [{'n': 1, 't': False}, {'n': 1, 't': False}, {'n': 2, 't': False}, {'n': 1, 't': True}, {'n': 1, 't': True}], 
    [{'n': 2, 't': True}, {'n': 2, 't': True}, {'n': 2, 't': True}, {'n': -1, 't': True}, {'n': 1, 't': True}], 
    [{'n': -1, 't': True}, {'n': -1, 't': True}, {'n': 2, 't': True}, {'n': 1, 't': True}, {'n': 1, 't': True}], 
    [{'n': -1, 't': True}, {'n': 3, 't': True}, {'n': 1, 't': True}, {'n': 0, 't': True}, {'n': 0, 't': True}]
]
i llista_mines [(0,1)]

1  @  ·  ·  ·   
1  1  2  ·  ·  
·  ·  ·  ·  ·  
·  ·  ·  ·  ·  
·  ·  ·  ·  · 

"""
def print_matriu(matriu,llista_mines,dev=True):
    print()
    print()
    for fila in matriu:
        print(fila)
  
    print()
    print()

    for i in range(MIDA):
        print(" ",end="")
        for j in range(MIDA):
            casella = matriu[i][j]
            c="·"
            if casella["t"]:
                if dev:
                    if es_mina(casella):
                        c="*"
                    else:
                        c=casella['n']
                elif es_marcada(i,j,llista_mines):
                    c="@"
                print(c,end="  ")
            else:
                print(casella["n"],end="  ")
        print()
    print("==="*(MIDA))




def posicio_aleatoria():
    return random.randint(0,MIDA-1),random.randint(0,MIDA-1)

def coloca_mina(x,y,matriu):
    matriu[x][y]["n"] = -1

""" 3. (1 punts) 
Fes una funció en Python anomenada coloca_mines
que rep 1 paràmetre,la matriu
i coloca n MINES a la matriu, assegurant-se que 
les mines es col·loquen sempre en caselles buides
"""
def coloca_mines(matriu):

    i = 0
    while i < MINES:
        x,y = posicio_aleatoria()
        casella = matriu[x][y]
        if es_buida(casella):
            coloca_mina(x,y,matriu)
            i+=1



def es_mina(casella):
    return casella["n"] == -1

def es_buida(casella):
    return casella["n"] == 0
def es_marcada(i,j,llista_mines):
    return (i,j) in llista_mines

""" 4. (2 punts) 
Fes una funció en Python anomenada veins
que rep 2 paràmetres, la x, i la y
i retorna una llista de tuples (x,y) que corresponen al les coordenades dels veins de la casella,
tingues en compte que hi ha caselles que estan a límit, per exemple les crides seGüents:
    
    veins(0,0) retorna [(0, 1), (1, 0), (1, 1)]
    i 
    veins(1,1) retorna [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]


coordenades dels de veins de la
"""


def veins(x,y):
    llista_veins=[]


    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (i >= 0 and i< MIDA) and (j >= 0 and j< MIDA) :
                coordenades = (i,j)
                llista_veins.append(coordenades)
    llista_veins.remove((x,y))

    # caselles superiors
    # if x-1>=0 and  y-1 >=0:
    #     coordenades = (x-1,y-1)
    #     llista_veins.append(coordenades)
    # if x-1 >=0:
    #     coordenades = (x-1,y)
    #     llista_veins.append(coordenades)
    # if x-1>=0 and  y+1 < MIDA:
    #     coordenades = (x-1,y+1)
    #     llista_veins.append(coordenades)
    # # caselles mateixa fila
    # if y-1 >=0:
    #     coordenades = (x,y-1)
    #     llista_veins.append(coordenades)
    # if y+1 < MIDA:
    #     coordenades = (x,y+1)
    #     llista_veins.append(coordenades)

    # # caselles inferiors
    # if x+1 < MIDA and  y-1 >= 0:
    #     coordenades = (x+1,y-1)
    #     llista_veins.append(coordenades)
    # if x+1 < MIDA :
    #     coordenades = (x+1,y)
    #     llista_veins.append(coordenades)
    # if x+1 < MIDA and  y+1 < MIDA:
    #     coordenades = (x+1,y+1)
    #     llista_veins.append(coordenades)

    print(llista_veins)


    return llista_veins    


""" 4. (0,5 punt) 
Fes una funció en Python anomenada calcula_veins_casella
que rep 3 paràmetres x,y qe correspon a la posició de la casella i la matriu
i retorna un sencer que indica quantes mines veïnes té aquesta casella, utilitza la funció veins
per exemple:
    calcula_veins_casella(0,0,matriu) retorna 1
    
        1  *  1  0  0  
        1  1  2  1  1  
        2  2  2  *  1  
        *  *  2  1  1  
        *  3  1  0  0  
"""
def calcula_veins_casella(x,y,matriu):
    num_veins = 0
    llista_veins = veins(x,y)
    for coordenada in llista_veins:
        vei = matriu[coordenada[0]][coordenada[1]]
        if es_mina(vei):
            num_veins+=1
        
    return num_veins


""" 5. (0,5 punt) 
Fes una funció en Python anomenada calcula_tots_veins(matriu)
que rep 1 paràmetre:
    la matriu
i calcula els veins de cada casella si la casella no és una mina,
és a dir modifica el valor n de diccionari de cada casella que no és
una mina
    
        1  *  1  0  0  
        1  1  2  1  1  
        2  2  2  *  1  
        *  *  2  1  1  
        *  3  1  0  0  
"""


def calcula_tots_veins(matriu):
    for i in  range(MIDA):
        for j in range(MIDA):
            if not es_mina(matriu[i][j]):
                num_veins=calcula_veins_casella(i,j,matriu)
                matriu[i][j]['n']=num_veins
""" 6. (0,5 punt) 
Fes una funció en Python anomenada destapa_casella
que rep 3 paràmetres:
    x,y i
    la matriu
i si la casella és una mina imprimeix "BOOOOOM" i retorna False
altre cas 
    posa la clau "t" del diccinnari de la casella x,y a False
    i retorna True

"""



def destapa_casella(x,y,matriu):
    casella = matriu[x][y]

    if es_mina(casella):
        print("BOOOM, has xafat una mina!!")
        return False
    else:
        matriu[x][y]['t'] = False
        return True
def demana_coordenades():
    x=0
    y=0
    ok=False
    mis=""
    while not ok:
        print(mis)
        x,ok,mis = input_int_segur("Introdueix la coordenada x:",0,MIDA-1)
        ok= not ok
    ok=False
    while not ok:
        print(mis)
        y,ok,mis = input_int_segur("Introdueix la coordenada y:",0,MIDA-1)
        ok= not ok
    
    return x,y




def vols_marcar_mina():
    r = input("Vols marcar una mina ??").upper()
    sis = ["S","SI","Y","YES"]
    return r in sis


def totes_marcades(llista,matriu):
    llista_mines_reals = []
    for i in range(MIDA):
        for j in range(MIDA):
            if es_mina(matriu[i][j]):
                llista_mines_reals.append((i,j))
    
    return all([True if mina in llista_mines_reals else False for mina in llista])
    #return len(llista)==MINES and all([True if es_mina(matriu[marcada[0]],[marcada[1]]) else False for marcada in llista])

"""
Programa principal:
    - crea la matriu de mida MIDA
    - imprimeix la matriu
    - coloca les mines
    - imprimeix la matriu
    - calcula tots el veins
    - imprimeix la matriu
    - metre el joc no s'hagi acabat
        - demana coordenades al jugador (pots utilitzar input_int_segur fet a classe)
        - demana si vols marcar una mina o destapar la casella
        - comprova si s'ha acabat el joc
            - el jugador ha trobat totes les mines
            - el jugador a destapat una mina
        - si el joc ha acabat mostra missatge corresponent jugador


"""

def main():
    matriu = crea_matriu(MIDA)
    llista_mines=[]
    
    print_matriu(matriu,llista_mines)
    coloca_mines(matriu)
    print_matriu(matriu,llista_mines)
    calcula_tots_veins(matriu)
    print_matriu(matriu,llista_mines)
    
    acabat = False
    while not acabat:
        print_matriu(matriu,llista_mines,False)


        x,y = demana_coordenades()
        if vols_marcar_mina():
            llista_mines.append((x,y))
            acabat = totes_marcades(llista_mines,matriu)
            if acabat:
                print("Enhorabona!!!!")
        else:
            print(x,y)
            acabat = not destapa_casella(x,y,matriu)

    print_matriu(matriu,llista_mines)




if __name__ == "__main__":
    main()
    