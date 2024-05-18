"""

Kalkulator zamiany liczb dziesiętnych na liczby binarne, ósemkowe oraz
szesnastkowe. Następnie dopisz odpowiednie funkcje odpowiadające za zamianę
podanych wartości z klawiatury z systemów binarnych na szesnastkowy i ósemkowy
oraz z szesnastkowych na ósemkowy.

Systemy pozycyjne:
Python pozwala na bardzo łatwą konwersję między systemami pozycyjnymi.
• hex() - służy do konwersji liczby całkowitej na odpowiadającą jej postać
szesnastkową.
• oct() - służy do konwersji liczby całkowitej na odpowiadającą jej postać ósemkową.
• bin()- służy do konwersji liczby całkowitej na odpowiadającą jej postać binarną.

"""

def dziesietna_na_binarna(liczba_dziesietna):
    return bin(liczba_dziesietna)[2:]

def dziesietna_na_osmekowa(liczba_dziesietna):
    return oct(liczba_dziesietna)[2:]

def dziesietna_na_szesnastkowa(liczba_dziesietna):
    return hex(liczba_dziesietna)[2:]

def binarna_na_szesnastkowa(liczba_binarna):
    return hex(int(liczba_binarna, 2))[2:]

def binarna_na_osmekowa(liczba_binarna):
    return oct(int(liczba_binarna, 2))[2:]

def szesnastkowa_na_osmekowa(liczba_szesnastkowa):
    return oct(int(liczba_szesnastkowa, 16))[2:]

def wybor_1():
    dziesietna = int(input("Podaj liczbę dziesiętną: "))
    binarna = dziesietna_na_binarna(dziesietna)
    print(f"\n{dziesietna} (dziesiętna) = {binarna} /binarna")

def wybor_2():
    dziesietna = int(input("Podaj liczbę dziesiętną: "))
    osemkowa = dziesietna_na_osmekowa(dziesietna)
    print(f"\n{dziesietna} (dziesiętna) = {osemkowa} /osemkowa")

def wybor_3():
    dziesietna = int(input("Podaj liczbę dziesiętną: "))
    hex = dziesietna_na_szesnastkowa(dziesietna)
    print(f"\n{dziesietna} (dziesiętna) = {hex} /szesnastkowa")

def wybor_4():
    binarna = int(input("Podaj liczbę binarna: "))
    hex = binarna_na_szesnastkowa(binarna)
    print(f"\n{binarna} (binarna) = {hex} /szesnastkowa")

def wybor_5():
    binarna = int(input("Podaj liczbę binarna: "))
    osemkowa = binarna_na_osmekowa(binarna)
    print(f"\n{binarna} (binarna) = {osemkowa} /osmekowa")

def wybor_6():
    hex = int(input("Podaj liczbę hex: "))
    osemkowa = szesnastkowa_na_osmekowa(hex)
    print(f"\n{hex} (szesnastkowa) = {osemkowa} /osmekowa")

def menu():

    while True:
        # Menu kalkulatora
        print("\nKalkulator systemów liczbowych")
        print("1. Dziesiętna na binarną")
        print("2. Dziesiętna na ósemkową")
        print("3. Dziesiętna na szesnastkową")
        print("4. Binarną na szesnastkową")
        print("5. Binarną na ósemkową")
        print("6. Szesnastkową na ósemkową")
        print("7. Wyjście")

        wybor = input("Wybierz opcję [1-7]: ")

        if wybor == '1':
            wybor_1()
        elif wybor == '2':
            wybor_2()
        elif wybor == '3':
            wybor_3()
        elif wybor == '4':
            wybor_4()
        elif wybor == '5':
            wybor_5()
        elif wybor == '6':
            wybor_6()
        elif wybor == '7':            
            break

def main():

    menu()

if __name__ == "__main__":
    
    main()