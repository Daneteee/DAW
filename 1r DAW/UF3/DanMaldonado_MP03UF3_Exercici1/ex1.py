# 1. Fes un programa que crea un fitxer de text de nom "text.txt" i escriu tres línies de text al fitxer. 
# Fes-lo usant les comandes open i close. Comprova que s'ha creat amb un editor de text, així sabràs on els guarda.

try:
    f = open("text.txt", "w")
    f.write("Hola\nBon\nDia")
    f.close()
    
except:
    print("No s'ha pogut crear.")

