"""

Program przy użyciu pętli while, w którym podajemy liczbę naturalną do momentu
podania liczby podzielnej przez 12. Algorytm kończy działanie napisem: „Podałeś liczbę
podzielną przez 12, wiec kończę działanie pętli".

"""

def main():

    liczba = None
    while liczba is None or liczba % 12 != 0:
        liczba = int(input("Podaj liczbę: "))
        print(f"podałeś {liczba}, bawimy się dalej")
    
    print("Podałeś liczbę podzielną przez 12, wiec kończę działanie pętli")
            
if __name__ == "__main__":
    main()