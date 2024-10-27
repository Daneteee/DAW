import random

text = "1, 2, 3, pica paret"

def joc(text):

    passos_usuari = 0
    passos_necesaris = random.randint(3, 10)

    posicio = 0
    while True:
        if posicio == 0:
            posicio = random.randint(0, len(text))

        else:
            posicio = random.randint(posicio, len(text))

        resposta = input("Mou o quiet? ")

        if resposta == "mou":
            passos_usuari += 1

        print(text[:posicio])

        if posicio == len(text) and resposta == "mou":
            print ("Has perdut!")
            break
        
        elif posicio == len(text) and resposta == "quiet":
            posicio = 0

        elif passos_usuari == passos_necesaris:
            print ("Has guanyat!!")
            break

while True:
    pregunta = input ("\n Menú \n ------------------ \n 1. Jugar \n 2. Sortir \n\nQue vols fer? ")
    if pregunta == "1":
        joc(text)

    elif pregunta == "2":
        break