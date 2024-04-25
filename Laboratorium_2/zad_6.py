"""
6. Napisz program, który spośród czterech podanych przez użytkownika liczb wybierze największą z nich i wypisze ją na ekranie. Spróbuj przewidzieć wszystkie trudne kombinacje liczb a,b,c i d. Czy może być problem w którymś z przypadków?

"""

def main():
    a = float(input("Podaj liczbę a:"))
    b = float(input("Podaj liczbę b:"))
    c = float(input("Podaj liczbę c:"))
    d = float(input("Podaj liczbę d:"))

    if a > b:
        if c > d:
            if a > c:
                print("a jest największe")
            else:
                print("c jest największe")
        elif d > c:
            if a > d:
                print("a jest największe")
            else:
                print("d jest największe")
    if b > a:
        if d > c:
            if b > d:
                print("b jest największe")
            else:
                print("d jest największe")
        elif c > d:
            if b > c:
                print("b jest największe")
            else:
                print("c jest największe")
    

if __name__ == "__main__":

    main()
