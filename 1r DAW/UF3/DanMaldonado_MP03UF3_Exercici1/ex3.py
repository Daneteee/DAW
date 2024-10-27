# 3. Fes un programa que afegeix una línia més al fitxer de text "text.txt" i el mostra per pantalla. 
# Fes-lo usant les comandes open i close. Per poder afegir al fitxer cal obrir-lo en mode append i 
# després per mostrar-lo cal tornar-lo a obrir en mode read.

try:
    f = open("text.txt", "a")
    f.write("\ni\nbona\nhora")
    f.close()
    
    f = open("text.txt", "r")
    for linia in f:
        print(linia, end="")
        
    f.close()

except FileNotFoundError:
    print("No s'ha trobat el fitxer.")