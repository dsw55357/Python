# 6. Oblicz średnią prędkość jazdy samochodu, który dystans 30km pokonał w 15 minut.
# Wynik podaj w km/h. O ile wynik się zmieni jeśli kolejne 30 km przejechał 12 minut?
# Z jaką średnią prędkością przejechał samochód cały dystans?

def srednia_predkosc(dystans, czas):
    predkosc = dystans/czas
    return predkosc

def main():

    dystans = 30 #km
    czas = 15 #minut
    czas_h_1 = czas/60
    v1 = srednia_predkosc(dystans, czas_h_1)
    print(f"Średnia predkość na {dystans} [km] w czasie {czas_h_1} [h]: {v1} km/h")

    #dystans = 30 #km
    czas = 12 #minut
    czas_h_2 = czas/60

    v2 = srednia_predkosc(dystans, czas_h_2)
    print(f"Średnia predkość na {dystans} [km] w czasie {czas_h_2} [h]: {v2} km/h")

    # Różnica w prędkości
    roznica_predkosci = abs(v2 - v1)

    # Wyświetlenie różnicy w prędkości
    print(f"Różnica w prędkości: {roznica_predkosci:.2f} km/h")

    # Z jaką średnią prędkością przejechał samochód cały dystans?
    srednia_predkosc_ = (2 * dystans)/(czas_h_1 + czas_h_2)
    print(f"Średnia prędkości: {srednia_predkosc_:.2f} km/h")
    
if __name__ == "__main__":

    main()
