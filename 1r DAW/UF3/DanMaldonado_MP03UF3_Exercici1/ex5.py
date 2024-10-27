# 5. Fes un programa que llegeix del fitxer "text.txt" i escriu el contingut en un fitxer nou de nom "text2.txt". 
# Mostra en el mateix programa el contingut del fitxer "text2.txt" (l'hauràs de tornar a obrir ara en mode lectura).

try:
    with open("text.txt", "r") as f1, open("text2.txt", "w") as f2:
        for linia in f1:
            print(linia, end="")
            f2.write(linia)
    
    with open("text2.txt", "r") as f2read: 
        for linia in f2read:
            print(linia, end="")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")

