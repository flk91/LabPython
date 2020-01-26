n1 = input("Digita un numero")
n2= input("Digita un altro numero")
oper = input("Scegliere un operatore [+ - * /]")

n1 = int(n1)
n2 = int(n2)

if oper=='+':
    ris = n1+n2
elif oper=='-':
    ris=n1-n2
elif oper == '*':
    ris = n1*n2
elif oper=='/':
    if n2 != 0:
        ris = n1/n2
    else:
        print("Non si può dividere un numero per zero")
else:
    print("Operatore non valido")