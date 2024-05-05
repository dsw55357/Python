"""

Pogram, który wygeneruje ciąg n – liczb zadeklarowanych przez użytkownika z zakresu
x do z – zadeklarowanych przez użytkownika. Wypisz trzeci element od końca. Usuń k-element
od końca(wybrany przez użytkownika). Wygeneruj drugi ciąg, który scalisz z pierwszą listą.
Sprawdź czy liczby się powtarzają. Wygeneruj długość listy oraz ilość wystąpień każdej liczby w
połączonym ciągu.

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
 
    print(lista)

    # Wypisz trzeci element od końca
    print(f"-3. elem.: {lista[-3]}")

    k = int(input(f"Usuń k-element od końca: "))
    lista.pop(-k)

    print(f"-{k}. elem.: {lista}")

    lista2 = []

    # Wygeneruj drugi ciąg
    for l in range(0, n):
        lista2.append(random.randint(x, z))

    print(lista2)

    lista3 = lista + lista2
    print(f"{lista3} : len {len(lista3)}")

    for l in lista3:
        if lista3.count(l):
            print(f"powtórzenia : {l}[{lista3.count(l)}]")

if __name__ == "__main__":
    
    main()

