import sys

def dzielenie_modulo(liczba, dzielnik):
  """Funkcja wykonująca dzielenie modulo z zabezpieczeniem przed błędami."""
  try:
    wynik = liczba % dzielnik
    print(f"{liczba} % {dzielnik} = {wynik}")
  except ZeroDivisionError:
    print(f"Dzielenie przez 0 jest niedozwolone: {liczba} % {dzielnik}")
  except NameError:
    print(f"Nie zdefiniowano 'największej liczby': {liczba} % największa_liczba")

# Przykłady dzielenia modulo
dzielenie_modulo(1, 1)
dzielenie_modulo(1, 69)
dzielenie_modulo(69, 666)
dzielenie_modulo(10000, 10000)
dzielenie_modulo(10000, sys.maxsize)

# With modern Python, you don't have to worry about reaching a maximum integer
# size. Just make sure you have enough memory to handle the computation of very
# large integer operations, and you're good to go.
# The largest pos integer is maxint
max_int = sys.maxsize*7809356576809509573609874689576897365487536545894358723468
print(f"Max wartość int: {max_int}")
# The largest negative integer is -maxint-1
min_int = (-sys.maxsize-1)*78093565768095095736098746895768973654875365458943587234681111111111111111111111111111111
print(f"Min wartość int: {min_int}")

dzielenie_modulo(10000, max_int)
dzielenie_modulo(10000, min_int)

# The maximum float value:
print(sys.float_info.max)
dzielenie_modulo(10000, sys.float_info.max)
# The minimum float value:
print(sys.float_info.min)
dzielenie_modulo(10000, sys.float_info.min)

