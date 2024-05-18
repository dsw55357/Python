"""

Program w którym zdefiniujesz dwie zmienne typu int. Program zapyta
użytkownika: „Na jakiej wysokości lecimy? [w metrach]:”. Jeśli będzie wysokość poniżej
5 km to program ma wypisać wartość podaną przez użytkownika„ km to za nisko!” . W
przeciwnym razie „Na tej wysokości jesteś już bezpieczny”.

"""

import time

wysokosc = 0
wyskosc_bezpieczna = 5 # km

przyspieszenie = 9.81
predkosc_pionowa = 0 

czas_symulacji = 15 # sekund
czas = 0

def symulacja_wysokosc(czas):

    global predkosc_pionowa, wysokosc

    # Obliczenie przyrostu prędkości pionowej
    przyrost_predkosci = przyspieszenie * czas

    # Aktualizacja prędkości pionowej
    predkosc_pionowa += przyrost_predkosci

    # Obliczenie przyrostu wysokości
    przyrost_wysokosci = predkosc_pionowa * czas

    # Aktualizacja wysokości
    wysokosc += przyrost_wysokosci

    return wysokosc

def main():

    global czas, wysokosc

    wysokosc = int(input("Na jakiej wysokości lecimy? [w metrach] "))

    h_km = wysokosc/1000

    while czas < czas_symulacji:

        if h_km < 5:
            print(f"{h_km} km to za nisko")
        else:
            print("Na tej wysokości jesteś już bezpieczny")
            break

        czas += 0.1

        h_km = symulacja_wysokosc(czas)/1000

        time.sleep(0.3)


if __name__ == "__main__":
    
    main()