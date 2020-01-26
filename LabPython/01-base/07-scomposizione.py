#leggo in input il numero
num=input("Digita un numero: ")

#num ora è una stringa. Posso determinare la sua lunghezza
#per sapere di quante cifre è il numero
cifre = len(num)

print("Il numero è composto da", str(cifre), "cifre:\n")

#converto il numero in int
num=int(num)

multipli = ("unità", "decine", "centinaia", "migliaia", "decine di migliaia", "centinaia di migliaia", "milioni", "decine di milioni", "centinaia di milioni", "miliardi")

for i in range(1, cifre+1):
    p = 10**i
    q = num % p
    num = num-q
    print(str(int(q/p*10)), multipli[i-1])


input("\nPremere invio per uscire...")
