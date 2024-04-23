"""

2. Napisz program, który będzie wyświetlał komunikat, jeśli wartość zmiennej będzie mniejsza lub równa 10, inny komunikat, jeśli wartość tej zmiennej będzie większa od 10, lecz mniejsza lub równa 25 oraz jeszcze inny komunikat, kiedy wartość ta będzie większa od 25.

"""


def main():

    liczba = float(input("Podaj dowolną liczbę:"))

    if liczba <= 10.0:
        print("Podana wartość jest mniejsza lub równa 10")
    elif liczba > 10.0 and liczba <= 25.0:
        print("wartość jest większa od 10, lecz mniejsza lub równa 25")
    elif liczba > 25.0:
        print("wartość większa od 25")


if __name__ == "__main__":
    
    main()
