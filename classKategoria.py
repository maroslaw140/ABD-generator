import cx_Oracle
import funkcje

class Kategoria:
    def __init__(self, kursor):
        self.kursor = kursor
        self.kategorie = []

    def pobierz_kategorie(self):
        self.kursor.execute("SELECT nazwa FROM kategoria")
        self.kategorie = self.kursor.fetchall()

    def generuj_dane(self, liczba_danych=1):
        for _ in range(liczba_danych):
            nazwa_kategorii = funkcje.losowy_ciag(50)

            while nazwa_kategorii in self.kategorie:
                nazwa_kategorii = funkcje.losowy_ciag(50)

            self.kategorie.append(nazwa_kategorii)
            self.kursor.execute("""INSERT INTO kategoria (nazwa) VALUES(:nazwa)""", {'nazwa': nazwa_kategorii})


