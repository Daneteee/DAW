from random import *

def omple_llista(llista,longitud,min,max):
    for i in range(longitud):
        llista.append(randint(min,max))

def demana_llista(n):
    ll = [input("Introdueix nombre: ") for i in range(n)]
    return ll

def imprimeix_llista(ll):
    print(*ll)

def ordena_llista(ll):
    ll = ll.sort()
    
def suma_llistes(ll1, ll2):    
    if len(ll1) == len(ll2):
        for i in range(len(ll1)):
            suma.append(int(ll1[i])+int(ll2[i]))
    else:
        print("ERROR: No tenen la mateixa longitud.")
    return suma