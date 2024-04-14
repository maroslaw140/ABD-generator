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

    def pobierz_pracownicy_fk(self):
        try:
            self.kursor.execute("SELECT DISTINCT id_pracownik FROM pracownik EXCEPT SELECT DISTINCT id_pracownik FROM uzytkowik")
            self.pracownicy_fk = [id_pracownik[0] for id_pracownik in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_klienci_fk(self):
        try:
            self.kursor.execute("SELECT DISTINCT id_klient FROM klient EXCEPT SELECT DISTINCT id_klient FROM uzytkowik")
            self.klienci_fk = [id_klient[0] for id_klient in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_status_uzytkownika_fk(self):
        try:
            self.kursor.execute("SELECT DISTINCT id_status_uzytkownika FROM status_uzytkownika")
            self.status_uzytkownika_fk = [id_status_uzytkownika[0] for id_status_uzytkownika in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):

                typ = random.choice(["klient", "pracownik"])

                if typ == "klient" and self.klienci_fk:
                    id_pracownik = None

                    id_klient = random.choice(self.klienci_fk)
                    self.klienci_fk.remove(id_klient)
                elif typ == "pracownik" and self.pracownicy_fk:
                    id_pracownik = random.choice(self.pracownicy_fk)
                    id_pracownik = random.choice(self.pracownicy_fk)

                    id_klient = None
                else:
                    continue

                uzytkownik = {
                    'login': funkcje.losowy_ciag(20, False, True),
                    'haslo': funkcje.losowy_ciag(255, False, True),
                    'id_pracownik': id_pracownik,
                    'id_klient': id_klient,
                    'id_status_uzytkownika': random.choice(self.status_uzytkownika_fk),
                    'data_rejestracji': funkcje.generuj_date()
                }
                self.dane_do_wstawienia.append(uzytkownik)

            self.kursor.executemany("""
                                INSERT INTO uzytkownik (login, haslo, id_pracownik, id_klient, id_status_uzytkownika, data_rejestracji)
                                VALUES (:login, :haslo, :id_pracownik, :id_klient, :id_status_uzytkownika, :data_rejestracji)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
