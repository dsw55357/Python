"""

Utwórz dwie krotki w których zadeklarujesz dwa wyrazy. Sprawdź czy są one anagrami – czy
dwa słowa składają się z tych samych liter. Zaproponuj przykładowe wyrazy, które będą
prawidłowymi rozwiązaniami zadania.

np.:

wektor – wtorek
makrela – reklama
łoś – stolik
bryka – rybak

"""

def main():

    krotkaA = (input("Podaj słowo : "))
    print(krotkaA)

    krotkaB = (input("Podaj kolejne słowo : "))
    print(krotkaB)

    if len(krotkaA) != len(krotkaB):
        print("Słowa nie są anagramem")

    if sorted(krotkaA) == sorted(krotkaB):
        print("Słowa są anagramem")

if __name__ == "__main__":
    
    main()