"""

Program, który wyświetli n kolejnych potęg naturalnych liczby 2.

"""

def main():
    lista_poteg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in lista_poteg:
        potega_liczby_2 = 2**i
        print(f"2^{i} : {potega_liczby_2}")


if __name__ == "__main__":

    main()