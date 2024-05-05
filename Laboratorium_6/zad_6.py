"""

Program, który usunie z listy duplikaty wygenerowane z wybranego zakresu przez funkcję random, następnie wypisze na ekran ilość pozostałych elementów oraz zwróci długość listy.

"""

import random

def main():

    n = int(input(f"Podaj długość ciągu (n): "))
    print("Podaj liczby z zakresu x do z")
    x = int(input(f"Podaj min wartość (x): "))
    z = int(input(f"Podaj max wartość (z): "))

    lista = []

    for l in range(0, n):
        lista.append(random.randint(x, z))

    lista.sort()

    print(f" {lista} [{len(lista)}]")

    lista_nowa = []
    for i, liczba in enumerate(lista):
        ile = lista.count(liczba)
        if ile > 1:
            if liczba not in lista_nowa:
                lista_nowa.append(liczba)
                print(f"powtórzenia : {liczba} [{ile}]")
        else:
            lista_nowa.append(liczba)

    lista_nowa.sort()

    print(f" {lista_nowa} : len [{len(lista_nowa)}]")

    #lista = list(set(lista))

if __name__ == "__main__":
    
    main()