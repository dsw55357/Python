"""

Program w którym zapytasz użytkownika o ilość liczb (n), następnie użytkownik musi
wpisać określone liczby ograniczone do ilości liczb n. Program powinien po wczytaniu
wyświetlić komunikat, czy liczba jest z przedziału [-6,6].

"""

def main():

    n = int(input("Podaj ilość liczb (n): "))

    for l in range(1, n+1):
        liczba = int(input("Podaj liczbę do zbioru: "))

        if liczba >= -6 and liczba <= 6:
            print(f"Liczna {liczba} jest z przedziału [-6, 6]") 
        else:
            print(f"Liczna {liczba} nie jest z przedziału [-6, 6]") 

if __name__ == "__main__":
    
    main()