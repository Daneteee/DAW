# 5. Fes un programa que llegeixi del fitxer text2.txt i del fitxer text3.txt i escrigui en un 
# fitxer nou de nom text7.txt alternadament línies d'un fitxer i de l'altre 
# (compte: els 2 fitxers poden no tenir el mateix nombre de línies i per tant un acabarà abans que l'altre).
# Mostra en el mateix programa el contingut del fitxer text7.txt 
# (l'hauràs de tornar a obrir ara en mode lectura). 

try:
    with open("text2.txt", "r") as f2, open("text3.txt", "r") as f3, open("text7.txt", "w") as f7:
        linies_f2, linies_f3 = f2.readlines(), f3.readlines()

        len_max = max(len(linies_f2), len(linies_f3))

        for i in range(len_max):
            if i < len(linies_f2):
                f7.write(linies_f2[i])

            if i < len(linies_f3):
                f7.write(linies_f3[i])
        
    with open("text7.txt", "r") as f7read:
        for linia in f7read:
            print(linia, end="")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")