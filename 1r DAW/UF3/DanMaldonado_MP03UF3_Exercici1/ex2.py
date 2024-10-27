# 2. Fes un programa que llegeix el fitxer de text "text.txt" anterior i el mostra per pantalla. 
# Fes-lo usant les comandes open i close.

try:
    f = open("text.txt", "r")
    for linia in f:
        print(linia, end="")
    f.close()
    
except FileNotFoundError:
    print("El fitxer no existeix.")
