# Importació de classes des de mòduls
from beguda import Beguda
from cafetera import Cafetera
from moneder import Moneder
from menu import Menu


# Definició de la funció principal
def main():
    # Creació d'objectes de begudes
    cafe_sol = Beguda(nom='Expresso', aigua=100, llet=0, cafe=10, preu=1.5)
    tallat = Beguda(nom='Tallat', aigua=100, llet=0, cafe=10, preu=1.5)
    cafe_amb_llet = Beguda(nom='Café amb llet', aigua=250, llet=250, cafe=25, preu=2.20)

    # Inicialització d'instàncies de classes
    menu = Menu([cafe_sol, cafe_amb_llet, tallat])
    moneder = Moneder()
    cafetera = Cafetera(aigua=500, llet=500, cafe=500)

    is_on = True

    # Bucle principal
    while is_on:
        print(menu)
        tria = input(f"Opcions: \noff = Parar \nafegir = Afegir recurs \nreport = Informe \ncaixa = Fer caixa \n\nQuina beguda vols? ")

        # Lògica de selecció d'opcions
        if tria == 'off':
            is_on = False

        elif tria == 'report':
            print(cafetera)
            print(moneder)

        elif tria == 'afegir':
            recurs = input("Quin recurs vols afegir (llet/aigua/cafe)? ")
            if recurs in cafetera.stock:
                cafetera.afegir_recurs(recurs=recurs, quantitat=500)

        elif tria == 'caixa':
            moneder.fer_caixa()
        else:
            beguda = menu.troba_beguda(tria.lower())

            if bool(beguda):
                if cafetera.hi_ha_recursos(beguda) and moneder.fer_pagament(beguda.preu):
                    cafetera.fer_beguda(beguda)


# Verificació de l'execució com a programa principal
if __name__ == "__main__":
    main()