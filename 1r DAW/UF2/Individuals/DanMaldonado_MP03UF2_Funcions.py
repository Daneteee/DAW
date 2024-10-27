# Fes un programa en Python amb un menú per fer la crida a cadascuna de les següents funcions. 
# Cap de les funcions té return. El programa serà amb estructura main.
# Dan Maldonado - 3/12/2023

menu = ("Multiplica", "Anys 2000", "Gira del revés", "Triangle de pascal")

# Creem una funció per mostrar el menú
def print_menu(menu):
    '''Mostra les entrades de la tupla "menu" afegint el nombre
    corresponent i la entrada "SORTIR" al final.'''
    mida = len(menu)
    print("\nFuncions\n--------------------")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    print(f"{mida+1}. SORTIR")

# Funció de multiplicació
def multiplica(num1,num2):
    '''Imprimeix el resultat de multiplicar dos números passats 
    com a paràmetres, els inputs es fan a fora de la funció.'''
    print(num1 * num2)

# Funció per calcular l'any "X" fins a l'actual
def anys_2000():
    '''Primer verifiquem que l'any sigui vàlid y després
    mostrem quant ha passat.'''
    any_valid = False
    while not any_valid:
        any_actual = input("Introdueix l'any: ")
        if any_actual.isdigit():
            any_actual = int(any_actual)
            if any_actual in range(2000,2023 + 1):
                any_valid = True
    
    print(f"Desde del {any_actual} han passat {2023 - any_actual} anys.")
    
# Funció per girar una cadena
def gira_reves():
    '''Introduim la cadena i la imprimim de dreta a esquerra.'''
    cadena = input("Introdueix una cadena per girar-la: ")
    print(cadena[::-1])

# Funció per crear el triangle de pascal
def triangle_pascal():
    '''Verifica que el nombre sigui vàlid, mostra el triangle
    de pascal i fica espais entre els digits per centrar-lo
    depenent de la longitud més gran dels digits i de l'altura
    introduida'''
    triangle = [[1]]
    n = ""

    while n not in map(str, range(2, 11)):
        n = input("Introduce un número del 2 al 10: ")
    n = int(n)

    for i in range(1, n):
        fila = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
        triangle.append(fila)

    c = len(triangle) 

    max_fila = max(len(str(element)) for fila in triangle for element in fila)

    for fila in triangle:
        if n < 6:
            print(" " * c, " ".join(f"{' ' * (max_fila - len(str(element)))}{element}" for element in fila))
            c -= 1

        elif n < 10:
            print("  " * c, "  ".join(f"{' ' * (max_fila - len(str(element)))}{element}" for element in fila))
            c -= 1

        else:
            print("  " * c, " ".join(f"{' ' * (max_fila - len(str(element)))}{element}" for element in fila))
            c -= 1

# Funció principal
def main():
    '''Anem demanant que vol fer l'usuari i
    depenent la resposta inicialitzem una funció
    o un altre.'''
    sortir = False
    while not sortir:
        print_menu(menu)
        opcio = input("\nQue vols fer? ")
        
        if opcio == "1":
            num1 = int(input("Introdueix el primer nombre: "))
            num2 = int(input("Introdueix el segon nombre: "))
            multiplica(num1,num2)

        elif opcio == "2":
            anys_2000()
    
        elif opcio == "3":
            gira_reves()
            
        elif opcio == "4":
            triangle_pascal()
        
        elif opcio == "5":
            sortir = True
    
if __name__ == "__main__":
    main()