from classAdres import Adres
from classAutor import Autor
from classGenerator import Generator
from classKategoria import Kategoria
from classKlient import Klient
from classKsiazka import Ksiazka
from classOpinia import Opinia
from classPracownik import Pracownik
from classRachunek import Rachunek
from classSeria import Seria
from classStanowisko import Stanowisko
from classUzytkownik import Uzytkownik
from classWydanie import Wydanie
from classWydawnictwo import Wydawnictwo
from classZamowienie import Zamowienie
from classZamowieniePozycja import ZamowieniePozycja

generator = Generator()
generator.polacz()

tabela = Kategoria(generator.kursor)
tabela.pobierz_nazwy()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "kategoria - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Seria(generator.kursor)
tabela.pobierz_nazwy()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "seria - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Autor(generator.kursor)
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "autor - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Adres(generator.kursor)
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "adres - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Stanowisko(generator.kursor)
tabela.pobierz_nazwy()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "stanowisko - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Wydawnictwo(generator.kursor)
tabela.pobierz_nazwy()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "wydawnictwo - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Pracownik(generator.kursor)
tabela.pobierz_stanowiska_fk()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "pracownik - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Klient(generator.kursor)
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "klient - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

# tabela = Uzytkownik(generator.kursor)
# tabela.pobierz_pracownicy_fk()
# tabela.pobierz_klienci_fk()
# tabela.pobierz_status_uzytkownika_fk()
# tabela.generuj_dane(10)
# print(tabela.kursor.rowcount, "uzytkownik - rekordów wstawiono.")
# generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Ksiazka(generator.kursor)
tabela.pobierz_autorzy_fk()
tabela.pobierz_serie_fk()
tabela.pobierz_kategorie_fk()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "ksiazka - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Wydanie(generator.kursor)
tabela.pobierz_ksiazki_fk()
tabela.pobierz_wydawnictwa_fk()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "wydanie - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = Opinia(generator.kursor)
tabela.pobierz_wydania_fk()
tabela.pobierz_klienci_fk()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "opinia - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

# tabela = Zamowienie(generator.kursor)
# tabela.pobierz_klienci_fk()
# tabela.pobierz_adresy_fk()
# tabela.pobierz_pracownicy_fk()
# tabela.pobierz_sposoby_dostawy_fk()
# tabela.pobierz_statusy_zamowienia_fk()
# tabela.generuj_dane(10)
# print(tabela.kursor.rowcount, "zamowienie - rekordów wstawiono.")
# generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

# tabela = Rachunek(generator.kursor)
# tabela.pobierz_zamowienia_fk()
# tabela.pobierz_wykorzystane_zamowienia_fk()
# tabela.pobierz_sposoby_zaplaty_fk()
# tabela.generuj_dane(10)
# print(tabela.kursor.rowcount, "rachunek - rekordów wstawiono.")
# generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)

tabela = ZamowieniePozycja(generator.kursor)
tabela.pobierz_zamowienia_fk()
tabela.pobierz_wydania_fk()
tabela.generuj_dane(10)
print(tabela.kursor.rowcount, "zamowienie_pozycja - rekordów wstawiono.")
generator.zapisz_insert_do_pliku(tabela.insert, tabela.dane_do_wstawienia)
