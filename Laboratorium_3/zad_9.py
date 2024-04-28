"""

9. Program, który symuluje działanie „LOTTO”

"""
import random

def wylosuj_liczby():
    
    liczby = []
    
    while len(liczby) < 6:
        nowa_liczba = random.randint(1, 49)
        if nowa_liczba not in liczby:
            liczby.append(nowa_liczba)

    liczby.sort()

    return liczby      

def czy_jest_wygrana(numery_klienta, lotto):

    print(f"Numery klienta: {numery_klienta}")
    print(f"Numery LOTTO: {lotto}")     

    trafione=0

    for liczba in numery_klienta:
         if liczba in lotto:
              trafione +=1

    match trafione:
        case 6: 
            print(f"Liczba trafień: {trafione}/6")
        case 5: 
            print(f"Liczba trafień: {trafione}/6")
        case 4: 
            print(f"Liczba trafień: {trafione}/6")
        case 3: 
            print(f"Liczba trafień: {trafione}/6")
        case 2: 
            print(f"Liczba trafień: {trafione}/6")
        case 1: 
            print(f"Liczba trafień: {trafione}/6")
        case _: 
            print(f"Brak trafień")

def main():
    
    numery_gracza = wylosuj_liczby()
    numery_LOTTO = wylosuj_liczby()

    czy_jest_wygrana(numery_gracza, numery_LOTTO)
    
            
if __name__ == "__main__":
        main()