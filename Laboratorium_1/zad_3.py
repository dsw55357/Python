# 3. Napisz skrypt, za pomocą zadeklarowanych zmiennych, który obliczy ile czasu i kilometrów ma rok świetlny.

rok = 365.25  # Dni w roku
dzien = 24  # Godziny w dobie
godzina = 60  # Minuty w godzinie
minuta = 60  # Sekundy w minucie
# prędokść światła: 300 000 000 m / s
predkosc_swiatla = 299792458  # Metry na sekundę

# Obliczenia
sekundy_w_roku = rok * dzien * godzina * minuta

metry_w_roku_swietlnym = predkosc_swiatla * sekundy_w_roku

kilometry_w_roku_swietlnym = metry_w_roku_swietlnym / 1000

# Wyświetlenie wyników
print(f"Rok świetlny to około {kilometry_w_roku_swietlnym:.2f} kilometrów.")
print(f"Rok świetlny to około {sekundy_w_roku} sekund.")
