# Exercici 1: El problema és que volem girar una llista T[] en complexitat de temps lineal O(N) i volem que l'algorisme
# també estigui al seu lloc, de manera que no es pot utilitzar cap variable auxiliar ni cap mètode de llistes
# Per exemple: l'entrada és [1,2,3,4,5] i la sortida és [5,4,3,2,1]
def swap(swap_list):
    for i in range(len(swap_list) // 2):
        swap_list[i], swap_list[-i - 1] = swap_list[-i - 1], swap_list[i]
    return swap_list


# Ex2: "Un palíndrom és una cadena que llegeix el mateix cap endavant i cap enrere". La nostra tasca és dissenyar un
# algorisme òptim per comprovar si una cadena és palíndrom o no. Podeu fer servir la funció feta anteriorment
def is_palindrome(string):
    # Com a la funció swap retorna una llista, cal transformar aquesta llista a string
    return string == "".join(swap([i for i in string]))


# Ex3: Girar un sencer. No es pot fer servir canvi de tipus, cal fer servir l’operació mòdul i la divisió sencera
def swap_int(num):
    swapped_int = 0
    while num != 0:
        residue = num % 10
        num = num // 10
        swapped_int = swapped_int * 10 + residue
    return swapped_int


# Ex4: Fes un algorisme per comprovar si dues paraules (o frases) són anagrames o no! "Un anagrama és una paraula o
# frase formada reordenant les lletres d'una paraula o frase diferent, normalment utilitzant totes les lletres originals
# exactament una vegada". Suposa que cada lletra (o paraula) és un element d’una llista. Ordena les llistes per
# comparar-les. Exemple anagrama: roma - amor
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)



# Exercici 5: El problema és que volem ordenar una matriu unidimensional de nombres enters T[] en temps d'execució O(N)
# i sense cap memòria addicional. La matriu pot contenir valors: 0, 1 i 2
# (consulteu la secció teòrica per a més informació).
def dutch_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


"""
Comença a llegir la array i si no troba un 0 o un 1 a la primera posició, intercanvia la primera posició amb la última.
I com la última posició ja ha estat canviada, resta 1 a la llargada de la array. En cas que trobi 0 intercanvia una 
posició X per una posició X+1 i suma 1 als punters low i mid. Si troba un 1 suma 1 al punter mid, per passar al
següent element de la array. I així fins que acaba tot ordenat de 0 a 2.
"""


# Ex6: El problema d’emmagatzemar aigua
def store_water(array):
    water_blocks = 0

    if len(array) >= 3:
        for block in range(1, len(array) - 1):

            # Contem el bloc més alt de l'esquerra
            max_left = array[block]
            for j in range(block):
                max_left = max(max_left, array[j])

            # Contem el bloc més alt de la dreta
            max_right = array[block]
            for j in range(block + 1, len(array)):
                max_right = max(max_right, array[j])

            water = min(max_left, max_right) - array[block]

            if water > 0:
                water_blocks += water

    return water_blocks
