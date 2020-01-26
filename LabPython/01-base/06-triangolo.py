l1 = float(input("Inserire lunghezza primo lato: "))
l2 = float(input("Inserire lunghezza secondo lato: "))
l3 = float(input("Inserire lunghezza terzo lato: "))

if l1 != l2 and l2 != l3:
    print("Il triangolo è SCALENO\n")
elif l1 == l2 and l2 == l3:
    print("Il triangolo è EQUILATERO\n")
else:
    print("Il triangolo è ISOSCELE")

input("Premere un tasto per uscire...")