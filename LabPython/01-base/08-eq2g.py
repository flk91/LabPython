# EQUAZIONI DI SECONDO GRADO
# Presi in input i coefficienti di un'equazione di secondo grado, 
# mostrare a video le soluzioni.
# Per informazioni: https://www.youmath.it/lezioni/algebra-elementare/equazioni/68-equazioni-di-secondo-grado-ad-unincognita-come-si-risolvono.html

import math

print("Equazioni di secondo grado")
print("--------------------------\n")

a = float(input("Inserire il valore del coefficiente a: "))
b = float(input("Inserire il valore del coefficiente b: "))
c = float(input("Inserire il valore del coefficiente c: "))
# mando in output una riga vuota
print("\n")

delta = b ** 2 * 4 * a * c

if delta < 0:
    print("Non esistono soluzioni reali")
else:
    if delta == 0:
        x = -b / 2 * a
        print("Due soluzioni coincidenti. x =", x)
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("Due soluzioni reali distinte")
        print("x1 =", x1)
        print("x2 =", x2)
        