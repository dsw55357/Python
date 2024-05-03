"""

Program uwzględniając wyrażenie break, który wypisze pierwsze 6 liczb z zadanego
zakresu n do x, a następnie przerwie działanie obliczając ich minimum, maksimum oraz średnią
i medianę. Program powinien przerwać również działanie w przypadku podania liczby 0 przez
użytkownika.

"""

import statistics

def calc(zakres):

    liczby = []
    suma = 0
    c = 0
    for i in range(zakres[0], zakres[1]):
        if c < 6:
            #print(f"{i}", end=", ")
            suma += i
            liczby.append(i)
        else:
            break
        c += 1

    print(f"{liczby}")
    print(f"Suma: {suma}")
    print(f"Minimum: {min(liczby)}")
    print(f"Maximum: {max(liczby)}")
    print(f"Mediana: {statistics.median(liczby)}")

def main():

    zakres = []
    # Wczytanie zakresu liczb
    print("Zdefiniuj zakres od n do x")

    while True:
        try:
            if len(zakres) < 2:
                r = int(input("Podaj liczbę: "))
                if r == 0:
                    print("Podałeś Zero - to nie jest prawidłowa cyfra. Spróbuj ponownie")
                    break

                if len(zakres) > 0:
                    if r-zakres[0] < 6:
                        print("Za wąski zakres. Spróbuj ponownie")
                        continue

                    if zakres[0] == r: 
                        print("x nie może być równe n. Spróbuj ponownie")
                        continue
                    else:
                        zakres.append(r)
                else:
                    zakres.append(r)
            else:
                break
                
        except ValueError as e:
            print(f"{e} Spróbuj ponownie.")
            continue 

    if len(zakres) > 1:
        #print(f"{zakres} [{r-zakres[0]}]")
        calc(zakres)




if __name__ == "__main__":
    
    main()
    