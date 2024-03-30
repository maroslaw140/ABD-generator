import cx_Oracle
import funkcje

class Seria:
    def __init__(self, kursor):
        self.kursor = kursor
        self.serie = []

    def pobierz_kategorie(self):
        self.kursor.execute("SELECT nazwa FROM seria")
        self.serie = self.kursor.fetchall()

    def generuj_dane(self, liczba_danych=1):
        for _ in range(liczba_danych):
            nazwa_serii = funkcje.losowy_ciag(255)

            while nazwa_serii in self.serie:
                nazwa_serii = funkcje.losowy_ciag(255)

            self.serie.append(nazwa_serii)
            self.kursor.execute("""INSERT INTO seria (nazwa) VALUES(:nazwa)""", {'nazwa': nazwa_serii})


