# ULTIMATE SHERIFF és un joc de velocitat en qual el Sheriff ha d'eliminar als Bandits!
# Autor: Dan Maldonado
# Data de creació: 02/05/2023   

# Llibreries necessaries
import os
import sys
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


# NECESSARI "PIP INSTALL PILLOW"

# Moviment del bandit d'adalt
def SpawnBanditUp():
    global CreateBanditUp, vides, afterBandit
    if CreateBanditUp is not None and Dead is False:
        canvas.move(CreateBanditUp, 0, 5)
        if canvas.coords(CreateBanditUp)[1] > 250:
            canvas.coords(CreateBanditUp, 300, -100)
        elif canvas.coords(CreateBanditUp) == canvas.coords(SpawnSheriff):
            # Restar vides si impacta amb el Sheriff
            vides -= 1
            Salut()
            if vides == 0:
                GameOver()
        else:
            enemics.append(CreateBanditUp)
    else:
        CreateBanditUp = canvas.create_image(300, -100, image=BanditUp)
    afterBandit = root.after(SpeedBandit, SpawnBanditUp)


# Moviment del bandit d'abaix
def SpawnBanditDown():
    global CreateBanditDown, vides, afterBandit
    if CreateBanditDown is not None and Dead is False:
        canvas.move(CreateBanditDown, 0, -5)
        if canvas.coords(CreateBanditDown)[1] < 250:
            canvas.coords(CreateBanditDown, 300, 530)
        elif canvas.coords(CreateBanditDown) == canvas.coords(SpawnSheriff):
            vides -= 1
            Salut()
            if vides == 0:
                GameOver()
        else:
            enemics.append(CreateBanditDown)
    else:
        CreateBanditDown = canvas.create_image(300, 530, image=BanditDown)
    afterBandit = root.after(SpeedBandit, SpawnBanditDown)


# Moviment del bandit de l'esquerra
def SpawnBanditLeft():
    global CreateBanditLeft, vides, afterBandit
    if CreateBanditLeft is not None and Dead is False:
        canvas.move(CreateBanditLeft, 5, 0)
        if canvas.coords(CreateBanditLeft)[0] > 300:
            canvas.coords(CreateBanditLeft, -100, 250)
        elif canvas.coords(CreateBanditLeft) == canvas.coords(SpawnSheriff):
            vides -= 1
            Salut()
            if vides == 0:
                GameOver()
        else:
            enemics.append(CreateBanditLeft)
    else:
        CreateBanditLeft = canvas.create_image(-100, 250, image=BanditLeft)
    afterBandit = root.after(SpeedBandit, SpawnBanditLeft)


# Moviment del bandit de la dreta
def SpawnBanditRight():
    global CreateBanditRight, vides, afterBandit
    if CreateBanditRight is not None and Dead is False:
        canvas.move(CreateBanditRight, -5, 0)
        if canvas.coords(CreateBanditRight)[0] < 300:
            canvas.coords(CreateBanditRight, 625, 250)
        elif canvas.coords(CreateBanditRight) == canvas.coords(SpawnSheriff):
            vides -= 1
            Salut()
            if vides == 0:
                GameOver()
        else:
            enemics.append(CreateBanditRight)
    else:
        CreateBanditRight = canvas.create_image(625, 250, image=BanditRight)
    afterBandit = root.after(SpeedBandit, SpawnBanditRight)


# Eliminar vides del canvas a mesura que baixen
def Salut():
    global vides
    if vides == 2:
        canvas.delete(Vida3)
    elif vides == 1:
        canvas.delete(Vida2)
    elif vides == 0:
        canvas.delete(Vida1)

    # Vincular moviment del Sheriff amb eliminació d'enemics


def tot(event):
    if not Dead:
        moviment(event)
        onKeyPress(event)


