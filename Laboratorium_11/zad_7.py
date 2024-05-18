"""

Wiedząc, że pierwiastek n-tego stopnia z x równa się x do potęgi 1/n i wykorzystując
wiedzę o użyciu liczb zespolonych w Pythonie, wylicz wartość pierwiastka drugiego
stopnia z −7.

"""

import cmath

def main():

    # Definiujemy liczbę zespoloną
    # Część rzeczywista = -7, część urojona = 0
    liczba_zespolona = complex(-7, 0)  

    # Obliczenie pierwiastka kwadratowego
    pierwiastek_kwadratowy = cmath.sqrt(liczba_zespolona)

    # Wyświetlenie wyniku
    print(f"Pierwiastek kwadratowy z {-7} to {pierwiastek_kwadratowy}.")
   

if __name__ == "__main__":
    
    main()