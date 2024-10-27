# 2. Donada la primera estrofa de "The fly song": 

# Una mosca volava per la llum
# i la llum es va apagar
# i la pobre mosca va quedar a les fosques
# i la pobre mosca no va poder volar. 

# Crea un programa que escriu el fitxer the_fly_song.txt:

# Per crear la cançó cal escriure la primera estrofa.
# La segona estrofa és igual a la primera estrofa, però canviant les vocals per a. 
# La tercera estrofa és igual a la primera estrofa, però canviant les vocals per e, ...etc...

PRIMERA_ESTROFA = """
Una mosca volava per la llum
i la llum es va apagar
i la pobre mosca va quedar a les fosques
i la pobre mosca no va poder volar. 
                """

CANCO = []

vocals = "aeiou"

def retorna_substitucio(string, vocal):
    """Retornem una nova string basada en la string pasada per paràmetre amb les 
    vocals canviades per la vocal que es rep per paràmetre 

    Args:
        string (string): La string a la qual es canviarán les vocals.
        vocal (string): Vocal la qual utilitzarà per canviar la resta de vocals.

    Returns:
        string: Retorna la nova string amb les vocals canviades.
    """
    nova_string = ""
    
    for lletra in string:
        if lletra in vocals:
            nova_string += vocal
            
        elif lletra in vocals.upper():
            nova_string += vocal.upper()
        
        else:
            nova_string += lletra
            
    return nova_string

def main():    
    try:
        with open("the_fly_song.txt", "a") as f:
            f.write(PRIMERA_ESTROFA)
            for vocal in vocals:
                f.write(retorna_substitucio(PRIMERA_ESTROFA, vocal))
        
    except FileNotFoundError:
        print("No s'ha trobat el fitxer.")
        
if __name__ == "__main__":
    main()