"""

Program przy użyciu pętli while wczytujący z klawiatury wartości, a następnie wyświetlający średnią tych wartości, niech program kończy wprowadzanie, kiedy natrafi na cyfrę 0. Czy możliwe by było przerwanie jeśli ktoś wpisze wybrany znak albo string o treści NULL?

"""

def main():

    liczba = None
    suma = 0
    index = 0
    while liczba != 0:
        try:
            liczba = int(input("Podaj liczbę: "))
            suma += liczba
            index += 1
        except ValueError:
            print("Wprowadzona wartość nie jest liczbą. Spróbuj ponownie.")
            continue
        
    if index > 0:
        srednia = suma / (index-1)
        print(f"średnia {suma}/{index-1}={srednia}")
    else:
        print("Nie podano liczb")

            
if __name__ == "__main__":
    main()