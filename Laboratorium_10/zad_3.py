"""

Dysponując łańcuchem znaków: "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'.", 
zwróć wycinek obejmujący znaki od początku do pierwszej kropki. 
Następnie dysponując listą ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."], 
przekształć ją w poprawne gramatycznie zdanie. Pomiędzy poszczególnymi słowami zdania mają być umieszczone odstępy, lecz nie ma być odstępu pomiędzy ostatnim słowem i kropką.

"""

tekst = f"Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."

def main():

    pierwsza_kropka = tekst.find(".")
    print(pierwsza_kropka)

    wycinek = tekst[:pierwsza_kropka + 1]

    print(wycinek)

    slowa = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]
    zdanie = " ".join(slowa)[:-2] + "." # Usuń odstępu z kropką i dodaj kropkę ;)

    print(zdanie)

if __name__ == "__main__":
    
    main()
