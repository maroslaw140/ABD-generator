import random
import cx_Oracle
import funkcje

class Rachunek:
    def __init__(self, kursor):
        self.kursor = kursor
        self.zamowienia_fk = []
        self.sposoby_zaplaty_fk = []
        self.dane_do_wstawienia = []

    def pobierz_zamowienia_fk(self):
        try:
            self.kursor.execute("SELECT id_zamowienie FROM zamowienie")
            rekordy = self.kursor.fetchall()
            self.zamowienia_fk = [id_zamowienie[0] for id_zamowienie in rekordy]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_sposoby_zaplaty_fk(self):
        try:
            self.kursor.execute("SELECT id_sposob_zaplaty FROM sposob_zaplaty")
            self.sposoby_zaplaty_fk = [id_sposob_zaplaty[0] for id_sposob_zaplaty in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                zamowienie = random.choice(self.zamowienia_fk)
                self.zamowienia_fk.remove(zamowienie)

                rachunek = {
                    'id_zamowienie': zamowienie,
                    'data_wystawienia': funkcje.generuj_date(),
                    'id_sposob_zaplaty': random.choice(self.sposoby_zaplaty_fk),
                }
                self.dane_do_wstawienia.append(rachunek)

            self.kursor.executemany("""
                                INSERT INTO rachunek (id_zamowienie, data_wystawienia, id_sposob_zaplaty)
                                VALUES (:id_zamowienie, :data_wystawienia, :id_sposob_zaplaty)""", self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()