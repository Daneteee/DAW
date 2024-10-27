def ponderacio(valors,percentatge):
    totalTasques=valors * percentatge
    
    return totalTasques

tasca1 = int(input("Nota de la tasca 1: "))
tasca2 = int(input("Nota de la tasca 2: "))
tasca3 = int(input("Nota de la tasca 3: "))
tasca4 = int(input("Nota de la tasca 4: "))
totalTasques = (tasca1 + tasca2 + tasca3 + tasca4) * 0.05
ponderacio([tasca1,tasca2,tasca3,tasca4],0.05)

treball1 = int(input("Nota del treball 1:"))
treball2 = int(input("Nota del treball 2:"))
totalTreballs = (treball1 + treball2) * 0.15

examen = int(input("Nota del exàmen: "))
totalExamen = examen * 0.50

notaTotal = totalExamen + totalTasques + totalTreballs

if notaTotal < 5:
    print("\nHas suspés...", "\n\nNota de les tasques:", totalTasques, "\nNota dels treballs:", totalTreballs, "\nNota dels examens:", totalExamen, "\nLa nota final és de:", notaTotal)

elif notaTotal >= 5:
    print("\nHas aprobat!", "\n\nNota de les tasques:", totalTasques, "\nNota dels treballs:", totalTreballs, "\nNota dels examens:", totalExamen, "\nLa nota final és de:", notaTotal)

if totalTasques + totalTreballs < 2.5:
    print("\nHas suspés...", "\n\nNota de les tasques:", totalTasques, "\nNota dels treballs:", totalTreballs, "\nNota dels examens:", totalExamen, "\nLa nota final és de:", notaTotal)

if examen < 2.5:
    print("\nHas suspés...", "\n\nNota de les tasques:", totalTasques, "\nNota dels treballs:", totalTreballs, "\nNota dels examens:", totalExamen, "\nLa nota final és de:", notaTotal)
