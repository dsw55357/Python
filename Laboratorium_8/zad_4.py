"""

Korzystając ze słowników stwórz listę mailingową o nazwie „serniczkowy spam”. Zadaniem tej listy jest gromadzenie adresów e-mail do wszystkich chętnych, którzy chcą codziennie
otrzymać na swoją skrzynkę pocztową zdjęcie np. serniczka na zimno. Zaproponuj w jaki
sposób przekazać te dane do innych aplikacji, systemów w celu zautomatyzowania procesu
wysyłania spamu.

"""

import csv
import os
from time import sleep

# list of column names
lista_kolum = ['id', 'user', 'email']

def czytaj_baze():

    with open("zad_4.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        baza = [row for row in csv_reader]

        file.close()

    return baza

def aktualizauj_baze(rekord):

    with open("zad_4.csv", "a", newline='') as file:
        dictwriter_object = csv.DictWriter(file, fieldnames=lista_kolum)
        
        dictwriter_object.writerow(rekord)
 
        # Close the file object
        file.close()

def symulacja_wyslania(user, mail):
    
    print(f"{user}, {mail}", end="")
    sleep(1)
    print("")

def rozeslij_dane(record):   
    #print(record)
    slownik = { k : v for k, v in record.items()}
    #print(f"{slownik['user']} : {slownik['email']}")

    symulacja_wyslania(slownik['user'], slownik['email'])

def ile_rekordow_bazie():
    liczba_rekordow = 0
    with open('zad_4.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            liczba_rekordow += 1
    return liczba_rekordow

def dodaj_klienta_do_bazy(zbior):
    # Clearing the Screen
    os.system('clear')
    print("Dodaj klienta do listy mailingowej")

    user = input(f"Podaj nazwę urzytkownika: ")
    email = input(f"Podaj adres email: ")

    rekord = {}
    rekord['id'] = ile_rekordow_bazie()
    rekord['user'] = user
    rekord['email'] = email

    print(rekord)
    aktualizauj_baze(rekord)

    print(f"Użytkownik dodany do bazy: {user} : {email}")
    print("Proszę czekać...")
    sleep(2)

def rozeslij_wiadomosc():
    os.system('clear')
    zbior = czytaj_baze()
    for record in zbior:
        rozeslij_dane(record)
    print("\nDone")

def wyswietl_menu():
    os.system('clear') 
    print("\nLista mailingowa:")
    print("1. Dodaj klienta do bazy - 1")
    print("2. Roześlij wiadomość    - 2")
    print("0. Wyjście")

def wybierz_opcje():
    
    while True:
        opcja = int(input("Wybierz opcję: "))
        if 0 <= opcja <= 2:
            return opcja
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie")

if __name__ == "__main__":

    zbior = czytaj_baze()

    while True:
        wyswietl_menu()
        opcja = wybierz_opcje()
    
        if opcja == 0:
            break
        elif opcja == 1:
            dodaj_klienta_do_bazy(zbior)
        elif opcja == 2:
            rozeslij_wiadomosc()
            sleep(1)

"""

Propozycje przekazania danych do innych aplikacji:

Baza danych: Możesz przechowywać listę subskrybentów w bazie danych, do której inne aplikacje lub systemy mogą uzyskiwać dostęp za pomocą zapytań SQL.

API: Możesz stworzyć API RESTful, które udostępnia punkty końcowe do dodawania, usuwania i pobierania subskrybentów z listy mailingowej. Inne aplikacje lub systemy mogą wykorzystywać to API do integracji z listą mailingową.

Użycie brokera do przesyłania wiadomości, np.: RabbitMQ 
Dostępne są biblioteki klienckie dla Pythona, takie jak pika i aioamqp

"""