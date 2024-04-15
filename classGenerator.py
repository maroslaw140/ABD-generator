import cx_Oracle
from dotenv import load_dotenv
import os

from classAdres import Adres
from classAutor import Autor
from classKategoria import Kategoria
from classKlient import Klient
from classKsiazka import Ksiazka
from classOpinia import Opinia
from classPracownik import Pracownik
from classRachunek import Rachunek
from classSeria import Seria
from classStanowisko import Stanowisko
from classUzytkownik import Uzytkownik
from classWydanie import Wydanie
from classWydawnictwo import Wydawnictwo
from classZamowienie import Zamowienie
from classZamowieniePozycja import ZamowieniePozycja


class Generator:

    def __init__(self):
        self.kursor = None
        self.plik = "plik.txt"
        self.tabele = [Kategoria, Seria, Autor, Adres, Stanowisko, Wydawnictwo, Pracownik, Klient, Uzytkownik, Ksiazka, Wydanie, Opinia, Zamowienie, Rachunek, ZamowieniePozycja]

    def polacz(self):
        try:
            load_dotenv()

            dsn = cx_Oracle.makedsn(host=os.getenv("db_host"), port=os.getenv("db_port"), service_name=os.getenv("db_service"))
            connection = cx_Oracle.connect(user=os.getenv("db_user"), password=os.getenv("db_password"), dsn=dsn)
            self.kursor = connection.cursor()
            print("Połączono z bazą")
        except cx_Oracle.Error as error:
            print(error)

    def zapisz_insert_do_pliku(self, insert, dane_do_wstawienia):
        try:
            with open(self.plik, "a") as file:
                for dane in dane_do_wstawienia:
                    linia_insert = insert.format(**dane)
                    if linia_insert[-1] != ';':
                        linia_insert += ';'
                    linia_insert += "\n"
                    file.write(linia_insert)
        except IOError as error:
            print("Błąd zapisu do pliku:", error)


    def uruchom(self):
        print("Wybierz opcję:")
        print("1. Dodaj do wszystkich tabel")
        print("2. Dodaj do jednej tabeli")
        wybor = input("Twój wybór: ")

        if wybor == '1':
            self.dodaj_do_wszystkich_tabel()
        elif wybor == '2':
            self.dodaj_do_jednej_tabeli()
        else:
            print("Niepoprawny wybór.")

    def dodaj_do_wszystkich_tabel(self):
        liczba_danych = int(input("Podaj ilość rekordów do wstawienia: "))
        for tabela in self.tabele:
            tabela = tabela(self.kursor)
            tabela.wstaw_dane(liczba_danych)
            print(f"{tabela.nazwa_tabeli} - wstawiono {tabela.kursor.rowcount} rekordów.")
            self.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

    def dodaj_do_jednej_tabeli(self):
        print("Wybierz tabelę:")
        print("1. Kategoria")
        print("2. Seria")
        # Dodaj pozostałe opcje wyboru tabeli
        wybor_tabeli = input("Twój wybór: ")

        if wybor_tabeli == '1':
            tabela = Kategoria
        elif wybor_tabeli == '2':
            tabela = Seria
        elif wybor_tabeli == '3':
            tabela = Ksiazka
        elif wybor_tabeli == '4':
            tabela = Uzytkownik
        else:
            print("Niepoprawny wybór tabeli.")
            return

        liczba_danych = int(input("Podaj ilość rekordów do wstawienia: "))
        tabela = tabela(self.kursor)
        tabela.wstaw_dane(liczba_danych)
        print(f"{tabela.nazwa_tabeli} - wstawiono {tabela.kursor.rowcount} rekordów.")
        self.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)