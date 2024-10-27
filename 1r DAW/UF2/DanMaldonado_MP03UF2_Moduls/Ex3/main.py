from llistes import *

def main():
    n = int( input('Quants elements? ') )
    w = []
    v = demana_llista(n)
    imprimeix_llista(v)
    omple_llista(w, n, -10, 10)
    imprimeix_llista(w)
    v = suma_llistes(v, w)
    imprimeix_llista(v)


    ordena_llista(v)
    imprimeix_llista(v)


if __name__ == "__main__":
    		main()
