"""

Sprawdź możliwość zastosowania pętli w zadaniu : Pracownik przez 12 miesięcy przy zarobkach 3891 zł brutto (nie netto) odkłada co miesiąc 333zł. W każdym miesiącu z całej odłożonej na tą
chwilę kwoty uzyskuje 8% odsetek. Jaką kwotę zgromadzi pracownik ?

"""

def main():

    oszczednosci_miesieczne = 333.00
    # oprocentowanie
    oprocentowanie = 0.08

    kwota_zebrana = 12 * oszczednosci_miesieczne
    okres_oszednosci = 12
    odsetki_lacznie = 0
    i = 1

    # Kapitalizacja odsetek: po 12 miesiacach
    while i  <= okres_oszednosci:
        odsetki = oszczednosci_miesieczne * oprocentowanie
        odsetki_lacznie += odsetki
        print(f"odsetki w {i} miesiącu: {odsetki_lacznie:.2f}")
        i += 1

    lacznie = kwota_zebrana + odsetki_lacznie
    print(f"Łączne oszczednosci {lacznie:.2f} w tym odsetki {odsetki_lacznie:.2f}")

if __name__ == "__main__":
    main()


# https://www.credit-agricole.pl/klienci-indywidualni/oszczednosci-i-inwestycje/kalkulator-oszczednosci