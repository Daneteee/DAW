taulell = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def jugar():
    peca = input ("Que vols ser? (O-X): ")
    while True:
        resposta = input ("Fica la coordenada: ")
        
        if resposta == "a1":
            taulell[0][0] = peca
        
        elif resposta == "a2":
            taulell[0][1] = peca
        
        elif resposta == "a3":
            taulell[0][2] = peca

        elif resposta == "b1":
            taulell[1][0] = peca

        elif resposta == "b2":
            taulell[1][1] = peca

        elif resposta == "b3":
            taulell[1][2] = peca

        elif resposta == "c1":
            taulell[2][0] = peca

        elif resposta == "c2":
            taulell[2][1] = peca

        elif resposta == "c3":
            taulell[2][2] = peca

        mostrarTaulell()
        
def mostrarTaulell():
    for i in taulell:
        print (i) 

while True:
    pregunta = input ("\n Menú \n ------------------ \n 1. Jugar \n 2. Sortir \n Que vols fer?: ")
    if pregunta == "1":
        jugar()


    elif pregunta == "2":
        break