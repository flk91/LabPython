prezzo = float(input("Quanto costa il biglietto? "))
eta = int(input("Quanti anni ha lo spettatore? "))

if eta < 14 or eta >= 65:
    print("Il prezzo è ridotto del 10%")
    rid = round(prezzo - (prezzo/1.10), 2)
    prezzo = prezzo - rid
    print("La riduzione è di € " + str(rid))
    print("Il prezzo finale è di € " + str(prezzo))
else:
    print("Prezzo pieno, € " + str(prezzo))

input("Premere un tasto per uscire...")