import cx_Oracle
import funkcje
import random

class Adres:
    def __init__(self, kursor):
        self.kursor = kursor
        self.dane_do_wstawienia = []

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                adres = {
                    'ulica': funkcje.losowy_ciag(100, True, False),
                    'nr_budynku': random.randint(1, 200),
                    'nr_mieszkania': random.randint(1, 50),
                    'miasto': funkcje.losowy_ciag(100, True, False),
                    'kod_pocztowy': funkcje.generuj_kod_pocztowy()
                }
                self.dane_do_wstawienia.append(adres)

            self.kursor.executemany("""
                                    INSERT INTO adres (ulica, nr_budynku, nr_mieszkania, miasto, kod_pocztowy) 
                                    VALUES (:ulica, :nr_budynku, :nr_mieszkania, :miasto, :kod_pocztowy)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
