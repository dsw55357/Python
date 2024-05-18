"""

Program na przeliczanie wysokości podanej w stopach i calach na wysokość w metrach, centymetrach, milimetrach i kilometrach. Zaproponuj przeliczanie na inne dziwne miary długości.

"""

def inne_jednostki(metry, jednostka):

    if jednostka == "cm":
        return metry * 100
    elif jednostka == "mm":
        return metry * 1000
    elif jednostka == "km":
        return metry / 1000
    elif jednostka == "mila":
        return metry * 0.00621371    
    elif jednostka == "yard":
        return metry * 1.09361   


def main():

    # metry = ft * 0.3048 + in * 2.54 = 2.54 * ( 12 * ft + in)
    # 1 stopa ma 12 cali stąd 12∗ft 

    print("John ma 5 stóp i 11 cali wzrostu (wzrost 5’11”), ile to metrów ?")

    john_ft = 5
    john_in = 11
    metry = john_ft * 0.3048 + john_in * 0.0254

    print(f"John ma {metry:.2f} m")

    centymetry = inne_jednostki(metry, "cm")
    print(f"{metry:.2f} metra to {centymetry:.2f} centymetrów.")

    milimetry = inne_jednostki(metry, "mm")
    print(f"{metry:.2f} metra to {milimetry:.2f} milimetrów.")

    kilometry = inne_jednostki(metry, "km")
    print(f"{metry:.2f} metra to {kilometry:.5f} kilometrów.")

    # 1 mile = 1,609 km ( mila )
    mila = inne_jednostki(metry, "mila")
    print(f"{metry:.2f} metra to {mila:.5f} mil.")

    # 1 yard = 91,44 cm ( jard )
    yard = inne_jednostki(metry, "yard")
    print(f"{metry:.2f} metra to {yard:.5f} jardów.")



if __name__ == "__main__":
    
    main()
