"""

Zadeklaruj krotkę A = 100 elementową, wypełnioną tylko liczbami parzystymi oraz krotkę B =
100 elementową wypełnioną tylko liczbami nieparzystymi. Wykonaj konkatenację. Sprawdź
jej długość. Sprawdź czy krotka zawiera liczby 0 oraz 100. Sprawdź jak zmieniło się ich miejsce
w pamięci.

"""


def main():

    # lista = list(range(100))
    # print(f"{lista}")

    A = tuple(x for x in range(100) if x % 2 == 0)
    print("\nliczby parzyste: ")
    print(f"{A}")
    print(f"id element 0: {id(A[0])}")

    B = tuple(x for x in range(100) if x % 2 != 0)
    print("\nliczby nieparzyste: ")
    print(f"{B}")
    print(id(B))

    C = A + B
    print(C)   
    print(f"len : {len(C)}")

    print(f"ilość 0: {C.count(0)}")
    print(f"ilość 100: {C.count(100)}")
    

    if id(C[0]) == id(A[0]):
        print(f"Element A po konkatenacji zajmuje to samo miejsce w pamięci : {id(C[0])}")


if __name__ == "__main__":
    
    main()