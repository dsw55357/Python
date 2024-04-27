"""
4. Napisz program wypisujący parzyste liczby z zakresu 100 do 200, ale niepodzielne przez 5,6 i 11.
"""

def main():
    for i in range(100, 201):
        if i % 2 == 0 and i % 5 != 0 and i % 6 != 0 and i % 11 != 0:
            print (i)   


if __name__ == "__main__":

    main()