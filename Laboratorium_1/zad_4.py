# 4. Napisz skrypt, za pomocą zadeklarowanych zmiennych, który obliczy ile sekund ma godzina, ile
# sekund ma doba, ile sekund ma rok, ile sekund ma twoje życie.

rok = 365.25  # Dni w roku
dzien = 24  # Godziny w dobie
godzina = 60  # Minuty w godzinie
minuta = 60  # Sekundy w minucie


# Obliczenia
sekundy_w_godzinie = godzina * minuta
sekundy_w_dobie = dzien * sekundy_w_godzinie
sekundy_w_roku = rok * sekundy_w_dobie

print(f"Ile sekund w godzinie: {sekundy_w_godzinie}")
print(f"Ile sekund w dobie: {sekundy_w_dobie}")
print(f"Ile sekund w roku: {sekundy_w_roku}")

wiek = 33
sekundy_wiek = wiek * sekundy_w_roku
print(f"Ile sekund ma życie: {sekundy_wiek}")
