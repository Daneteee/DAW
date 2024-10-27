# 3. Castiga a Python a escriure en un fitxer anomenat castiga.txt: 

def escriu_castig(string1, string2, n):
    """Afageix a la variable "castig" les strings pasades per paràmetre "n" vegades, alternant les strings.

    Args:
        string1 (string): Primera string.
        string2 (string): Segona string.
        n (int): nombre de cops que s'afegiràn les strings.

    Returns:
        string: El castig sencer amb totes les strings afegides
    """
    castig = ""
    
    for i in range(1, n):
        
        # Utilitzem un sistema binari per alternar entre strings
        if i % 2 != 0:
            # Afegim la string formatada (i. String)
            castig += f"{i}. {string1}\n"
        else:
            castig += f"{i}. {string2}\n"

    return castig

def main():
    try:
        with open("castiga.txt", "w") as f:
            f.write(escriu_castig("Faré totes les tasques de python perquè vull aprovar", "Faré totes les tasques de python perquè m’agrada programar", 1000))

    except FileNotFoundError:
        print("No s'ha trobat el fitxer.")

if __name__ == "__main__":
    main()