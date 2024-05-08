"""

Zadeklaruj krotkę składającą się z 6 elementów znakowych i liczbowych. Wyznacz jej długość.
Sprawdź jej miejsce w pamięci. Dodaj dwa dowolne elementu. Sprawdź po raz drugi jej miejsce
w pamięci. Jakie widzisz zmiany? Skonwertuj krotkę na listę. Jakie widzisz zmiany?

"""

def main():
    t = ('A', 'B', 1, 2, 'ff', 'fe')
    print(t)
    print(f"{len(t)}")
    print(id(t))
    t = t + ('3', '4')
    print(id(t))

    # konwersja krotki na listę
    print(list(t))



if __name__ == "__main__":
    
    main()
