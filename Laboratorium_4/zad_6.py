"""

Program, który sprawdzi, czy wpisana przez użytkownika liczba jest doskonała. Liczba doskonała, to taka liczba, która jest sumą wszystkich swoich dzielników właściwych (czyli mniejszych od niej samej).

"""

def main():

    liczba = None
    liczba = int(input("Podaj liczbę: "))
    print(f"podałeś {liczba}")

    suma_dzielnikow = 0

    for dzielnik in range(1, liczba):
        
        if liczba % dzielnik == 0:   
            suma_dzielnikow += dzielnik

    if  suma_dzielnikow == liczba:
        print("Podana liczba {liczba} jest doskonała!")
    else:
        print("Podana liczba {liczba} nie jest doskonała!")
            
if __name__ == "__main__":
    main()

# Dzielniki właściwe 6 to 1, 2 oraz 3. Jako że suma tych liczb jest równa sześć, jest to liczba doskonała.
# Kilka kolejnych liczb doskonałych: 6, 28, 496, 8128, 33550336, 8589869056, 137438691328

