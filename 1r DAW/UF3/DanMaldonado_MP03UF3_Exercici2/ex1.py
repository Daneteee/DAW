# 1. Fes un programa que llegeixi del fitxer text.txt i escrigui les línies parelles en 
# un fitxer nou de nom text3.txt. Mostra en el mateix programa el contingut del fitxer text3.txt 
# (l'hauràs de tornar a obrir ara en mode lectura).

try:
    with open("text.txt", "r") as f1, open("text3.txt", "w") as f3:
        i = 1
        for linia in f1:
            if i % 2 == 0:
                f3.write(linia)
            i += 1
            
    with open("text3.txt", "r") as f3read:
        for linia in f3read:
            print(linia, end="")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")