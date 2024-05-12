"""

Korzystając ze słowników stwórz listę kontaktów. Dodaj do niej 10 pozycji razem z numerami
telefonicznymi. Zmień klucz 1 i ostatniej wartości. Usuń wartości środkowe. Wypisz listę
kontaktów. Wyczyść wszystkie elementy ze słownika. Dodaj do niej 2 pozycje razem z
numerami telefonicznymi. Zaproponuj sortowanie słownika. Czy słownik można
skonwertować na listę? Jeśli tak to w jaki sposób? Czy wtedy też będziemy mogli sortować
dane?

"""

kontakty = {
    "Jan Kowalski": "+48 123 456 789",
    "Anna Nowak": "+48 987 654 321",
    "Krzysztof Wiśniewski": "+48 111 222 333",
    "Marta Dąbrowska": "+48 444 555 666",
    "Piotr Górski": "+48 777 888 999",
    "Zuzanna Zielińska": "+48 222 333 444",
    "Mateusz Kowalski": "+48 555 666 777",
    "Justyna Nowak": "+48 888 999 000",
    "Bartosz Wiśniewski": "+48 333 444 555",
    "Patrycja Dąbrowska": "+48 666 777 888"
}

def pokaz_kontakty():
    for k, v in kontakty.items():
        print(f"{k}: {v}")


def main():

    pokaz_kontakty()

    print("\nZmiana wartości klucza 1 i ostatniego")
    kontakty["Jan Kowalski"] = "+48 123 123 123"
    kontakty["Patrycja Dąbrowska"] = "+48 666 666 666"
    pokaz_kontakty()
    
    print("\nUsunięcie wartości")
    del kontakty["Marta Dąbrowska"]
    del kontakty["Piotr Górski"]
    del kontakty["Zuzanna Zielińska"]
    pokaz_kontakty()

    print("\nDodajemy dwa nowe wpisy")
    kontakty["Jakub Maj"] = "+48 456 123 321"
    kontakty["Katarzyna Kwiecień"] = "+48 457 789 987"
    pokaz_kontakty()

    #print("\nSortowanie słownika według kluczy")
    posortowane_kontakty = sorted(kontakty.items())
    print("\nPosortowana lista kontaktów:")
    for osoba, numer in posortowane_kontakty:
        print(f"{osoba}: {numer}")

    print("\nKonwersja słownika na listę")
    lista_kontaktow = list(kontakty.items())
    # otrzymujemy listę krotek
    for osoba, numer in lista_kontaktow:
        print(f"{osoba} {numer}")

    print("\npo czym ją posortujemy")
    lista_kontaktow.sort()
    for osoba, numer in lista_kontaktow:
        print(f"{osoba} {numer}")

if __name__ == "__main__":
    
    main()