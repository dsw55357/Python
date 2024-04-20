# start

def main():
  """Funkcja główna programu."""
  # Pobranie liczb od użytkownika
  liczba1 = float(input("Podaj pierwszą liczbę: "))
  liczba2 = float(input("Podaj drugą liczbę: "))

  # Obliczenie sumy
  suma = liczba1 + liczba2
  print(f"Suma: {suma}")

  # Obliczenie różnicy
  roznica = liczba1 - liczba2
  print(f"Różnica: {roznica}")

  # Obliczenie iloczynu
  iloczyn = liczba1 * liczba2
  print(f"Iloczyn: {iloczyn}")

  # Obliczenie ilorazu (jeśli druga liczba nie jest zerem)
  try:
    iloraz = liczba1 / liczba2
    print(f"Iloraz: {iloraz}")
  except ZeroDivisionError:
    print("Nie można obliczyć ilorazu, druga liczba jest równa 0.")


if __name__ == "__main__":
  main()
