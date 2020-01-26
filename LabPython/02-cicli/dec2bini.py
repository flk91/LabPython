#preso in input un qualsiasi numero in base 10, restituire la sua
#rappresentazione in base 2.

#colorare lo schermo
import colorama #libreria funzionante su tutti i sistemi operativi
colorama.init()
print(colorama.Back.BLUE)
print(colorama.Fore.WHITE)
print(colorama.Style.BRIGHT)
print(colorama.ansi.clear_screen())
########################

num = int(input("Digita un numero: "))

#nbin è una stringa, cioè una sequenza di caratteri
nbin = ""

d = num

while d>=0:
    nbin += str(d%2)
    d = d // 2
    if d==0: break

nbin_inv = "".join(reversed(nbin))
print("La rappresentazione binaria di " + str(num) + " è " + str(nbin_inv))
input("Premere invio per uscire...")
