# 1. Crea un fitxer de text saluda.txt, en Python, 
# amb el contingut: "Bon dia CLASSE!!".  i tanca'l. 
# Obre el fitxer anterior, i afegeix-li les següents frases, 
# cadascuna en una línia diferent:

try:
    with open("saluda.txt", "w") as f:
        f.write("Bon dia CLASSE!!\n")
            
    with open("saluda.txt", "a") as fa:
        fa.write("Bona nit a tot@s !!!\n")
        fa.write("Buff no puc dormir, potser que compti xaiets")
            
except FileNotFoundError:
    print("No s'ha trobat el fitxer.")
