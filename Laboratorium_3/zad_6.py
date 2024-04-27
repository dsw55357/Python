"""

6. Program wyświetlający trójkąt prostokątny z gwiazdek (*, **, *** itp.). W „podstawie”
ma być 5 gwiazdek nie 8

"""

"""
posłużymy się równaniem funkcji: y = a*x + b
przekszałcimy funkcję do postaci: x = (y - b)/a
przyjmieny parametry: a=-2, b=50

"""

def main():
    a=-2
    b=50
    # zaczynamy od góry, aby w podstawie był krótszy bok
    for y in range(b, 1, -1):
        x = int((y - b)/a)
        for j in range(1, x):
            print("*", end="")
        print()

if __name__ == "__main__":

    main()