# preso in input un numero, compreso tra 1 e 7,
# fornire la sua rappresentazione in sistema binario.

num = input("Digita un numero compreso tra 0 e 7\n")
num = int(num)

if num>=0 and num<=7 :
    d = num
    r1 = d % 2
    d = d // 2 # l'operatore // è la divisione intera
    r2 = d % 2
    d = d // 2
    r3 = d%2
    d = d//2

    nbin = str(r3)+ str(r2)+str(r1)
    print("La rappresentazione binaria del numero è: " + nbin)
else:
    print("Il numero inserito non è valido")

input("Premere un tasto per uscire...")
