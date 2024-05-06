"""

Program, który pomiesza zawartość listy wygenerowanej przez funkcję random a
następnie te liczby posortuje w wybranej kolejności np. od najmniejszej do największej. Wypisz zawartość listy przed i po pomieszaniu oraz sortowaniu jej elementów.

"""
import random

def main():

    print("*")

    lista = []

    for i in range(0, 64):
        lista.append(random.randint(0, 1024))

    print(f"start: {lista}")

    random.shuffle(lista)

    print(f"shuffle: {lista}")

    lista.sort()

    print(f"sorted: {lista}")

    print(f"reverse: {lista[::-1]}")



if __name__ == "__main__":
    
    main()