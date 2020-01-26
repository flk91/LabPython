import random

def carica(n: int) -> list:
    """
    Carica una lista con valori presi in input,
    senza eseguire operazioni di convalida

    Parameters
        n (int) : numero di elementi che il vettore conterrà

    """
    vet = []
    for i in range(0, n):
        vet.append(input("Inserire " + i +"-esimo valore: "))
    return vet



def carica_rand(n: int, rmin:int=0, rmax: int=1000) -> list:
    """ 
    Restituisce un vettore di numeri casuali

    Parameters
        n(int): numero di elementi
        rmin(int): valore minimo da generare
        rmax(int): velore massimo da generare
    """
    
    vet = []
    random.seed() # inizializza il generatore di numeri casuali
    for i in range(0, n):
        vet.append(random.randint(rmin, rmax))
    return vet