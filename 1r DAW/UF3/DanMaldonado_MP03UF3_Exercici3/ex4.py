# 4. Crea un fitxer de text abece.txt amb el contingut: 

abcdari = "abcdefghijklmnopqrstuvwxyz"

def crear_piramide(lletra, n):
    """Retornem una piramide de les lletres del abecedari en cada nivell.

    Args:
        lletra (string): La lletra per la qual es començarà. 
        n (int): Nombre de salts que donarà el chr().

    Returns:
        string: Retorna la piramide en string. 
    """
    piramide = ""
    
    for i in range(1, n+1): 
        # Afegeix la lletra a la piramide multiplicada pel nombre de cops que s'ha iterat afegint un salt de línia.
        piramide += lletra * i + "\n"
        lletra = chr(ord(lletra) + 1)

    return piramide

def main():
    try:
        with open("abece.txt", "w") as f:
            f.write(crear_piramide("a", len(abcdari)))

    except FileNotFoundError:
        print("No s'ha trobat el fitxer.")

if __name__ == "__main__":
    main()
