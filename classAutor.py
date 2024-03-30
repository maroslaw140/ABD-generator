import cx_Oracle
import funkcje

class Autor:
    def __init__(self, kursor):
        self.kursor = kursor

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                self.kursor.execute("""
                                    INSERT INTO autor (imie, nazwisko) 
                                    VALUES (:imie, :nazwisko)""",
                                    {'imie': funkcje.losowe_imie(), 'nazwisko': funkcje.losowe_nazwisko()})

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
