import random
import cx_Oracle
import funkcje


class Wydanie:
    def __init__(self, kursor):
        self.kursor = kursor
        self.ksiazki_fk = []
        self.wydawnictwa_fk = []
        self.dane_do_wstawienia = []

        self.nazwa_tabeli = "wydanie"
        self.insert = """INSERT INTO wydanie (id_ksiazka, isbn, data_wydania, liczba_stron, id_wydawnictwo, cena, wysokosc_mm, dlugosc_mm, szerokosc_mm, liczba_sztuk_mag) VALUES ({id_ksiazka}, '{isbn}', '{data_wydania}', {liczba_stron}, {id_wydawnictwo}, {cena}, {wysokosc_mm}, {dlugosc_mm}, {szerokosc_mm}, {liczba_sztuk_mag})"""

    def pobierz_ksiazki_fk(self):
        try:
            self.kursor.execute("SELECT id_ksiazka FROM ksiazka")
            self.ksiazki_fk = [id_ksiazka[0] for id_ksiazka in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def pobierz_wydawnictwa_fk(self):
        try:
            self.kursor.execute("SELECT id_wydawnictwo FROM wydawnictwo")
            self.wydawnictwa_fk = [id_wydawnictwo[0] for id_wydawnictwo in self.kursor.fetchall()]
        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)

    def generuj_dane(self, liczba_danych=1):
        try:
            for _ in range(liczba_danych):
                wydanie = {
                    'id_ksiazka': random.choice(self.ksiazki_fk),
                    'isbn': str(random.randint(1000000000000, 9999999999999)),
                    'data_wydania': funkcje.generuj_date(100),
                    'liczba_stron': random.randint(10, 1000),
                    'id_wydawnictwo': random.choice(self.wydawnictwa_fk),
                    'cena': round(random.uniform(10, 100), 2),
                    'wysokosc_mm': random.randint(100, 299),
                    'dlugosc_mm': random.randint(100, 299),
                    'szerokosc_mm': random.randint(100, 299),
                    'liczba_sztuk_mag': random.randint(0, 100000),
                }
                self.dane_do_wstawienia.append(wydanie)

            self.kursor.executemany("""
                                INSERT INTO wydanie (id_ksiazka, isbn, data_wydania, liczba_stron, id_wydawnictwo, cena, wysokosc_mm, dlugosc_mm, szerokosc_mm, liczba_sztuk_mag)
                                VALUES (:id_ksiazka, :isbn, :data_wydania, :liczba_stron, :id_wydawnictwo, :cena, :wysokosc_mm, :dlugosc_mm, :szerokosc_mm, :liczba_sztuk_mag)""",
                                    self.dane_do_wstawienia)

            self.kursor.connection.commit()

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
            self.kursor.connection.rollback()

    def wstaw_dane(self, liczba_danych=1):
        try:
            self.pobierz_ksiazki_fk()
            self.pobierz_wydawnictwa_fk()
            self.generuj_dane(liczba_danych)

        except cx_Oracle.Error as error:
            print(error)
            funkcje.zapisz_blad(error)
