string = input(("Escriu una frase: "))
vocals = ["a", "e", "i", "o", "u"]
num_vocals = 0

for i in string:
	if i in vocals:
		num_vocals = num_vocals + 1
print(num_vocals)