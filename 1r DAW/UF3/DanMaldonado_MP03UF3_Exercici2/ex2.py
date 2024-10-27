# 2. Fes un programa que llegeixi del fitxer text.txt, afegeixi un punt al final de totes les línies 
# d’aquest fitxer i les escrigui en un fitxer nou de nom text4.txt. Mostra en el mateix programa 
# el contingut del fitxer text4.txt (l'hauràs de tornar a obrir ara en mode lectura).

try:
    with open("text.txt", "r") as f1, open("text4.txt", "a") as f4:
        for linia in f1:
            linia_modificada = linia.rstrip() + ".\n"
            f4.write(linia_modificada)

            
    with open("text4.txt", "r") as f4read:
        for linia in f4read:
            print(linia, end="")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")