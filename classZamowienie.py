import random
import cx_Oracle
import funkcje


class Zamowienie:
    def __init__(self, kursor):
        self.kursor = kursor
        self.klienci_fk = []
        self.adresy_fk = []
        self.pracownicy_fk = []
        self.sposoby_dostawy_fk = []
        self.statusy_zamowienia_fk = []
        self.dane_do_wstawienia = []

        self.nazwa_tabeli = "zamowienie"
        self.insert = """INSERT INTO zamowienie (id_klient, id_adres, data_zamowienia, data_realizacji, data_wyslania, id_pracownik_realizujacy, id_sposob_dostawy, id_status_zamowienia) VALUES ('{id_klient}', '{id_adres}', '{data_zamowienia}', '{data_realizacji}', '{data_wyslania}', '{id_pracownik_realizujacy}', '{id_sposob_dostawy}', '{id_status_zamowienia}')"""

    def pobierz_klienci_fk(self):
        try:
            self.kursor.execute("SELECT id_klient FROM klient")
            self.klienci_fk = [id_klient[0] for id_klient in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_adresy_fk(self):
        try:
            self.kursor.execute("SELECT id_adres FROM adres")
            self.adresy_fk = [id_adres[0] for id_adres in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_pracownicy_fk(self):
        try:
            self.kursor.execute("SELECT id_pracownik FROM pracownik")
            self.pracownicy_fk = [id_pracownik[0] for id_pracownik in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_sposoby_dostawy_fk(self):
        try:
            self.kursor.execute("SELECT id_sposob_dostawy FROM sposob_dostawy")
            self.sposoby_dostawy_fk = [id_sposob_dostawy[0] for id_sposob_dostawy in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_statusy_zamowienia_fk(self):
        try:
            self.kursor.execute("SELECT id_status_zamowienia AS status FROM status_zamowienia")
            self.statusy_zamowienia_fk = [status[0] for status in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                data_zamowienia = funkcje.generuj_date(100)
                data_realizacji = funkcje.generuj_date(50)
                data_wyslania = funkcje.generuj_date(1)

                zamowienie = {
                    'id_klient': random.choice(self.klienci_fk),
                    'id_adres': random.choice(self.adresy_fk),
                    'data_zamowienia': data_zamowienia,
                    'data_realizacji': data_realizacji,
                    'data_wyslania': data_wyslania,
                    'id_pracownik_realizujacy': random.choice(self.pracownicy_fk),
                    'id_sposob_dostawy': random.choice(self.sposoby_dostawy_fk),
                    'id_status_zamowienia': random.choice(self.statusy_zamowienia_fk),
                }
                self.dane_do_wstawienia.append(zamowienie)

            self.kursor.executemany("""
                                INSERT INTO zamowienie (id_klient, id_adres, data_zamowienia, data_realizacji, data_wyslania, id_pracownik_realizujacy, id_sposob_dostawy, id_status_zamowienia)
                                VALUES (:id_klient, :id_adres, :data_zamowienia, :data_realizacji, :data_wyslania, :id_pracownik_realizujacy, :id_sposob_dostawy, :id_status_zamowienia)""",
                                    self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()

    def wstaw_dane(self, liczba_danych=1):
        try:
            self.pobierz_klienci_fk()
            self.pobierz_adresy_fk()
            self.pobierz_pracownicy_fk()
            self.pobierz_sposoby_dostawy_fk()
            self.pobierz_statusy_zamowienia_fk()
            self.generuj_dane(liczba_danych)

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
