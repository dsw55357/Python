# 5. Napisz skrypt pozwalający przeliczyć cale na centymetry (1 cal = 2.54 cm).

def main():
    cal = 2.54
    # Pobranie liczb od użytkownika
    dlugosc_w_calach = float(input("Podaj długość w calach: "))

    if dlugosc_w_calach < 0:
        print("!! Podana długość nie może być ujemna !!")
        print("!! Spróbuj raz jeszcze !!")
    else:
        dlugosc_w_centymetrach = cal * dlugosc_w_calach
        print(f"Suma: {dlugosc_w_centymetrach}")

if __name__ == "__main__":
  main()
