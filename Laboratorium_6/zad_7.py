"""

Program typu losowanie Lotto znane z poprzednich zajęć w oparciu o funkcję random i
listy. Użytkownik powinien do listy wpisać liczby i porównać je z liczbami w wylosowanej liście.
Użytkownik powinien otrzymać informację ile liczb trafił, jaką nagrodę pienieżną wygrał np.
10 000 000 PLN. Program powinien umożliwić np. wygenerowanie losowo liczb użytkownika
przy większej ilości losów.

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

def liczby_gracza():
    
    liczby = []
    i = 1
    print("Wybierz swoje liczby")
    while len(liczby) < 6:
        nowa_liczba = int(input(f"Podaj {i} z 6 z 49 liczb: "))
        if nowa_liczba <= 49: 
            if nowa_liczba not in liczby:
                liczby.append(nowa_liczba)
                i += 1
        else:
            print("Nieprawidłowa liczba! Podaj liczbę od 1 do 49")

    liczby.sort()

    return liczby  


def czy_jest_wygrana(numery_klienta, lotto):

    print(f"Numery gracza: {numery_klienta}")
    print(f"Numery LOTTO: {lotto}")     

    trafione=0

    for liczba in numery_klienta:
         if liczba in lotto:
              trafione +=1

    match trafione:
        case 6: 
            print(f"Liczba trafień: {trafione}/6")
            print("Trafiona szóstka, wygrana 5 000 000,00 zł")
        case 5: 
            print(f"Liczba trafień: {trafione}/6")
            print("Trafiona piątka, wygrana 5049,90 zł")
        case 4: 
            print(f"Liczba trafień: {trafione}/6")
            print("Trafiona czwórka, wygrana 264,40 zł")
        case 3: 
            print(f"Liczba trafień: {trafione}/6")
            print("Trafiona trójka, wygrana 24,00 zł")
        case 2: 
            print(f"Liczba trafień: {trafione}/6")
        case 1: 
            print(f"Liczba trafień: {trafione}/6")
        case _: 
            print(f"Brak trafień")

def na_chybil_trafil():

    print("\nNa chybił trafił")
   
    ilosc_losow = int(input("Podaj ilość losów: "))

    if 0 < ilosc_losow <= 10:
        i = 0
        while i < ilosc_losow:
            na_chybil_trafil1 = wylosuj_liczby()
            numery_LOTTO = wylosuj_liczby()
            czy_jest_wygrana(na_chybil_trafil1, numery_LOTTO)
            print("\n")
            i += 1
    else:
        print("\nNieprawidłowy wybór! Sp©óbuj raz jeszcze")


def wyswietl_menu():
     
    print("\nZagraj w Lotto:")
    print("1. Wybierz swoje liczby    - 1")
    print("2. Zagraj na chybił trafił - 2")
    print("0. Wyjście")

def wybierz_opcje():
    
    while True:
        opcja = int(input("Wybierz opcję: "))
        if 0 <= opcja <= 2:
            return opcja
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie")

def main():

    while True:
        wyswietl_menu()
        opcja = wybierz_opcje()

        if opcja == 0:
            break
        elif opcja == 1:
            numery_gracza = liczby_gracza()
            numery_LOTTO = wylosuj_liczby()
            czy_jest_wygrana(numery_gracza, numery_LOTTO)
        elif opcja == 2:
            na_chybil_trafil()

if __name__ == "__main__":
    
    main()