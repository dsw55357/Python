"""

Program który wczyta od użytkownika wielkość kąta w stopniach i wyświetli
wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla
danego kąta jest to możliwe. Zaproponuj rozwiązania dla kątów, 70, 90, 35,180, 240,
360.

"""

import math

katy = [70, 90, 35, 185, 240, 360]

def oblicz(kat_stopnie):

    kat_radiany = math.radians(kat_stopnie)

    # wynik zapisujemy w słowniku wartości sin, cos, tg i ctg dla danego kąta
    wyniki = {
        "sin": math.sin(kat_radiany),
        "cos": math.cos(kat_radiany),
        "tg": math.tan(kat_radiany),
        "ctg": 1 / math.tan(kat_radiany) if math.tan(kat_radiany) != 0 else math.inf
    }

    return wyniki

def main():

    kat_stopnie = float(input("Podaj wartość kąta w stopniach: "))
    
    print(oblicz(kat_stopnie))

    for kat_stopnie in katy:
        wyniki = oblicz(kat_stopnie)
        print(f"Kąt: {kat_stopnie} stopni")
        for nazwa_funkcji, wartosc in wyniki.items():
            # czy dana wartość typu float jest nieskończoną liczbą dodatnią lub ujemną.
            if not math.isinf(wartosc):
                print(f"{nazwa_funkcji}: {format(wartosc, '.2f')}") 
            else:
                print(f"{nazwa_funkcji}: nieskończoność")
        print()


if __name__ == "__main__":
    
    main()