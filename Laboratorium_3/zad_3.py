"""
3. Napisz program wypisujący nieparzyste liczby z zakresu 100 do 200, ale niepodzielne przez 2 i 3
"""

def main():
    for i in range(100, 200):
        if i % 2 != 0 and i % 3 != 0:
            print (i)   


if __name__ == "__main__":

    main()

