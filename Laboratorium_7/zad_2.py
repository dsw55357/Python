"""

Zadeklaruj krotkę 100 elementową, wypełnioną losowymi liczbami z przedziału 0–10
wykorzystując funkcję random. Sprawdź ile razy wystąpiła liczba 0 oraz 1. Sprawdź ile razy w
krotce znajduje się liczba 2. Wypisz elementy parzyste i nie parzyste za pomocą pętli for.
Zastanów się jak możesz dopisać dodatkowe elementy do krotki.

"""

import random

def main():

    krotka = tuple(random.randint(0, 10) for x in range(0, 100))

    print(krotka)

    print(f"\nilość 0: {krotka.count(0)}")
    print(f"ilość 1: {krotka.count(1)}")
    print(f"ilość 2: {krotka.count(2)}")

    print("\nliczby parzyste: ")
    for l in krotka:
        if l % 2 == 0:
            print(f"{l}, ", end="")

    print("\nliczby nieparzyste: ")
    for l in krotka:
        if l % 2 != 0:
            print(f"{l}, ", end="")
    print("\n")

    # .. jak możesz dopisać dodatkowe elementy do krotki
    s= (2,5,8)
    # Python conversion for list and tuple to one another
    x = list(s)
    print(x)
    print(type(x))

    # Add items by using insert ()
    x.insert(5, 90)
    print(x)

    # Use tuple to convert a list to a tuple ().
    s_insert = tuple(x)
    print(s_insert)
    print(type(s_insert))

if __name__ == "__main__":
    
    main()
