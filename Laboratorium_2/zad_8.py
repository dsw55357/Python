# 8. Napisz program, który poprosi o podanie trzech długości boków trójkąta
# i sprawdzi czy jest on prostokątny.

"""

Twierdzenie: Pitagorasa
Jeżeli trójkąt jest prostokątny, to suma kwadratów długości jego przyprostokątnych jest
równa kwadratowi długości jego przeciwprostokątnej.

"""

def czy_jest_prostokatny(a, b, c):
    
    """
    Sprawdza, czy podane długości boków a, b i c tworzą trójkąt prostokątny.
    
    Args:
      a: Długość pierwszego boku.
      b: Długość drugiego boku.
      c: Długość trzeciego boku.
    
    Returns:
      True, jeśli trójkąt jest prostokątny, False w przeciwnym przypadku.
    """
    # Sortowanie boków rosnąco
    boki = sorted([a, b, c])

    # Sprawdzenie twierdzenia Pitagorasa
    return boki[0] ** 2 + boki[1] ** 2 == boki[2] ** 2


def main():

    # Pobranie długości boków od użytkownika
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    # Sprawdzenie, czy trójkąt jest prostokątny
    if czy_jest_prostokatny(a, b, c):
        print("Podane długości boków tworzą trójkąt prostokątny.")
    else:
        print("Podane długości boków nie tworzą trójkąta prostokątnego.")
  
if __name__ == "__main__":

    main()
