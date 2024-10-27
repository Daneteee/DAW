while 0==0:
	num = int(input("Entra un nombre: "))

	print("\n" "Mostrant la taula del", num, "\n------------------------------------")
	for taula in range(1,11):

		print(taula * num)
	
	sortir = input("Desitja sortir (S/N)? ")
	
	if sortir == "S":
		print("Sortint...")
		break
	elif sortir == "N":
		print("No surts")
	else:
		print("Error, tornant a intentar...")