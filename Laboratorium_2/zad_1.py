"""
1. Napisz program Czy liczba a jest podzielna przez b? Program ma pobrać od użytkownika dwie liczby całkowite a, b. Jako wynik pracy program ma wydrukować informację mówiącą o tym, czy liczba a jest podzielna przez liczbę b (jeden z tekstów A JEST PODZIELNE PRZEZ B lub A NIE JEST PODZIELNE PRZEZ B).

"""

def czy_liczba_podzielna(a, b):
    if a % b == 0:
        return f"{a} JEST PODZIELNE PRZEZ {b}"
    else:
        return f"{a} NIE JEST PODZIELNE PRZEZ {b}"
    

def main():
    a = int(input("Podaj pierwszą liczbę całkowitą: "))
    b = int(input("Podaj drugą liczbę całkowitą: "))

    result = czy_liczba_podzielna(a, b)
    print(result)


if __name__ == "__main__":

    main()
