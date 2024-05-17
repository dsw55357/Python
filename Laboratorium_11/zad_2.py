"""

Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita.
Napisz program który po podaniu temperatury w stopniach Celsjusza określi
temperaturę w stopniach Fahrenheita i w przypadku zamarzania bądź wrzenia
program wypisze informacje „woda zamarza”, „woda wrze”. Pamiętaj o wyświetlaniu
znaku plus/minus przy temperaturze. Dołącz funkcje odpowiadające za przeliczenie
temperatury Kelwina na Fahrenhaita, Fahrenheita na Kelwina, Kelwina na Celsjusze i
Celsjusze na Kelwina. Czy znasz jeszcze jakieś inne jednostki temperatury?

"""

# Konwertuje temperaturę z stopni Celsjusza na stopnie Fahrenheita.
def celsjusz_na_fahrenheita(celsiusz):

  fahrenheit = (celsiusz * 9/5) + 32

  # Wartość temperatury w stopniach Fahrenheita.
  return fahrenheit

# Konwertuje temperaturę ze stopni Fahrenheita na stopnie Celsjusza.
def fahrenheit_na_celsjusza(fahrenheit):

  celsiusz = (fahrenheit - 32) * 5/9

  # Wartość temperatury w stopniach Celsjusza (float).
  return celsiusz

# Konwertuje temperaturę z Kelwinów na stopnie Fahrenheita.
def kelwin_na_fahrenheita(kelwin):
  
  fahrenheit = (kelwin - 273.15) * 9/5 + 32

  # Wartość temperatury w stopniach Fahrenheita.
  return fahrenheit

# Konwertuje temperaturę ze stopni Fahrenheita na Kelwiny.
def fahrenheit_na_kelwina(fahrenheit):

  kelwin = (fahrenheit - 32) * 5/9 + 273.15
  # Wartość temperatury w Kelwinach.
  return kelwin

# Konwertuje temperaturę z stopni Celsjusza na Kelwiny.
def celsjusz_na_kelwina(celsiusz):
  
  kelwin = celsiusz + 273.15
  # Wartość temperatury w Kelwinach.
  return kelwin

# Konwertuje temperaturę z Kelwinów na stopnie Celsjusza.
def kelwin_na_celsjusza(kelwin):

  celsiusz = kelwin - 273.15
  # Wartość temperatury w stopniach Celsjusza.
  return celsiusz

# Sprawdza stan skupienia wody na podstawie temperatury w stopniach Celsjusza.
def sprawdz_stan_wody(temperatura_celsiusz):
  
  # Informacje o stanie skupienia wody.
  if temperatura_celsiusz < 0:
    return "woda zamarza"
  elif temperatura_celsiusz > 100:
    return "woda wrze"

def main():

    temperatura_celsiusz = float(input("Podaj temperaturę w stopniach Celsjusza: "))

    temperatura_fahrenheit = celsjusz_na_fahrenheita(temperatura_celsiusz)
    temperatura_kelwin = celsjusz_na_kelwina(temperatura_celsiusz)
    print(f"Temperatura w stopniach Fahrenheita: {temperatura_fahrenheit:.2f}")
    print(f"Temperatura w Kelwinach: {temperatura_kelwin:.2f}")

    stan_wody = sprawdz_stan_wody(temperatura_celsiusz)
    if stan_wody:
        print(stan_wody)

if __name__ == "__main__":
    
    main()
