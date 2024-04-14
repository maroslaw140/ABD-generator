import random
import cx_Oracle
import funkcje

class Ksiazka:
    def __init__(self, kursor):
        self.kursor = kursor
        self.autorzy_fk = []
        self.serie_fk = []
        self.kategorie_fk = []
        self.dane_do_wstawienia = []

        self.insert = """INSERT INTO ksiazka (id_autor, tytul, id_seria, id_kategoria) VALUES ('{id_autor}', '{tytul}', '{id_seria}', '{id_kategoria}')"""

    def pobierz_autorzy_fk(self):
        try:
            self.kursor.execute("SELECT id_autor FROM autor")
            self.autorzy_fk = [id_autor[0] for id_autor in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_serie_fk(self):
        try:
            self.kursor.execute("SELECT id_seria FROM seria")
            self.serie_fk = [id_seria[0] for id_seria in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_kategorie_fk(self):
        try:
            self.kursor.execute("SELECT id_kategoria FROM kategoria")
            self.kategorie_fk = [id_kategoria[0] for id_kategoria in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                czy_seria = random.choice([True, False])

                if czy_seria:
                    id_seria = random.choice(self.serie_fk)
                else:
                    id_seria = None

                ksiazka = {
                    'id_autor': random.choice(self.autorzy_fk),
                    'tytul': funkcje.losowy_ciag(255, True, False),
                    'id_seria': id_seria,
                    'id_kategoria': random.choice(self.kategorie_fk),
                }
                self.dane_do_wstawienia.append(ksiazka)

            self.kursor.executemany("""
                                INSERT INTO ksiazka (id_autor, tytul, id_seria, id_kategoria)
                                VALUES (:id_autor, :tytul, :id_seria, :id_kategoria)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()