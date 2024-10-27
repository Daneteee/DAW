string = input(("Escriu una frase: "))
vocals = ["a", "e", "i", "o", "u"]

for i in string:
	if i in vocals:
		print (i)