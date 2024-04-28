"""

Program, który symuluje działanie „Mini LOTTO”.

"""

import random

def wylosuj_liczby(ile_liczb = 5):
    
    liczby = []
    
    while len(liczby) < ile_liczb:
        nowa_liczba = random.randint(1, 42)
        if nowa_liczba not in liczby:
            liczby.append(nowa_liczba)

    liczby.sort()

    return liczby  

def czy_jest_wygrana(numery_klienta, lotto, ile_liczb = 5):

    print(f"Numery klienta: {numery_klienta}")
    print(f"Numery miniLOTTO: {lotto}")     

    trafione=0

    for liczba in numery_klienta:
         if liczba in lotto:
              trafione +=1

    match trafione:
        case 5: 
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 4: 
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 3: 
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 2: 
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 1: 
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case _: 
            print(f"Brak trafień")


def main():
    numery_gracza = wylosuj_liczby()
    numery_miniLOTTO = wylosuj_liczby()

    czy_jest_wygrana(numery_gracza, numery_miniLOTTO)
    
            
if __name__ == "__main__":
        main()