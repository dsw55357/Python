"""

Zadeklaruj krotkę składającą się 6 elementów znakowych. Sprawdź za pomocą polecenia in czy
w krotce znajduje się słowo, które zostało zadeklarowane. Wypisz jego indeks jeśli słowo
zostało znalezione. Spróbuj do krotki wprowadzić dłuższy tekst i sprawdź czy słowo wpisane
przez użytkownika znajduje się w tym tekście i ile razy w nim wystąpiło.

"""

def main():

    krotka = ('Ala', 'ma', 'kota', 'Ala', 'lubi', 'mleko')
    szukane_slowo = "Ala"

    if szukane_slowo in krotka:
        print(f"Słowo '{szukane_slowo}' znajduje się w krotce.")
        # Znalezienie indeksu słowa
        indeks = krotka.index(szukane_slowo)
        print(f"Indeks słowa '{szukane_slowo}': {indeks}")
    else:
        print(f"Słowo '{szukane_slowo}' nie znajduje się w krotce.")

    tekst = """Zadeklaruj krotkę składającą się 6 elementów znakowych. Sprawdź za pomocą polecenia in czy w krotce znajduje się słowo, które zostało zadeklarowane. Wypisz jego indeks jeśli słowo
zostało znalezione. Spróbuj do krotki wprowadzić dłuższy tekst i sprawdź czy słowo wpisane
przez użytkownika znajduje się w tym tekście i ile razy w nim wystąpiło."""
    
    szukane_slowo = input("Podaj słowo, które chcesz wyszukać w tekście: ")

    # Zliczanie wystąpień słowa
    liczba_wyst = tekst.count(szukane_slowo)

    if liczba_wyst > 0:
        print(f"Słowo '{szukane_slowo}' występuje w tekście {liczba_wyst} razy.")
    else:
        print(f"Słowo '{szukane_slowo}' nie znajduje się w tekście.")


if __name__ == "__main__":
    
    main()