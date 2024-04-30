"""

Program przy użyciu pętli while, który skończy wczytywania liczb podawanych przez użytkownika, gdy ich suma przekroczy 100 albo średnia wyniesie 66.

"""

def main():

    liczba = None
    suma = 0
    index = 1
    srednia = 0
    while True:
        try:
            liczba = int(input("Podaj liczbę: "))
            suma += liczba
           
            srednia = suma / (index)

            if suma > 100:
                print(f"suma > 100: {suma}")
                break
            else:
                print(f"suma: {suma}")
            if srednia == 66:
                print(f"srednia = 66")
                break

            index += 1

        except ValueError:
            print("Wprowadzona wartość nie jest liczbą. Spróbuj ponownie.")
            continue     

    print("Kończymy zabawę")
            
if __name__ == "__main__":
    main()