"""

Oblicz sumę sześcianów liczb naturalnych od 0 do 100. Rozwiń swój program, który policzy ile
liczb naturalnych (od 0) trzeba zsumować, by uzyskać liczbę większą niż 10^6

"""

def main():
     
    suma = 0
    n = 0

    while n <= 100:

        if suma > 1000000:
            print(f"Suma szescianów {suma} > 10^6 gdy n={n}")
            break

        n += 1
        szescian = n*n*n
        suma += suma + szescian
        print(f"n={n} suma: {suma}")

    print(f"Suma sześcianów liczb naturalnych od 0 do 100: {suma}")

if __name__ == "__main__":
    
    main()