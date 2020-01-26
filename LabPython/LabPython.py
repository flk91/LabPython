import os

print("Laboratorio Python")
print("------------------\n")
print("Seleziona un progetto da avviare")

print("eq2g\tEquazioni di secondo grado")
print("retta\tCoordinate linea retta")


scelta=input("Digitare una scelta: ")
print("\n\n")

if scelta=="eq2g":
    os.system("python eq2g.py")
elif scelta=="retta":
    os.system("python retta.py")
else:
    print("scelta non riconosciuta")