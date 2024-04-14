import cx_Oracle
import funkcje


class Wydawnictwo:
    def __init__(self, kursor):
        self.kursor = kursor
        self.wydawnictwa = []
        self.dane_do_wstawienia = []

        self.insert = """INSERT INTO wydawnictwo (nazwa) VALUES ('{nazwa}')"""

    def pobierz_nazwy(self):
        try:
            self.kursor.execute("SELECT nazwa FROM wydawnictwo")
            self.wydawnictwa = [nazwa[0] for nazwa in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                nazwa_wydawnictwa = funkcje.losowy_ciag(200)

                while nazwa_wydawnictwa in self.wydawnictwa:
                    nazwa_wydawnictwa = funkcje.losowy_ciag(200)

                self.wydawnictwa.append(nazwa_wydawnictwa)
                self.dane_do_wstawienia.append({'nazwa': nazwa_wydawnictwa})

            self.kursor.executemany("INSERT INTO wydawnictwo (nazwa) VALUES (:nazwa)", self.dane_do_wstawienia)
            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()
