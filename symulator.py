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

autor = Autor(generator.kursor)
#autor.generuj_dane(100)
#print(autor.kursor.rowcount, "autor record inserted.")

adres = Adres(generator.kursor)
#adres.generuj_dane(100)
#print(adres.kursor.rowcount, "adres record inserted.")

kategoria = Kategoria(generator.kursor)
kategoria.pobierz_nazwy()
#kategoria.generuj_dane(100)
#print(kategoria.kursor.rowcount, "kategoria record inserted.")

pracownik = Pracownik(generator.kursor)
pracownik.pobierz_stanowiska_fk()
#pracownik.generuj_dane(1000)
#print(pracownik.kursor.rowcount, "pracownik record inserted.")

seria = Seria(generator.kursor)
seria.pobierz_nazwy()
#seria.generuj_dane(100)
#print(seria.kursor.rowcount, "seria record inserted.")

stanowisko = Stanowisko(generator.kursor)
stanowisko.pobierz_nazwy()
#stanowisko.generuj_dane(100)
#print(stanowisko.kursor.rowcount, "stanowisko record inserted.")

wydawnictwo = Wydawnictwo(generator.kursor)
wydawnictwo.pobierz_nazwy()
#wydawnictwo.generuj_dane(100)
#print(wydawnictwo.kursor.rowcount, "wydawnictwo record inserted.")

klient = Klient(generator.kursor)
#klient.generuj_dane(1000)
#print(klient.kursor.rowcount, "klient record inserted.")

uzytkownik = Uzytkownik(generator.kursor)
uzytkownik.pobierz_pracownicy_fk()
uzytkownik.pobierz_klienci_fk()
uzytkownik.pobierz_status_uzytkownika_fk()
#uzytkownik.generuj_dane(1)
#print(uzytkownik.kursor.rowcount, "uzytkownik record inserted.")

ksiazka = Ksiazka(generator.kursor)
ksiazka.pobierz_autorzy_fk()
#print(ksiazka.autorzy_fk)
ksiazka.pobierz_serie_fk()
#print(ksiazka.serie_fk)
ksiazka.pobierz_kategorie_fk()
#print(ksiazka.kategorie_fk)
#ksiazka.generuj_dane(100)
#print(ksiazka.kursor.rowcount, "ksiazka record inserted.")

wydanie = Wydanie(generator.kursor)
wydanie.pobierz_ksiazki_fk()
wydanie.pobierz_wydawnictwa_fk()
#wydanie.generuj_dane(100)
#print(wydanie.kursor.rowcount, "wydanie record inserted.")

opinia = Opinia(generator.kursor)
opinia.pobierz_wydania_fk()
opinia.pobierz_klienci_fk()
#opinia.generuj_dane(5)
#print(opinia.kursor.rowcount, "opinia record inserted.")

zamowienie = Zamowienie(generator.kursor)
#zamowienie.pobierz_klienci_fk()
#print(zamowienie.klienci_fk)
#zamowienie.pobierz_adresy_fk()
#print(zamowienie.adresy_fk)
#zamowienie.pobierz_pracownicy_fk()
#print(zamowienie.pracownicy_fk)
#zamowienie.pobierz_sposoby_dostawy_fk()
#print(zamowienie.sposoby_dostawy_fk)
#zamowienie.pobierz_statusy_zamowienia_fk()
#print(zamowienie.statusy_zamowienia_fk)
#zamowienie.generuj_dane(100)
#print(zamowienie.kursor.rowcount, "zamowienie record inserted.")

rachunek = Rachunek(generator.kursor)


rachunek.pobierz_sposoby_zaplaty_fk()
rachunek.generuj_dane(4)
#print(rachunek.kursor.rowcount, "rachunek record inserted.")

zamowienie_pozycja = ZamowieniePozycja(generator.kursor)
zamowienie_pozycja.pobierz_zamowienia_fk()
zamowienie_pozycja.pobierz_wydania_fk()
zamowienie_pozycja.generuj_dane(100)
print(zamowienie_pozycja.kursor.rowcount, "zamowienie_pozycja record inserted.")
