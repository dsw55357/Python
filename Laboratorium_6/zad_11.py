"""

Program generujący ciąg liczb pierwszych od 0 do n metoda sita Eratostanesa

"""

def main( ):

    n = int(input(f"Podaj wielkość zbioru liczb całkowitych: ")) 

    liczbyPierwsze = [True] * (n + 1) # Budujemy tablicę z wartościami True
    
    liczbyPierwsze[0] = False # 0 - to nie jest liczna pierwsza
    liczbyPierwsze[0] = False # 1 - to nie jest liczna pierwsza

    dzielnik = 2
    i = 3  

    while dzielnik < n:
        while i <= n:
            if i % dzielnik == 0:
                liczbyPierwsze[i] = False
            i += 1
        dzielnik += 1
        i = dzielnik + 1

    i = 0
    while i < len(liczbyPierwsze):
        if liczbyPierwsze[i]:
            print(f"{i}, ", end="")
        i += 1
    print("\n")

if __name__ == "__main__":
    
    main()