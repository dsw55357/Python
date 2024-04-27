"""

5. Program, który wyznaczy silnię.

"""

def silnia(n):
  if n == 0:
    return 1
  else:
    silnia = 1
    for i in range(1, n + 1):
      silnia *= i
    return silnia

def main():
  liczba = int(input("Podaj liczbę: "))
  silnia_liczby = silnia(liczba)
  print(f"Silnia liczby {liczba} to: {silnia_liczby}")

if __name__ == "__main__":

    main()