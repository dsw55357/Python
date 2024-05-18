"""

Program, w którym program losuje i wczytuje nieujemną liczbę całkowitą n i
jako wynik wypisuje sumę kwadratów liczb od 0 do n, czyli wartość 0 2 + 12 + 32 + ... +
n2 . (Ogranicz liczbę mnożenia do minimum).

"""

import random

def suma_kwadratow(n):
    return (n*(n+1)*(2*n+1))/6

def main():

    # Losowanie liczby całkowitej n z zakresu 0 do 100 (można dostosować zakres w razie potrzeby)
    n = random.randint(0, 10)
    print(f'Wylosowana liczba n: {n}')
    
    # Obliczanie sumy kwadratów
    wynik = suma_kwadratow(n)

    print(f'Suma kwadratów liczb od 0 do {n} wynosi: {wynik}')

if __name__ == "__main__":
    
    main()