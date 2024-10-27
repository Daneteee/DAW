quant_num = int(input("Quants números introduiràs?"))
negatius = 0
 
for i in range(quant_num):
    num = int(input("Escriu el número: "))
 
    if num < 0:
        negatius = negatius + 1
print ("Hi han ", negatius, "nombres negatius.")