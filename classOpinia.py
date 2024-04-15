import random
import cx_Oracle
import funkcje


class Opinia:
    def __init__(self, kursor):
        self.kursor = kursor
        self.wydania_fk = []
        self.klienci_fk = []
        self.dane_do_wstawienia = []

        self.nazwa_tabeli = "opinia"
        self.insert = """INSERT INTO opinia (id_wydanie, id_klient, tresc, ocena, data_wystawienia) VALUES (:id_wydanie, :id_klient, '{tresc}', {ocena}, '{data_wystawienia}')"""

    def pobierz_wydania_fk(self):
        try:
            self.kursor.execute("SELECT id_wydanie FROM wydanie")
            self.wydania_fk = [id_wydanie[0] for id_wydanie in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_klienci_fk(self):
        try:
            self.kursor.execute("SELECT id_klient FROM klient")
            self.klienci_fk = [id_klient[0] for id_klient in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                opinia = {
                    'id_wydanie': random.choice(self.wydania_fk),
                    'id_klient': random.choice(self.klienci_fk),
                    'tresc': funkcje.losowy_ciag(255),
                    'ocena': random.randint(1, 5),
                    'data_wystawienia': funkcje.generuj_date(5),
                }
                self.dane_do_wstawienia.append(opinia)

            self.kursor.executemany("""
                                INSERT INTO opinia (id_wydanie, id_klient, tresc, ocena, data_wystawienia)
                                VALUES (:id_wydanie, :id_klient, :tresc, :ocena, :data_wystawienia)""",
                                    self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()

    def wstaw_dane(self, liczba_danych=1):
        try:
            self.pobierz_wydania_fk()
            self.pobierz_klienci_fk()
            self.generuj_dane(liczba_danych)

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
