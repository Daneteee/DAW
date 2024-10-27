quant_num = int(input("Quants números introduiràs? "))
primer_num = int(input("Escriu el primer número: ")) 

for i in range(quant_num - 1): 
    num = int(input("Escriu el número: "))

    if num < primer_num:
        print(num,"és més petit que", primer_num)