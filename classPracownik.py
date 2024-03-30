import cx_Oracle
import funkcje
import random

class Pracownik:
    def __init__(self, kursor):
        self.kursor = kursor
        self.stanowiska_fk = []

    def pobierz_stanowiska(self):
        try:
            self.kursor.execute("SELECT id_stanowisko FROM stanowisko")
            self.stanowiska_fk = self.kursor.fetchall()
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                pracownik = {
                    'imie': funkcje.losowe_imie(),
                    'nazwisko': funkcje.losowe_nazwisko(),
                    'telefon': funkcje.generuj_nr_telefonu(),
                    'mail': funkcje.generuj_mail(),
                    'id_stanowisko': random.choice(self.stanowiska_fk),
                    'data_zatrudnienia': funkcje.generuj_date()
                }
                self.kursor.execute("""
                                INSERT INTO pracownik (imie, nazwisko, telefon, mail, id_stanowisko, data_zatrudnienia)
                                VALUES (:imie, :nazwisko, :telefon, :mail, :id_stanowisko, :data_zatrudnienia)""", pracownik)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
