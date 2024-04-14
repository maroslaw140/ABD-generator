from classAdres import Adres
from classAutor import Autor
from classGenerator import Generator
from classKategoria import Kategoria
from classKlient import Klient
from classPracownik import Pracownik
from classSeria import Seria
from classStanowisko import Stanowisko
from classWydawnictwo import Wydawnictwo

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
klient.generuj_dane(1000)