# Moviment del Sheriff
def moviment(event):
    global Sheriff
    global SpawnSheriff

    # Rotem la imatge quan es presiona la tecla corresponent
    if event.keysym == "Up":
        canvas.delete(SpawnSheriff)
        Sheriff = ImageTk.PhotoImage(Imatge.rotate(0))
        SpawnSheriff = canvas.create_image(window_width / 2, window_height / 2, image=Sheriff)

    elif event.keysym == "Down":
        canvas.delete(SpawnSheriff)
        Sheriff = ImageTk.PhotoImage(Imatge.rotate(180))
        SpawnSheriff = canvas.create_image(window_width / 2, window_height / 2, image=Sheriff)


    elif event.keysym == "Left":
        canvas.delete(SpawnSheriff)
        Sheriff = ImageTk.PhotoImage(Imatge.rotate(90))
        SpawnSheriff = canvas.create_image(window_width / 2, window_height / 2, image=Sheriff)

    elif event.keysym == "Right":
        canvas.delete(SpawnSheriff)
        Sheriff = ImageTk.PhotoImage(Imatge.rotate(-90))
        SpawnSheriff = canvas.create_image(window_width / 2, window_height / 2, image=Sheriff)


# Eliminació de Bandits i puntuació
def onKeyPress(event):
    global CreateBanditUp, CreateBanditDown, CreateBanditLeft, CreateBanditRight, punts, SpeedBandit

    # Assignem l'eliminació de cada bandit a una tecla
    if event.keysym == "Up" and CreateBanditUp is not None:
        canvas.delete(CreateBanditUp)
        CreateBanditUp = None
        # Afegim puntuació al eliminar
        punts += 10
        if len(str(punts)) >= 2 and str(punts)[-2] == '0':
            SpeedBandit -= 3
        canvas.itemconfigure(puntsMostrats, text=punts)

    elif event.keysym == "Down" and CreateBanditDown is not None:
        canvas.delete(CreateBanditDown)
        CreateBanditDown = None
        punts += 10
        if len(str(punts)) >= 2 and str(punts)[-2] == '0':
            SpeedBandit -= 3
        canvas.itemconfigure(puntsMostrats, text=punts)

    elif event.keysym == "Left" and CreateBanditLeft is not None:
        canvas.delete(CreateBanditLeft)
        CreateBanditLeft = None
        punts += 10
        if len(str(punts)) >= 2 and str(punts)[-2] == '0':
            SpeedBandit -= 3
        canvas.itemconfigure(puntsMostrats, text=punts)

    elif event.keysym == "Right" and CreateBanditRight is not None:
        canvas.delete(CreateBanditRight)
        CreateBanditRight = None
        punts += 10
        if len(str(punts)) >= 2 and str(punts)[-2] == '0':
            SpeedBandit -= 3
        canvas.itemconfigure(puntsMostrats, text=punts)

    # Pantalla que apareixerà quan les vides arribin a 0


def GameOver():
    global punts, Nom, board, Dead

    Dead = True
    # Assignem la funció per començar el joc a la tecla "Enter"
    root.bind("<Return>", lambda event: restart_game())

    # Elements bàsics de GameOver
    canvas.delete("all")
    canvas.create_text(300, 150, text="Game Over", fill="red", font=("Amiga", 60))
    canvas.create_rectangle(400, 480, 580, 230)
    canvas.create_text(300, 380, text="... or press enter", font=("Helvetica", 10))

    # Reiniciar el joc
    restart_button = tk.Button(root, text="Restart Game", command=restart_game)
    canvas.create_window(300, 350, window=restart_button)
    canvas.create_text(300, 380, text="... or press enter", font=("Helvetica", 10))

    # Text LeaderBoard
    canvas.create_text(490, 220, text="WANTED", font=("cmsy10", 13))
    canvas.create_text(435, 390, text="Name:", font=("Helvetica", 10))

    # Nom del jugador
    Nom = tk.Entry(canvas)
    canvas.create_window(490, 410, window=Nom)

    # Punts
    canvas.create_text(300, 250, text="Points:", font=("Helvetica", 11))
    canvas.create_text(300, 270, text=punts, font=("Helvetica", 13))

    # Guardar puntuació 
    saveScore = tk.Button(root, text="Save", command=LeaderBoard)
    canvas.create_window(450, 450, window=saveScore)
    board = Text(root, width=20, height=7)
    canvas.create_window(490, 305, window=board)
    actualizarPunts()

    # No guardar dades i reiniciar
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    canvas.create_window(530, 450, window=exit_button)


