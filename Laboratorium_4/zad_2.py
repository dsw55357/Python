"""

Program przy użyciu pętli while wyświetlający na ekranie liczby od 254 do 320, ale
niepodzielne przez 2 ale podzielne przez 5. Jak zmieni się program jeśli będziemy chcieli
wyświetlać tylko liczby ujemne z zakresu -320 do -254 ?

"""

def main():
    x = 254
    while x <= 320:
        if x % 2 != 0 and x % 5 == 0:
            print(f"{x}")
        x += 1

    x = -320
    while x <= -254:
        if x % 2 != 0 and x % 5 == 0:
            print(f"{x}")
        x += 1

            
if __name__ == "__main__":
    main()