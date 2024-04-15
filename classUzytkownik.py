import cx_Oracle
import funkcje
import random


class Uzytkownik:
    def __init__(self, kursor):
        self.kursor = kursor
        self.pracownicy_fk = []
        self.klienci_fk = []
        self.status_uzytkownika_fk = []
        self.loginy = []
        self.dane_do_wstawienia = []

        self.nazwa_tabeli = "uzytkownik"
        self.insert = """INSERT INTO uzytkownik (login, haslo, id_klient, id_status_uzytkownika, data_rejestracji) VALUES ('{login}', '{haslo}', '{id_klient}', '{id_status_uzytkownika}', '{data_rejestracji}')"""

    def pobierz_pracownicy_fk(self):
        try:
            self.kursor.execute(
                "SELECT id_pracownik FROM pracownik MINUS SELECT id_pracownik FROM uzytkownik WHERE id_pracownik IS NOT NULL")
            self.pracownicy_fk = [id_pracownik[0] for id_pracownik in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_klienci_fk(self):
        try:
            self.kursor.execute("SELECT id_klient FROM klient MINUS SELECT id_klient FROM uzytkownik WHERE id_klient IS NOT NULL")
            self.klienci_fk = [id_klient[0] for id_klient in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_status_uzytkownika_fk(self):
        try:
            self.kursor.execute("SELECT id_status_uzytkownika AS status FROM status_uzytkownika")
            self.status_uzytkownika_fk = [status[0] for status in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_loginy(self):
        try:
            self.kursor.execute("SELECT login FROM uzytkownik")
            self.loginy = [login[0] for login in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for i in range(liczba_danych):

                login = funkcje.losowy_ciag(20, False, True)

                while login in self.loginy:
                    login = funkcje.losowy_ciag(20, False, True)

                self.loginy.append(login)

                if self.klienci_fk and i < len(self.klienci_fk):
                    id_klient = self.klienci_fk[i]
                else:
                    print("Nie ma już dostępnych klientów ani pracowników bez konta.")
                    break

                uzytkownik = {
                    'login': login,
                    'haslo': funkcje.losowy_ciag(255, False, True),
                    'id_klient': id_klient,
                    'id_status_uzytkownika': random.choice(self.status_uzytkownika_fk),
                    'data_rejestracji': funkcje.generuj_date()
                }

                self.dane_do_wstawienia.append(uzytkownik)

            self.kursor.executemany("""
                                INSERT INTO uzytkownik (login, haslo, id_klient, id_status_uzytkownika, data_rejestracji)
                                VALUES (:login, :haslo, :id_klient, :id_status_uzytkownika, :data_rejestracji)""",
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
            self.pobierz_loginy()
            self.generuj_dane(liczba_danych)

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
