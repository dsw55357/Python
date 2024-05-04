"""

Napisz program w którym zadeklarujesz w tablicy 10 dowolnych elementów z zakresu liczb 0-59 i dodasz 3 dowolne liczby parzyste do tablicy metodą append i insert i usuniesz 3 dowolne liczby nieparzyste metodą pop i remove. Podmień 5 i 10 element tablicy na wartości 3 i 33.

"""

import random

def main():
    tablica = []

    i = 0
    while i < 10:
        tablica.append(random.randint(0, 59))
        print(f"{tablica[i]}")
        i += 1
    print(tablica)
    
    i = 0
    print("append")
    while i < 3:
        liczba = int(input(f"Podaj liczbę parzystą: "))
        tablica.append(liczba)
        print(f"{tablica[len(tablica)-1]}")
        i += 1
    print(tablica)

    i = 0
    print("insert")
    while i < 3:
        liczba = int(input(f"Podaj liczbę parzystą: "))
        pozycja = int(input(f"Podaj miejsce gdzie wstawić liczbę: "))
        tablica.insert(pozycja, liczba)
        print(f"{tablica[len(tablica)-1]}")
        i += 1
    print(tablica)


    i = 0
    usuniety = 0
    print("pop")
    while usuniety < 3 and i < len(tablica):
        if tablica[i] % 2 != 0:
            print(f"usuwam metodą pop element: {tablica[i]}")
            tablica.pop(i)
            usuniety += 1
        else:
            i += 1
    print(tablica)

    i = 0
    usuniety = 0
    print("remove")
    while usuniety < 3 and i < len(tablica):
        if tablica[i] % 2 != 0:
            print(f"usuwam metodą remove element: {tablica[i]}")
            tablica.remove(tablica[i])
            usuniety += 1
        else:
            i += 1
    print(tablica)

    print("Podmień 5 i 10 element tablicy na wartości 3 i 33.")
    if len(tablica) < 10:
        print("Lista musi mieć co najmniej 10 elementów!")
    else:
        tablica[5-1] = 3
        tablica[10-1] = 33
    print(tablica)

if __name__ == "__main__":
    
    main()

