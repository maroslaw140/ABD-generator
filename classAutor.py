import cx_Oracle
import funkcje

class Autor:
    def __init__(self, kursor):
        self.kursor = kursor
        self.dane_do_wstawienia = []

    def generuj_dane(self, liczba_danych=1):

        try:
            for _ in range(liczba_danych):
                self.dane_do_wstawienia.append((funkcje.losowe_imie(), funkcje.losowe_nazwisko()))

            self.kursor.executemany("""
                                    INSERT INTO autor (imie, nazwisko) 
                                    VALUES (:imie, :nazwisko)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
