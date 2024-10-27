def salari_calculs(sou_base,preuContracte):
    total = sou_base + preuContracte * 0.05
    return total 

sou_base = 1000
preuContracte = int(input("Diga'm de quant ha sigut la firma en €: "))


print("El sou que et queda és:",salari_calculs(sou_base,preuContracte),"€")