# Fes un programa que llegeixi del fitxer text2.txt i escrigui en un fitxer nou de nom text6.txt 
# només les línies parelles. Després llegeixi del fitxer text3.txt i escrigui a continuació en el 
# fitxer text6.txt només les línies senars. Mostra en el mateix programa el contingut del fitxer text6.txt
# (l'hauràs de tornar a obrir ara en mode lectura).

try:
    with open("text2.txt", "r") as f2, open("text6.txt", "w") as f6, open("text3.txt", "r") as f3:
        i = 1
        for linia in f2:
            if i % 2 == 0:
                f6.write(linia)
            i += 1
            
        i = 0
        for linia in f3:
            if i % 2 == 0:
                f6.write(linia)
            i += 1

    with open("text6.txt", "r") as f6read:
        for linia in f6read:
            print(linia, end="")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")