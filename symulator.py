from classAdres import Adres
from classAutor import Autor
from classGenerator import Generator
from classKategoria import Kategoria
from classPracownik import Pracownik
from classSeria import Seria
from classStanowisko import Stanowisko
from classWydawnictwo import Wydawnictwo

generator = Generator()
generator.polacz()

autor = Autor(generator.kursor)
autor.generuj_dane(1000)

adres = Adres(generator.kursor)
adres.generuj_dane(1000)

kategoria = Kategoria(generator.kursor)
kategoria.pobierz_nazwy()
kategoria.generuj_dane(1000)

pracownik = Pracownik(generator.kursor)
pracownik.pobierz_stanowiska_fk()
pracownik.generuj_dane(1000)

seria = Seria(generator.kursor)
seria.pobierz_nazwy()
seria.generuj_dane(1000)

stanowisko = Stanowisko(generator.kursor)
stanowisko.pobierz_nazwy()
stanowisko.generuj_dane(1000)

wydawnictwo = Wydawnictwo(generator.kursor)
wydawnictwo.pobierz_nazwy()
wydawnictwo.generuj_dane(1000)