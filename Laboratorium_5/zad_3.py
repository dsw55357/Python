"""

Program, który będzie odwracał kolejność cyfr w liczbie. Przykładowo liczba 12345 w
wyniku działania programu zostanie wyświetlona jako 54321. Dodaj warunek w którym
sprawdzamy, czy wczytana z klawiatury liczba jest palindromem, tzn. czytana od końca jest
taka sama np. 12321,234432,3445.

"""

def main():

    n = int(input("Podaj liczbę do odwrócenia: "))
    
    # Odwracamy kolejność znaków
    odwrocona = int(str(n)[::-1])
    
    if int(odwrocona) == n:
        print(f"Podana liczba {odwrocona} jest palindromem")
    else:
        print(f"Podana Liczba {n} po odwróceniu: {odwrocona}")

if __name__ == "__main__":
    
    main()