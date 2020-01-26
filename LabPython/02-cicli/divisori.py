num = input("Digita il numero di cui vuoi trovare i divisori: ")

num = int(num)

primo = True #True e False vanno scritti con iniziale maiuscola

for i in range(1, num+1):
    if num%i==0:
        if i!=1 and i!=num:
            primo=False
        print(str(i) + " è un divisore di " + str(num))

if primo==True:
    print(str(num) + " è un numero primo")

input("Premere invio per uscire...")