import cx_Oracle
import funkcje

class Seria:
    def __init__(self, kursor):
        self.kursor = kursor
        self.serie = []
        self.dane_do_wstawienia = []

    def pobierz_nazwy(self):
        try:
            self.kursor.execute("SELECT nazwa FROM seria")
            self.serie = [nazwa[0] for nazwa in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                nazwa_serii = funkcje.losowy_ciag(255)

                while nazwa_serii in self.serie:
                    nazwa_serii = funkcje.losowy_ciag(255)

                self.serie.append(nazwa_serii)
                self.dane_do_wstawienia.append({'nazwa': nazwa_serii})

            self.kursor.executemany("INSERT INTO seria (nazwa) VALUES (:nazwa)", self.dane_do_wstawienia)
            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
