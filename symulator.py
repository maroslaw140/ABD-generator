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

generator = Generator()
generator.polacz()

autor = Autor(generator.kursor)
autor.generuj_dane(0)

adres = Adres(generator.kursor)
adres.generuj_dane(0)

kategoria = Kategoria(generator.kursor)
kategoria.pobierz_nazwy()
kategoria.generuj_dane(0)

pracownik = Pracownik(generator.kursor)
pracownik.pobierz_stanowiska_fk()
pracownik.generuj_dane(0)

seria = Seria(generator.kursor)
seria.pobierz_nazwy()
seria.generuj_dane(0)

stanowisko = Stanowisko(generator.kursor)
stanowisko.pobierz_nazwy()
stanowisko.generuj_dane(0)

wydawnictwo = Wydawnictwo(generator.kursor)
wydawnictwo.pobierz_nazwy()
wydawnictwo.generuj_dane(0)

# test

klient = Klient(generator.kursor)
klient.generuj_dane(100)

uzytkownik = Uzytkownik(generator.kursor)
uzytkownik.pobierz_pracownicy_fk()
uzytkownik.pobierz_klienci_fk()
uzytkownik.pobierz_status_uzytkownika_fk()
uzytkownik.generuj_dane(100)

ksiazka = Ksiazka(generator.kursor)
ksiazka.pobierz_autorzy_fk()
ksiazka.pobierz_serie_fk()
ksiazka.pobierz_kategorie_fk()
ksiazka.generuj_dane(100)

wydanie = Wydanie(generator.kursor)
wydanie.pobierz_ksiazki_fk()
wydanie.pobierz_wydawnictwa_fk()
wydanie.generuj_dane(100)

opinia = Opinia(generator.kursor)
opinia.pobierz_wydania_fk()
opinia.pobierz_klienci_fk()
opinia.generuj_dane(100)

zamowienie = Zamowienie(generator.kursor)
zamowienie.pobierz_klienci_fk()
zamowienie.pobierz_adresy_fk()
zamowienie.pobierz_pracownicy_fk()
zamowienie.pobierz_sposoby_dostawy_fk()
zamowienie.pobierz_statusy_zamowienia_fk()
zamowienie.generuj_dane(100)

rachunek = Rachunek(generator.kursor)
rachunek.pobierz_zamowienia_fk()
rachunek.pobierz_sposoby_zaplaty_fk()
rachunek.generuj_dane(100)
