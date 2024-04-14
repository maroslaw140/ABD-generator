import cx_Oracle
import funkcje

class Stanowisko:
    def __init__(self, kursor):
        self.kursor = kursor
        self.stanowiska = []
        self.dane_do_wstawienia = []

    def pobierz_nazwy(self):
        try:
            self.kursor.execute("SELECT nazwa FROM stanowisko")
            self.stanowiska = [nazwa[0] for nazwa in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):

        try:
            for _ in range(liczba_danych):
                nazwa_stanowiska = funkcje.losowy_ciag(50)

                while nazwa_stanowiska in self.stanowiska:
                    nazwa_stanowiska = funkcje.losowy_ciag(50)

                self.stanowiska.append(nazwa_stanowiska)
                self.dane_do_wstawienia.append({'nazwa': nazwa_stanowiska})

            self.kursor.executemany("INSERT INTO stanowisko (nazwa) VALUES (:nazwa)", self.dane_do_wstawienia)
            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
