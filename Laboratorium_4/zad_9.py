"""

Program, który wczytuje i zlicza wczytanie po kolei liczby aż do momentu, gdy wartość
bezwzględna różnicy pomiędzy dwoma kolejnymi liczbami będzie mniejsza od 5

"""

def main():

    poprzednia_liczba = 0 
    abs_value = 0
    
    while True:
        try:
            # Wczytanie nowej liczby
            nowa_liczba = float(input("Podaj liczbę: "))
        except ValueError:
            # Obsługa błędnego formatu liczby
            print("Wprowadzona wartość nie jest liczbą. Spróbuj ponownie.")
            continue

        # Sprawdzenie warunku zakończenia pętli
        abs_value = abs(nowa_liczba - poprzednia_liczba)
        if abs_value < 5:
            break

        print(f"abs : {abs_value}")
        
        poprzednia_liczba = nowa_liczba

    print(f"{abs_value} < 5")

if __name__ == "__main__":
    main()