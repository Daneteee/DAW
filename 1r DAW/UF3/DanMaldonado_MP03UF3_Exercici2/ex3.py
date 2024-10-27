# 3. Fes un programa que llegeixi del fitxer text2.txt i l'escrigui en un fitxer nou de nom text5.txt.
# Després que llegeixi del fitxer text3.txt i l'escrigui a continuació en el fitxer text5.txt 
# (hi haurà tot el contingut del fitxer text2.txt i després tot el contingut del fitxer text3.txt). 
# Mostra en el mateix programa el contingut del fitxer text5.txt 
# (l'hauràs de tornar a obrir ara en mode lectura).

try:
    with open("text2.txt", "r") as f2, open("text5.txt", "w") as f5, open("text3.txt", "r") as f3:
        for linia in f2:
            f5.write(linia)            

        for linia in f3:
            f5.write(linia)


    with open("text5.txt", "r") as f5read:
        for linia in f5read:
            print(linia, end="")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")