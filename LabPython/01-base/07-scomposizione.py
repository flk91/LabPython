#leggo in input il numero
num=input("Digita un numero: ")

#num ora è una stringa. Posso determinare la sua lunghezza
#per sapere di quante cifre è il numero
cifre = len(num)

print(str(cifre), "cifre")

#converto il numero in int
num=int(num)

multipli = ("unità", "decine", "centinaia", "migliaia", "milioni")

for i in range(1, cifre+1):
    p = 10**i
    q = num % p
    num = num-q
    print(str(int(q/p*10)), multipli[i-1])


input("Premere invio per uscire...")