# Afegeix el Nom del jugador i la puntuació a LeaderBoard
def LeaderBoard():
    with open("LeaderBoard.txt", "a") as arxiuPunts:
        afegirNom = Nom.get() + " - " + str(punts) + "\n"
        arxiuPunts.write(afegirNom)
    Nom.delete(0, END)
    actualizarPunts()


# Actualizar la LeaderBoard
def actualizarPunts():
    with open("LeaderBoard.txt", "r") as archivo:
        contenido = archivo.read().splitlines()
    contenido_ordenado = sorted(contenido, key=lambda x: int(x.split(" - ")[1]), reverse=True)
    contenido_final = "\n".join(contenido_ordenado)
    board.delete("1.0", END)
    board.insert(END, contenido_final)


# Reiniciar el programa
def restart_game():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Creació de la finestra
root = tk.Tk()
root.title('Ultimate Sheriff')
root.resizable(False, False)

# Mesures de la finestra
window_width = 600
window_height = 500

# Posicionem la finestra al centre de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Creem un Llenç
canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack(anchor=tk.CENTER, expand=True)

# Puntuació
canvas.create_rectangle(500, 10, 580, 50)
punts = 0
puntsMostrats = canvas.create_text(540, 29, text=punts)

# Definim que el jugador no hagi mort
Dead = False

# Imatge i creació del Sheriff
Imatge = Image.open("/home/dan/Documents/VSCode/Juegardo/DanMaldonado_UltimateSheriff/Multimedia/sheriff-up.png")
Sheriff = ImageTk.PhotoImage(Imatge.rotate(0))
SpawnSheriff = canvas.create_image(window_width / 2, window_height / 2, image=Sheriff)

# Imatge dels Bandits
ImatgeBandit = Image.open("/home/dan/Documents/VSCode/Juegardo/DanMaldonado_UltimateSheriff/Multimedia/bandit-up.png")
BanditUp = ImageTk.PhotoImage(ImatgeBandit.rotate(180))
BanditDown = ImageTk.PhotoImage(ImatgeBandit.rotate(0))
BanditLeft = ImageTk.PhotoImage(ImatgeBandit.rotate(-90))
BanditRight = ImageTk.PhotoImage(ImatgeBandit.rotate(90))

# Enemics actius
enemics = []

# Velocitat inicial dels enemics
SpeedBandit = 50

# Imatge del cor i creació de les 3 vides
ImatgeCor = Image.open("/home/dan/Documents/VSCode/Juegardo/DanMaldonado_UltimateSheriff/Multimedia/cor.png")
Cor = ImageTk.PhotoImage(ImatgeCor)
Vida1 = canvas.create_image(40, 35, image=Cor)
Vida2 = canvas.create_image(80, 35, image=Cor)
Vida3 = canvas.create_image(120, 35, image=Cor)
vides = 3

# Creació dels Bandits i cridem a les funcions de moviment
CreateBanditUp = canvas.create_image(300, -100, image=BanditUp)
SpawnBanditUp()
CreateBanditRight = canvas.create_image(300, -100, image=BanditRight)
SpawnBanditRight()
CreateBanditLeft = canvas.create_image(300, -100, image=BanditLeft)
SpawnBanditLeft()
CreateBanditDown = canvas.create_image(300, -100, image=BanditDown)
SpawnBanditDown()

# Assignem les tecles a les funcions corresponents
canvas.bind_all('<KeyPress-Up>', tot)
canvas.bind_all('<KeyPress-Down>', tot)
canvas.bind_all('<KeyPress-Left>', tot)
canvas.bind_all('<KeyPress-Right>', tot)

root.mainloop()
