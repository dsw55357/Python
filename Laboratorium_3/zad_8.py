"""

Program, który wypisze największą liczbę niepodzielną przez 2,3,5,7 ale mniejszą od
1000.

"""

def max_liczba_niepodzielna():
    for i in range(1000-1, 0, -1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            return i


def main():

    print(f"największą liczbę niepodzielną : {max_liczba_niepodzielna()}")
            
if __name__ == "__main__":
        main()
