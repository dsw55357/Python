# 4. Napisz program, który wypisze czy podana liczba jest ujemna czy dodatnia
# oraz czy jest podzielna przez 2 z resztą. Zaproponuj odpowiednie warunki.


def main():

    liczba = float(input("Podaj liczbę: "))

    if liczba < 0:
        print("Podana liczba jest ujemna.")
    elif liczba > 0:
        print("Podana liczba jest dodatnia.")
    
    # czy liczba jest podzielna przez 2 z resztą
    if liczba % 2 == 0:
        print(f"{liczba} jest parzysta, czyli podzielna.")
    else:
        print(f"{liczba} jest nieparzysta, czyli nie^podzielna")



if __name__ == "__main__":
    
    main()
