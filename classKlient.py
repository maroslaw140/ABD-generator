import cx_Oracle
import funkcje
import random

class Klient:
    def __init__(self, kursor):
        self.kursor = kursor
        self.dane_do_wstawienia = []

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                pracownik = {
                    'imie': funkcje.losowe_imie(),
                    'nazwisko': funkcje.losowe_nazwisko(),
                    'telefon': funkcje.generuj_nr_telefonu(),
                    'mail': funkcje.generuj_mail(),
                }
                self.dane_do_wstawienia.append(pracownik)

            self.kursor.executemany("""
                                INSERT INTO klient (imie, nazwisko, telefon, mail)
                                VALUES (:imie, :nazwisko, :telefon, :mail)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
