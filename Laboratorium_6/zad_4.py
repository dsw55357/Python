"""

Program, który jako parametr wejściowy przyjmie liczbę naturalną n. Funkcja powinna zwracać listę składającą się ze wszystkich dzielników liczby n.

"""

def main():

    n = int(input(f"Podaj dowolną liczbę naturalną: "))

    lista = []

    dzielnik = 1
    while dzielnik <= n:
        if n % dzielnik == 0:
            lista.append(dzielnik)
        dzielnik += 1

    print(lista)

if __name__ == "__main__":
    
    main()

