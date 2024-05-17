"""

Oblicz ile metrów kwadratowych mają ściany i sufit pokoju (dla uproszczenia bez drzwi i okien:)) o wymiarach 3m x 5m i wysokości 2.5m? Jak zmieni się wynik kiedy przyjmiemy standardowe wymiary drzwi i okien?

"""

def main():

    wys = 2.5
    szer = 3.0
    dl = 5.0

    sciana_1 = dl * wys  
    sciana_2 = szer * wys

    sufit = szer * dl

    pow_calkowita = 2 * ( sciana_1 + sciana_2 ) + sufit

    print(f"Powierzchnia bez okien i drzwi: {pow_calkowita} m^2")

    drzwi = 0.8 * 2.0
    okno = 1.5 * 1

    pow_calkowita = pow_calkowita - drzwi - 2 * okno

    print(f"Powierzchnia z uwzględnieniem okien i drzwi: {pow_calkowita} m^2")

if __name__ == "__main__":
    
    main()







