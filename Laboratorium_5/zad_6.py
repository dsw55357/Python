"""

Napisz program, który będzie interpretacją gry w ”Za dużo, za mało”. Program losuje liczbę z
zakresu 1...100, a gracz (użytkownik) ma za zadanie odgadnąć, co to za liczba poprzez
podawanie kolejnych wartości. Użytkownik ma 3 szanse. Jeżeli podana wartość jest:
• większa – wyświetlany jest komunikat „Podałeś za dużą wartość”,
• mniejsza – wyświetlany jest komunikat „Podałeś za małą wartość”,
• identyczna z wylosowaną – wyświetlany jest komunikat „Gratulacje” i gra się kończy.
• Jeśli po 3 próbach użytkownik nie podał poprawnej wartości program ma przerwać działanie i wyświetlić komunikat – „Haha przegrałeś!”

"""

import random

def main():

    liczba = random.randint(1, 100)     
    i = 1
    print(liczba)
    while i <= 3:
        n = int(input(f"Próba: {i} - Podaj liczb: "))
        i += 1
        if n > liczba:
            print("Podałeś za dużą liczbę")           
        if n < liczba:
            print("Podałeś za małą liczbę")
        if n == liczba:
            print("Gratulacje")
            break
        if i > 3:
            print(f"Haha przegrałeś! Wylosowana liczba to {liczba}")
            break

if __name__ == "__main__":
    
    main()