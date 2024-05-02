"""

Program, który wczytuje i sumuje po kolei liczby aż do momentu, gdy dwie kolejne liczby
będą takie same.

"""

def main():
    
    poprzednia_liczba = 0 
    suma = 0
        
    while True:
        try:
            # Wczytanie nowej liczby
            nowa_liczba = float(input("Podaj liczbę: "))
        except ValueError:
            # Obsługa błędnego formatu liczby
            print("Wprowadzona wartość nie jest liczbą. Spróbuj ponownie.")
            continue

        # Sprawdzenie warunku zakończenia pętli
        if nowa_liczba == poprzednia_liczba:
            print("Warunek równości osiągniety.")
            break

        suma += nowa_liczba
        print(f"Suma : {suma}")
        
        poprzednia_liczba = nowa_liczba

if __name__ == "__main__":
    main()