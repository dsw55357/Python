"""

Program, który podaje 50 razy wynik rzutu monetą - losowo 0 lub 1. 
Zapamiętuj liczbę wylosowanych zer i jedynek i na koniec wyświetl podsumowanie. 
Zmodyfikuj program żeby zamiast 0 lub 1 po wylosowaniu wyświetlało się "orzeł" lub "reszka".

"""

import random

def podsumowanie(tablica):

    licznik_1 = 0
    licznik_0 = 0
    for e in tablica:
        if e:
            licznik_1 += 1  

    licznik_0 = len(tablica) - licznik_1
    print(f"reszka: {licznik_0} \norzeł: {licznik_1}")

def game():
    tablica_rzutow_moneta = []

    for i in range(0, 50):
        tablica_rzutow_moneta.append(random.randint(0, 1))


    print(f" {tablica_rzutow_moneta}")
    podsumowanie(tablica_rzutow_moneta)

    # podumowanie używając nazwy orzeł, reszka 
    print("[ ", end="")
    for l in tablica_rzutow_moneta:
        if l:
            print(f"orzeł, ", end="")
        else:
            print(f"reszka, ", end="")

    print("]\n")

def main():
    
    game()
            
if __name__ == "__main__":
        main()