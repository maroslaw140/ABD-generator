import cx_Oracle
import funkcje


class Kategoria:
    def __init__(self, kursor):
        self.kursor = kursor
        self.kategorie = []
        self.dane_do_wstawienia = []

        self.insert = """INSERT INTO kategoria (nazwa) VALUES('{nazwa}')"""

    def pobierz_nazwy(self):
        try:
            self.kursor.execute("SELECT nazwa FROM kategoria")
            self.kategorie = [nazwa[0] for nazwa in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                nazwa_kategorii = funkcje.losowy_ciag(50)

                while nazwa_kategorii in self.kategorie:
                    nazwa_kategorii = funkcje.losowy_ciag(50)

                self.kategorie.append(nazwa_kategorii)
                self.dane_do_wstawienia.append({'nazwa': nazwa_kategorii})

            self.kursor.executemany("""INSERT INTO kategoria (nazwa) VALUES(:nazwa)""", self.dane_do_wstawienia)
            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
