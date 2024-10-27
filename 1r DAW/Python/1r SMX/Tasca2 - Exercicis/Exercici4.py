num = 1
total = 0 

while num != 0:
	num = int(input("Entra un nombre: "))

	if num in range (1,10):
		total = total + num

	elif num == 0:
		print("La suma és", total)

	else:
		print("Error")
