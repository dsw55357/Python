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

    return liczby   

def na_chybil_trafil():
    return wylosuj_liczby(10)

def czy_jest_wygrana(numery_klienta, multi_multi):

    print(f"Numery klienta: {numery_klienta}")
    print(f"Numery Multi-Multi: {multi_multi}")     

    trafione=0

    for liczba in numery_klienta:
         if liczba in multi_multi:
              trafione +=1

    match trafione:
        case range(1, 10):
            print(f"Liczba trafień: {trafione}/10")
        case _: 
            print(f"Brak trafień")

def game():

    try:
        ile_liczb_wylosowac = int(input("Podaj ile liczb wylosować z zakresu [1..10]: "))
        if ile_liczb_wylosowac>10:
            print("Podaj liczbę z zakresu 1..10")
        else:
            numery_gracza = na_chybil_trafil()
            numery_multi = wylosuj_liczby(20)

        czy_jest_wygrana(numery_gracza, numery_multi)    
    except ValueError:
        print("Niepoprawna wartość. Wprowadź liczbę całkowitą.")

def main():
    
    game()
            
if __name__ == "__main__":
        main()