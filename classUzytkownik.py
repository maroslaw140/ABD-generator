import cx_Oracle
import funkcje
import random


class Uzytkownik:
    def __init__(self, kursor):
        self.kursor = kursor
        self.pracownicy_fk = []
        self.klienci_fk = []
        self.status_uzytkownika_fk = []
        self.dane_do_wstawienia = []

        self.nazwa_tabeli = "uzytkownik"
        self.insert = """INSERT INTO uzytkownik (login, haslo, id_pracownik, id_klient, id_status_uzytkownika, data_rejestracji) VALUES ('{login}', '{haslo}', '{id_pracownik}', '{id_klient}', '{id_status_uzytkownika}', '{data_rejestracji}')"""

    def pobierz_pracownicy_fk(self):
        try:
            self.kursor.execute(
                "SELECT DISTINCT id_pracownik FROM pracownik MINUS SELECT DISTINCT id_pracownik FROM uzytkownik")
            self.pracownicy_fk = [id_pracownik[0] for id_pracownik in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_klienci_fk(self):
        try:
            self.kursor.execute("SELECT DISTINCT id_klient FROM klient MINUS SELECT DISTINCT id_klient FROM uzytkownik")
            self.klienci_fk = [id_klient[0] for id_klient in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_status_uzytkownika_fk(self):
        try:
            self.kursor.execute("SELECT id_status_uzytkownika FROM status_uzytkownika")
            self.status_uzytkownika_fk = [id_status_uzytkownika[0] for id_status_uzytkownika in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):

                if self.klienci_fk and self.pracownicy_fk:
                    typ = random.choice(["klient", "pracownik"])
                elif self.klienci_fk:
                    typ = "klient"
                elif self.pracownicy_fk:
                    typ = "pracownik"
                else:
                    print("Nie ma już dostępnych klientów ani pracowników.")
                    break

                if typ == "klient":
                    id_pracownik = None
                    id_klient = random.choice(self.klienci_fk)
                    self.klienci_fk.remove(id_klient)
                elif typ == "pracownik":
                    id_pracownik = random.choice(self.pracownicy_fk)
                    id_klient = None
                    self.pracownicy_fk.remove(id_pracownik)
                else:
                    continue

                uzytkownik = {
                    'login': funkcje.losowy_ciag(20, False, True),
                    'haslo': funkcje.losowy_ciag(255, False, True),
                    'id_pracownik': id_pracownik,
                    'id_klient': id_klient,
                    'id_status_uzytkownika': random.randint(1, 5),
                    'data_rejestracji': funkcje.generuj_date()
                }
                self.dane_do_wstawienia.append(uzytkownik)

            self.kursor.executemany("""
                                INSERT INTO uzytkownik (login, haslo, id_pracownik, id_klient, id_status_uzytkownika, data_rejestracji)
                                VALUES (:login, :haslo, :id_pracownik, :id_klient, :id_status_uzytkownika, :data_rejestracji)""",
                                    self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()

    def wstaw_dane(self, liczba_danych=1):
        try:
            self.pobierz_pracownicy_fk()
            self.pobierz_klienci_fk()
            self.pobierz_status_uzytkownika_fk()
            self.generuj_dane(liczba_danych)

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
