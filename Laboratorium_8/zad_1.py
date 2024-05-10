"""

Korzystając ze słowników stwórz menu restauracji. Dodaj do niej 10 pozycji razem z cenami.
Za pomocą pętli for wypisz: wartości, klucze, klucze i wartości. W menu restauracji usuń
element o najniższej cenie oraz o największej. Dodaj możliwość dodania nowej pozycji do
słownika np. pizza hawajska z ceną 19.99 zł.

"""

def main():

    menu = {
        "Zupa pomidorowa z bazylią" : 	9.99,
        "Kotlet schabowy z ziemniakami i surówką" :	17.50,
        "Spaghetti carbonara" :	16.90,
        "Pieczeń z kurczaka z ryżem i warzywami" :	22.00,
        "Sałatka grecka" :	14.50,
        "Burgery wołowe (2 szt.) z frytkami" :	25.00,
        "Placki ziemniaczane z gulaszem" :	18.90,
        "Filet z łososia z brokułami i sosem holenderskim" :	29.90,
        "Pizza Margherita" :	19.99,
        "Tiramisu" :	12.50,
    }


    print("menu\n")

    print("\n tylko wartość")
    for v in menu.values():
        print(f"{v}")

    
    print("\n tylko klucz")
    for k in menu:
        print(f"{k}")

    print("\n")
    print("klucz z wartością")
    for k, v in menu.items():
        print(f"{k}: {v}")

    print("\n")

    min_cena = min(menu.values())
    print(f"min cena: {min_cena}")
    for k, v in menu.items():
        if v == min_cena:
            del menu[k]
            break

    max_cena = max(menu.values())
    print(f"max cena: {max_cena}")
    for k, v in menu.items():
        if v == max_cena:
            del menu[k]
            break

    print(f"\n {menu}")

    nowa_pozycja = "pizza hawajska "
    cena = 19.99

    menu[nowa_pozycja] = cena

    print(f"\n {menu}")


if __name__ == "__main__":
    
    main()
