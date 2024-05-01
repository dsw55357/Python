"""

Sprawdź, czy podana przez użytkownika liczba jest liczbą pierwszą. Dla przypomnienia –liczba
pierwsza to liczba naturalna większa od siebie, która ma dokładnie dwa dzielniki naturalne –1
oraz samą siebie.

"""

def main():

    liczba = None
    liczba = int(input("Podaj liczbę: "))

    if liczba <= 1:
        print(f"{liczba} - to nie jest liczba pierwsza")
        return False
  
    i = 2
    ile_dzielnikow = 0
    while i <= liczba:
        if liczba % i == 0: 
            print(f"podzielna przez {i}")
            ile_dzielnikow += 1
        i += 1

    if ile_dzielnikow+1 <= 2:
        print(f"{liczba} - to liczba pierwsza")
    else:
        print(f"{liczba} - to nie jest liczba pierwsza")

            
if __name__ == "__main__":
    main()

# 2: i=2 
# 3: i=3
# 4: i=2; i=4
# 5: i=5
# 6: i=2; i=3; i=6