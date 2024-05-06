"""

Program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć największą
spośród podanych liczb oraz wydrukować na ekranie informację mówiącą o tym, ile razy
największa liczba wystąpiła w podanym ciągu liczb.

"""

def main():

    n = int(input(f"Podaj długość ciągu (n): "))

    i = 1

    lista = []

    while i <= n:
        lista.append(int(input(f"Podaj {i} z {n} liczb całkowitych: ")))
        i += 1
    
    lista.sort(reverse=True)

    print(f"Największa z podanych : {lista[0]}")

    print(f"Ilość wystąpień {lista[0]} : {lista.count(lista[0])}")


if __name__ == "__main__":
    
    main()