quant_num = int(input("Quants números introduiràs? "))
 
parells = 0
senars = 0
 
for i in range(quant_num):
    num = int(input("Escriu el número: "))
 
    if num % 2 == 0:
        parells = parells + 1
    
    elif num % 2 != 0:
        senars = senars + 1 

print ("Hi han ", parells, "parells" "\nHi han", senars, "senars")