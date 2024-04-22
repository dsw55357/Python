"""

3. Napisz program, który porówna ze sobą 3 liczby i wskaże, która jest większa i czy liczby są identyczne. Zastanów się nad opcją zagnieżdżania ifów.

"""

a = float(input("Podaj liczbę a:"))
b = float(input("Podaj liczbę b:"))
c = float(input("Podaj liczbę c:"))

if a == b:
    print("Liczby są równe : a = b")
elif a == c:
    print("Liczby są równe : a = c")
elif b == c:
    print("Liczby są równe : b = c")
elif a < b:
    if b > c:
        print("b - liczba największa")
    elif a < c:
        print("c - liczba największa")
elif a > b:
    if a > c:
        print("a - liczba największa")
    elif b < c:
        print("c - liczba największa")
