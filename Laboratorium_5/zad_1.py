"""

Program obliczający średnią arytmetyczną z n liczb całkowitych wprowadzonych z
klawiatury przy uwzględnieniu tylko liczb nieujemnych uwzględniając instrukcje continue.
Program powinien dodatkowo umożliwiać zliczać wartości typu float oraz int. Zaproponuj
modyfikację programu wykorzystując przy tym funkcję random.

"""

import random

def wersja_1():
    
    poprzednia_liczba = 0 
    suma = 0
    n = 1
        
    while True:
        try:
            # Wczytanie nowej liczby
            nowa_liczba = float(input("Podaj liczbę: "))
            if nowa_liczba < 0:
                raise ValueError("Liczba musi być nie^ujemna!")

        except ValueError as e:
            print(f"{e} Spróbuj ponownie.")
            continue

        if nowa_liczba != 0:
            suma += nowa_liczba
            print(f"Średnia arytmetyczna : {suma/n}")
            n += 1

        # Sprawdzenie warunku zakończenia pętli
        if nowa_liczba == poprzednia_liczba:
            print("Warunek równości osiągniety.")
            break
        
        poprzednia_liczba = nowa_liczba


def wersja_2(n):

    srednia = 0
    suma = 0    
    i = 1
    while i <= n:
        nowa_liczba = random.uniform(-80, 80)
        if nowa_liczba < 0:
            continue
        suma += nowa_liczba
        print(f"{nowa_liczba} : suma {suma}")
        srednia = suma/i
        i += 1
    
    print(f"Średnia arytmetyczna : {srednia:.2f} [{suma:.2f}/{n}]")

def main():

    # wersja_1()

    wersja_2(5)

if __name__ == "__main__":
    
    main()
    