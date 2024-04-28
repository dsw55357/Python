"""

10. Program, który symuluje działanie „Multi Multi”.

"""

import random

def wylosuj_liczby(ile_wylosowac):
    
    liczby = []
    
    while len(liczby) < ile_wylosowac:
        nowa_liczba = random.randint(1, 80)
        if nowa_liczba not in liczby:
            liczby.append(nowa_liczba)
    
    liczby.sort()

    return liczby   

def na_chybil_trafil(ile_liczb_):
    return wylosuj_liczby(ile_liczb_)

def czy_jest_wygrana(numery_klienta, multi_multi, ile_liczb):

    print(f"Numery klienta: {numery_klienta}")
    print(f"Numery Multi-Multi: {multi_multi}")     

    trafione=0

    for liczba in numery_klienta:
         if liczba in multi_multi:
              trafione +=1

    match trafione:
        case 1:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 2:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 3:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 4:    
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 5:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 6:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 7:    
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 8:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 9:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case 10:
            print(f"Liczba trafień: {trafione}/{ile_liczb}")
        case _: 
            print(f"Brak trafień")

def game():

    try:
        ile_liczb_wylosowac = int(input("Podaj ile liczb wylosować z zakresu [1..10]: "))
        
        if ile_liczb_wylosowac>10:
            print("Podaj liczbę z zakresu 1..10")
        else:
            numery_gracza = na_chybil_trafil(ile_liczb_wylosowac)
            numery_multi = wylosuj_liczby(20)
            czy_jest_wygrana(numery_gracza, numery_multi, ile_liczb_wylosowac)    

    except ValueError:
        print("Niepoprawna wartość. Wprowadź liczbę całkowitą.")

def main():
    
    game()
            
if __name__ == "__main__":
        main()