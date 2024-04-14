import random
import cx_Oracle
import funkcje


class ZamowieniePozycja:
    def __init__(self, kursor):
        self.kursor = kursor
        self.zamowienia_fk = []
        self.wydania_fk = []
        self.dane_do_wstawienia = []

        self.insert = """INSERT INTO zamowienie_pozycja (id_zamowienie, id_wydanie, liczba_sztuk) VALUES ('{id_zamowienie}', '{id_wydanie}', '{liczba_sztuk}')"""

    def pobierz_zamowienia_fk(self):
        try:
            self.kursor.execute("SELECT id_zamowienie FROM zamowienie")
            self.zamowienia_fk = [id_zamowienie[0] for id_zamowienie in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_wydania_fk(self):
        try:
            self.kursor.execute("SELECT id_wydanie FROM wydanie")
            self.wydania_fk = [id_wydanie[0] for id_wydanie in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                zamowienie_pozycja = {
                    'id_zamowienie': random.choice(self.zamowienia_fk),
                    'id_wydanie': random.choice(self.wydania_fk),
                    'liczba_sztuk': random.randint(1, 10),
                }
                self.dane_do_wstawienia.append(zamowienie_pozycja)

            self.kursor.executemany("""
                                INSERT INTO zamowienie_pozycja (id_zamowienie, id_wydanie, liczba_sztuk)
                                VALUES (:id_zamowienie, :id_wydanie, :liczba_sztuk)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
