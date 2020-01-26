import caricamento

#in python non esiste il do-while
elem=0
while elem<1:
    elem = int(input("Quanti elementi vuoi caricare? "))
    miovet = caricamento.carica_rand(elem)


print(miovet)

input("Premere invio per uscire...")