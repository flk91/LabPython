import math

###########################
# FUNZIONE sdiv(n)
#
# Preso in input un numero n,
# restituisce la somma dei suoi divisori propri
# (i divisori del numero compreso 1, escluso n
###########################


def sdiv(n):
    sd=0
    for i in range(1, n):
        if n%i==0:
            sd=sd+i
    return sd

###########################

def amicabili(a, b):
    sa = sdiv(a)
    sb = sdiv(b)
    if sa==b and sb==a:
        ami=True
    else:
        ami=False
    return ami

#############################

x=int(input("Digita il primo numero: "))
y=int(input("Digita il secondo numero: "))
a = amicabili(x, y)
if a==True:
    print(x, "e", y, "sono amicabili")
else:
    print(x, "e", y, "NON sono amicabili")
