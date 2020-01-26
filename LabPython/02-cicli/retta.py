m=int(input("Digita il valore di m: "))
q=int(input("Digita il valore di q: "))

print("x\ty")
for x in range (-10, 10):
    y=m*x+q
    print(x, "\t", y)
input("Premere invio per uscire")