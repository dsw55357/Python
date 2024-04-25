"""

2. Napisz program, który wypisze na ekran liczby od zadanej wartości do zera i podzielne przez 6 oraz 9.

"""

def podzielne_przez_6_i_9(liczba):

    """
    Sprawdza, czy dana liczba jest podzielna przez 6 i 9.

    Args:
        liczba: Liczba, dla której sprawdzana jest podzielność.

    Returns:
        True, jeśli liczba jest podzielna przez 6 i 9, False w przeciwnym razie.
    """

    if liczba % 6 == 0 and liczba % 9 == 0:
        return True
    else:
        return False

def main():

    print("Program, wypisze na ekran liczby od zadanej wartości do zera i podzielne przez 6 oraz 9.")

    wartosc_poczatkowa = int(input("Podaj wartość początkową: "))

    # Pętla iterująca od wartości początkowej do zera
    for liczba in range(wartosc_poczatkowa, 0, -1):
    # Sprawdzenie podzielności i wyświetlenie liczby
        if podzielne_przez_6_i_9(liczba):
            print(liczba)


if __name__ == "__main__":

    main()