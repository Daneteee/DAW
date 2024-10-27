# 4. Modifica els 3 programes anteriors usant la comanda with i no fent servir la comanda close. Posa tot el codi en un sol programa.

try:
    with open("text.txt", "w") as f:
        f.write("Hola\nBon\nDia")

    with open("text.txt", "r") as f:
        for linia in f:
            print(linia, end="")

    with open("text.txt", "a") as f:
        f.write("\ni\nbona\nhora")
        
    with open("text.txt", "r") as f:
        for linia in f:
            print(linia, end="")

except FileNotFoundError:
    print("No s'ha trobat el fitxer.")
