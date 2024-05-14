"""
zad.1:
Utwórz 4 zestawy złożone z nazw drużyn sportowych min. 10 na każdy zestaw. Spraw by część nazw się powtarzała np. LigaMistrzow= set(["Real Madrid", "PSG", "Bayern
Monachium”"]) Nazwy drużyn do zestawów powinny zostać wpisane losowo z puli 20
zespołów.

zad.2
Sprawdź za pomocą metod intersection(), difference(), union(), issuperset() oraz
issubset() jak zachowają się te 4 zbiory. Jakie można wyciągnąć z tych zestawów
informacje?

zad.3
Sprawdź długość zestawów. Usuń wybrane elementy z zestawów, które się pojawiają.
Dokonaj wybranych porównań. Dokonaj konwersji z zestawu na listę. Co dzięki
takiemu działaniu zyskujemy?

"""

import random

druzyny = [
    "Real Madrid",
    "PSG",
    "Bayern Monachium",
    "Liverpool",
    "Atletico Madryt",
    "Borussia Dortmund",
    "Ajax Amsterdam",
    "AS Roma",
    "Tottenham Hotspur",
    "FC Porto",
    "Arsenal",    
    "Manchester City",
    "FC Barcelona",
    "Juventus",
    "Chelsea",
    "Manchester United",
    "Inter Mediolan",
    "AC Milan",
    "Napoli",
    "Bayer Leverkusen"
]


def generuj_zestaw():

    # Generuje losowy zestaw drużyn sportowych z wykorzystaniem zbiorów.
    
    losowy_zestaw = set()

    while len(losowy_zestaw) < 10:
        losowy_zestaw.add(random.choice(druzyny))  # Dodanie drużyny do zbioru

    return losowy_zestaw


def main():

# część zad.1

    zestaw_1 = generuj_zestaw()
    zestaw_2 = generuj_zestaw()
    zestaw_3 = generuj_zestaw()
    zestaw_4 = generuj_zestaw()

    print("Zestaw 1:", zestaw_1)
    print("Zestaw 2:", zestaw_2)
    print("Zestaw 3:", zestaw_3)
    print("Zestaw 4:", zestaw_4)

# część zad.2

    # intersection zestaw_1 zestaw_2
    # Zbiór wynikowy intersection() zawiera elementy, które są wspólne dla obu zbiorów. 
    print("intersection..:")
    zbiory_wspolne = zestaw_1.intersection(zestaw_2)
    print(zbiory_wspolne)

    # difference
    # Zawiera elementy z zestaw_1, które nie są obecne w zestaw_2.
    print("difference..:")
    roznica_1_2 = zestaw_1.difference(zestaw_2)
    print(roznica_1_2)  
    roznica_2_1 = zestaw_2.difference(zestaw_1)
    print(roznica_2_1) 

    #  Zbiór wynikowy union()
    # union_3_4 zawiera wszystkie unikalne elementy z obu zbiorów zestaw_3 i zestaw_4.
    print("union..:")
    union_3_4 = zestaw_3.union(zestaw_4)
    print(f"czy wynik zawiera wszystkie unikalne elementy z obu zbiorów zestaw_3 i zestaw_4 ? {union_3_4}")


    # issuperset()
    # sprawdzamy czy zestaw_1 zawiera wszystkie elementy zestaw_3, jeśli nie to zwraca False
    print("issuperset..:")
    czy_1_zawiera_3 = zestaw_1.issuperset(zestaw_3)
    print(f"czy zestaw_1 zawiera wszystkie elementy zestaw_3 ? : {czy_1_zawiera_3}")  
    # sprawdzamy czy zestaw_2 zawiera wszystkie elementy zestaw_4, jeśli nie to zwraca False
    czy_2_zawiera_4 = zestaw_2.issuperset(zestaw_4)
    print(f"czy zestaw_2 zawiera wszystkie elementy zestaw_4 ? : {czy_2_zawiera_4}")


    # issubset
    # sprawdza czy zestaw_1 jest podzbiorem zestaw_2, jeśli nie to False
    print("issuperset..:")
    czy_1_zawiera_podzespol_2 = zestaw_1.issubset(zestaw_2)
    print(f"czy zestaw_1 jest podzbiorem zestaw_2 ? : {czy_1_zawiera_podzespol_2}")

    czy_3_zawiera_podzespol_2 = zestaw_3.issubset(zestaw_2)
    print(f"czy zestaw_3 jest podzbiorem zestaw_2 ? : {czy_3_zawiera_podzespol_2}")

# część zad.3

    # Sprawdzenie długości zestawów
    print(len(zestaw_1)) 
    print(len(zestaw_2))
    print(len(zestaw_3))
    print(len(zestaw_4))

    # Konwersja z zestawu na listę:
    lista_a = list(zestaw_2)
    lista_d = list(zestaw_4)

    print(lista_a)
    print(lista_d)

    #Usuwanie wybranych elementów z zestawów:
    print(lista_a[0])
    zestaw_2.remove(lista_a[0])
    print(lista_d[len(lista_d)-1])
    zestaw_4.remove(lista_d[len(lista_d)-1])

    print(zestaw_2)
    print(zestaw_4)


if __name__ == "__main__":
    
    main()
