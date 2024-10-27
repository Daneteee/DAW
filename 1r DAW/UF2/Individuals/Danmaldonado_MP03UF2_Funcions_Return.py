# Fes un programa en Python amb un menú per fer la crida a cadascuna de les funcions. 
# Dan Maldonado - 3/12/2023

menu = ("Int Segur", "Comptar mayus. i minus.", "Calcular any de traspàs", "Comptar dies del mes", "Nombre perfecte", "Calculadora")

# Creem una funció per mostrar el menú
def print_menu(menu):
    '''Mostra les entrades de la tupla "menu" afegint el nombre
    corresponent i la entrada "SORTIR" al final.'''
    mida = len(menu)
    print("\nFuncions\n--------------------")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    print(f"{mida+1}. SORTIR")

# Funció per validar un enter
def introduir_int_segur(text, num1=None, num2=None):
    '''Utilitza el primer paràmetre de text com a el text de l’input, 
    un valor mínim i un valor màxim, i demana un input a l’usuari, 
    assegurant que és un sencer entre el valor mínim i el màxim, si 
    el mínim i el màxim no s’han definit no els té en compte.'''
    int_valid = False
    while not int_valid:
        if num1 is None and num2 is None:
            num_introduit = input(f"{text} enter: ")
        else:
            num_introduit = input(f"{text} entre {num1} i {num2}: ")

        if (num_introduit.startswith('-') and num_introduit[1:].isdigit()) or num_introduit.isdigit():
            num_introduit = int(num_introduit)
            int_valid = True
            if num1 is not None and num2 is not None and num_introduit not in range(num1, num2):
                int_valid = False
    return num_introduit

# Funció per comptar les majúscules i minúscules d'una cadena
def comptar_majuscules_minuscules(cadena):
    '''Accepta una cadena com a paràmetre i retorna el nombre de lletres 
    majúscules i minúscules.'''
    minus = sum(1 for i in cadena if i.islower())
    mayus = sum(1 for i in cadena if i.isupper())
    return (mayus, minus)

# Funció per calcular si un any és de traspàs o no
def calcular_any_traspas(sencer):
    '''Donat un any retorna si és un any de traspàs.'''
    traspas = sencer % 4 == 0 and sencer % 100 != 0 or sencer % 400 == 0
    return traspas

# Funció per comptar els dies d'un mes, tenint en compte si l'any és de traspàs o no
def comptar_dies_mes(mes, any_int):
    '''Donat un mes i un any, la funció retorna quants dies té el mes, 
    tenint en compte si l’any és de traspàs.'''
    dies = {1:31, 2:29 if calcular_any_traspas(any_int) else 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return dies[mes]

# Funció per comprovar si un número és perfecte o no
def comprovar_num_perfecte(num):
    '''Comprova si un número passat per paràmetre és perfecte.'''
    perfecte = sum([i for i in range(1, num + 1) if num % i == 0]) / 2 == num
    return perfecte 

# Funcions per la calculadora
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    '''Aquí si la divisió és entre zero retornem 0 i l'error'''
    if num1 == 0 or num2 == 0:
        print("ERROR: Divisió entre zero.")
        return 0
    else:
        return num1 / num2

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
            num = introduir_int_segur("Introdueix un nombre: ")
            print(num)
            
        elif opcio == "2":
            cadena = input("introdueix una cadena de text: ")
            print(comptar_majuscules_minuscules(cadena))
    
        elif opcio == "3":
            sencer = int(input("Introdueix un any: "))
            print(calcular_any_traspas(sencer))

        elif opcio == "4":
            mes = int(input("Introdueix un mes: "))
            any_int = int(input("Introdueix un any: "))
            print(comptar_dies_mes(mes, any_int))
        
        elif opcio == "5":
            num = int(input("Introdueix un enter: "))
            print(comprovar_num_perfecte(num))
            
        elif opcio == "6":
            num1 = introduir_int_segur("Introdueix el primer nombre")
            num2 = introduir_int_segur("Introdueix el segon nombre")
            operacions = {
                "+": sumar,
                "-": restar,
                "*": multiplicar,
                "/": dividir
            }
            
            for item in operacions:
                print(item)

            # Validem que el simbol sigui vàlid
            simbol_ok = False
            while not simbol_ok:
                simbol = input("Què vols fer? ") 
                if simbol in operacions:
                    # Fem la crida a les operacions i mostrem resultats
                    operacio = operacions[simbol]
                    resultat = operacio(num1, num2)
                    print(f"{num1} {simbol} {num2} = {resultat}")
                    simbol_ok = True
                else:
                    print("ERROR: Operació no vàlida.")
                
            calc_sortir = False
            while not calc_sortir:
                eleccio = input(f"Vols continuar amb {resultat}? (S/N)")
                if eleccio in "Ss":
                    num1 = resultat
                    simbol_ok = False
                    while not simbol_ok:
                        simbol = input("Què vols fer? ") 
                        if simbol in operacions:
                            operacio = operacions[simbol]
                            resultat = operacio(num1, num2)
                            print(f"{num1} {simbol} {num2} = {resultat}")
                            simbol_ok = True
                        else:
                            print("ERROR: Operació no vàlida.")
                    num2 = introduir_int_segur("Introdueix el següent nombre")
                    operacio = operacions[simbol]
                    resultat = operacio(num1, num2)
                    print(f"{num1} {simbol} {num2} = {resultat}")

                
                elif eleccio in "Nn":
                    calc_sortir = True
                    
                else:
                    print("ERROR: Valor incorrecte.")
            

        elif opcio == "7":
            sortir = True
    
if __name__ == "__main__":
    main()