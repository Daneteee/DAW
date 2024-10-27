
#-------------------------------------------------------------------

def afegirCategories(categories, categoria):
    categoria = input ("Posa una categoria a afegir: ")
    categories[categoria] = {}
    return categories

#-------------------------------------------------------------------

def afegirProductes(producte):
    categoria = input("Indica a quina categoria pertanyen: ")
    while True:
        producte = input("Posa el producte (Surt amb '!'): ")
        if producte=="!":
            break
        else:
            categories[categoria] = {producte:0}

    return categories

#-------------------------------------------------------------------

def afegirPreu(categories):
    categoria = input("Indica a quina categoria pertanyen: ")
    producte = input("Quin producte és?: ")
    preu = int(input("Quin preu té?: "))

    categories[categoria][producte] = preu

    return categories

#-------------------------------------------------------------------

def mostrarProductesPreu(categories):
    for categoria in categories.keys():
        print (mostrar)

    
#-------------------------------------------------------------------

categories = {}
categoria = {}
productes = {}
producte = {}
preu = 0

#-------------------------------------------------------------------

while True:
    pregunta = input ("\n Menú \n ------------------ \n 1. Afegir categories \n 2. Afegir productes \n 3. Afegir preus als productes \n 4. Mostrar productes i preus \n 5. Calcular preu d'una comanda \n 6. Sortir \n Que vols fer?: ")
    if pregunta == "1":
        categories = afegirCategories(categories, categoria)
        print(categories)


    elif pregunta == "2":
        productes = afegirProductes(categories)
        print(productes)

    
    elif pregunta == "3":
        preu = afegirPreu(categories)
        print(preu)
        

    elif pregunta == "4":
        mostrar = mostrarProductesPreu(producte)


    elif pregunta == "6":
        break

#-------------------------------------------------------------------