"""

Program który zapyta użytkownika o imię, nazwisko, numer telefonu oraz
buta, a następnie: sprawdź czy imię i nazwisko składają się tylko z liter, a nr telefonu i
numer buta składa się wyłącznie z cyfr (wyświetl tę informację jako true/false).Sprawdź
czy imię i nazwisko rozpoczyna się z dużej litery. Jeśli nie popraw ich.Sprawdź czy numer
telefonu oraz buta zawiera dziwne znaki np. myślniki. Usuń ich. Zakładając, że twoi
użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą. Uważaj na
przypadki np.Nel, Barnaba. Zastosuj odpowiednie formatowanie przy użyciu f-stringów.

"""

"""Sprawdza, czy imię i nazwisko składają się tylko z liter."""
def sprawdz_imie_nazwisko(imie_nazwisko):

  for znak in imie_nazwisko:
    if not znak.isalpha() and znak != " ":
      return False
  return True


"""Sprawdza, czy numer (telefonu lub buta) składa się tylko z cyfr."""
def sprawdz_numer(numer, typ):

  dozwolone_znaki = {
    "telefon": set("0123456789"),
    "but": set("0123456789"),
  }

  for znak in numer:
    if znak not in dozwolone_znaki:
      return False
  return True

"""Poprawia wielkość pierwszej litery imienia i nazwiska."""
def popraw_duze_litery(imie_nazwisko):
  
  return imie_nazwisko.title()

"""Usuwa dziwne znaki z numeru."""
def usun_dziwne_znaki(numer):
  
  dozwolone_znaki = "0123456789"
  wyczyszczony_numer = ""
  for znak in numer:
    if znak in dozwolone_znaki:
      wyczyszczony_numer += znak
  return wyczyszczony_numer

def sprawdz_plec(imie_nazwisko):

  imie = imie_nazwisko.split()[0] # Pobierz pierwsze imię

  imiona_zenskie = ["nel" ]
  imiona_meskie = ["barnaba" ]

#endswith(str
  #if imie[-1].lower() == "a" and imie.lower() != imiona_meskie[0].lower() or imie.lower() == imiona_zenskie[0].lower():
  if imie.endswith('a') and imie.lower() != imiona_meskie[0].lower() or imie.lower() == imiona_zenskie[0].lower():
    return "kobieta"
  else:
    return "mężczyzna"

# Wyświetl wyniki
def wyswietl_wynik(wynik):
  print("")

  for k, v in wynik.items():
        print(f"{k}: {v}")

# Sprawdź poprawność danych
def sprawdz_poprawnosc_danych(dane):
  
  wynik = {}
  wynik["imie_nazwisko"] = sprawdz_imie_nazwisko(dane["imie_nazwisko"])
  wynik["numer_telefonu"] = sprawdz_numer(dane["numer_telefonu"], "telefon")
  wynik["numer_buta"] = sprawdz_numer(dane["numer_buta"], "but")

  wynik["imie_nazwisko_z_duzymi_literami:"] = popraw_duze_litery(dane["imie_nazwisko"])
  wynik["numer_telefonu_bez_znakow"] = usun_dziwne_znaki(dane["numer_telefonu"])
  wynik["numer_buta_bez_znakow"] = usun_dziwne_znaki(dane["numer_buta"])

  wynik["plec"] = sprawdz_plec(dane["imie_nazwisko"])

  wyswietl_wynik(wynik)

def main():

  dane = {}
  # Pobierz dane od użytkownika

  dane["imie_nazwisko"] = input("Podaj imię i nazwisko: ")
  dane["numer_telefonu"] = input("Podaj numer telefonu: ")
  dane["numer_buta"] = input("Podaj numer buta: ")

  sprawdz_poprawnosc_danych(dane)


if __name__ == "__main__":
    
    main()