string = input("Escriu una frase: ").split()
 
for i in string:
    paraula = max(string, key=len)
   
print(paraula)