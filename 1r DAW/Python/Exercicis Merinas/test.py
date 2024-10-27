import mysql.connector as con

baseDades = con.connect(
    host = "10.42.130.120",
    user = "phpmyadmin",
    password = "123",
    database = "appPython"
)

cursor = baseDades.cursor()

comanda = "SELECT Nom, contrasenya FROM usuaris"
cursor.execute(comanda)
usuari = cursor.fetchall()

cursor.close()

for i in usuari:
    print ("\nNom:",i[0], "\nContrasenya:",i[1],"\n")
