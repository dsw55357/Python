"""

Korzystając ze słowników stwórz powiązane z sobą dane do logowania typu login i hasło.
Utwórz 6 użytkowników. Napisz warunek, który pozwoli użytkownikowi o loginie i haśle admin,
admin dostać się na „brzydką” stronę internetową zwaną panelem admina. Reszta
użytkowników powinna otrzymać dostęp do innej strony.

"""

uzytkownicy = {
    "admin": "admin",
    "anowak": "admin123",
    "kwisniewski": "admin123",
    "mdabrowska": "admin123",
    "pgorski": "admin123",
}


def main():

    # Pobranie danych logowania od użytkownika
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")

    if login in uzytkownicy and uzytkownicy[login] == haslo:
        if login == "admin":
            print("Zalogowano jako administrator. Dostęp do panelu admina:")
            for l in range(3):
                print("*")
        else:
            print(f"Zalogowano jako {login}. Dostęp do strony użytkownika:")
            for l in range(3):
                print("#")
    else:
        print("Niepoprawny login lub hasło.")


if __name__ == "__main__":
    
    main()