"""

1. Napisz program, który wypisze liczby podzielne przez 8 ( w zakresie 1..100)

"""

def main():
    for i in range(1, 100):
        if i % 8 == 0:
            print (i)   


if __name__ == "__main__":

    main()