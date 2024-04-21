# 7. Napisz program potrafiący rozwiązywać równanie kwadratowe: y = ax2 + bx + c
# źródło: https://pl-static.z-dn.net/files/d0b/aad07fe2fcb53b5077b747a8f95502cf.pdf

import math

"""

Równanie kwadratowe:
ax2 + bx + c = 0 gdzie a != 0 oraz b, c ∈ R

Aby rozwiązać równanie kwadratowe obliczmany wpierw ∆ (delta):
∆ = b2 − 4ac

W zależności od wyniku równanie może mieć dwa, jeden lub zero pierwiastków.
Zatem jeśli:

∆ > 0 Równanie ma dwa pierwiastki :
x1 = (−b−√∆)/2a , x2 = (−b+√∆)/2a

∆ = 0 Równanie ma jeden pierwiastek (podwójny):
x0 = −b/2a

∆ < 0 Równanie ma zero pierwiastków, nie ma rozwiązań.

Pierwiastki równiania ax2 + bx + c = 0 są to miejsca zerowe równiania kwadratowego y = ax2 + bx + c = 0.
Warto dodać, że występują równanie niezupełne to takie gdzie współczynnik b = 0
lub c = 0

źródło: https://pl-static.z-dn.net/files/d0b/aad07fe2fcb53b5077b747a8f95502cf.pdf

"""

def policz_delte(a, b, c):
    """

    Returns:
    Zwraca krotę: dwa pierwiastki lub wiadomość o braku
    """
    # ∆ = b2 − 4ac
    d = b ** 2 - 4 * a * c
    # ∆ > 0 Równanie ma dwa pierwiastki
    if d > 0:
        # dwa pierwiastki
        x1 = (-b - math.sqrt(d)) / ( 2 * a )
        x2 = (-b + math.sqrt(d)) / ( 2 * a )
        print("Równanie ma dwa pierwiastki")
        return (x1, x2)
    elif d == 0:
        #jeden pierwiastek
        x0 = -b / ( 2 * a )
        print("Równanie ma jeden pierwiastek")
        return (x0, x0)
    elif d < 0:
        return ("Równanie nie pierwiastków, nie ma rozwiązań.")


def main():

    # Pobranie współczynników równia
    # ax2 + bx + c = 0
    print("Podaj współczynniki równania kwadratowego: ax2 + bx + c = 0")
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    # Sprawdzenie, czy trójkąt jest prostokątny
    pierwiastki =  policz_delte(a, b, c)  

    # isinstance() takes two parameters:
    #    object - object to be checked
    #    classinfo - class, type, or tuple of classes and types

    if isinstance(pierwiastki, tuple):
        print(f"Pierwiastki równania to: x1 = {pierwiastki[0]:.2f}, x2 = {pierwiastki[1]:.2f}")
    else:
        print(pierwiastki)
    
  
if __name__ == "__main__":

    main()
