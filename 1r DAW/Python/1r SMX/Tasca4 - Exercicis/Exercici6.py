frase = input("Escriu una frase: ")
paraula = input("Escriu una paraula: ")

if paraula in frase:

	index = frase.split().index(paraula)

	print(paraula.capitalize(), "és la", str(index + 1)+"a", "paraula de", frase.capitalize())