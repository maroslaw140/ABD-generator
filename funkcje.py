import random
import string
from datetime import datetime, timedelta

def losowy_ciag(max_dl, zawiera_spacje=True, zawiera_cyfry=False):
    zestaw_znakow = string.ascii_letters
    if zawiera_cyfry:
        zestaw_znakow += string.digits
    if zawiera_spacje:
        zestaw_znakow += ' '

    dlugosc = random.randint(1, max_dl)
    pierwszy_znak = random.choice(string.ascii_letters.upper())
    reszta_ciagu = ''.join(random.choices(zestaw_znakow.lower(), k=dlugosc-1))
    return pierwszy_znak + reszta_ciagu


def generuj_date(liczba_lat = 10, format= "%Y-%m-%d"):
    dzisiaj = datetime.now()
    dzien_losowy = dzisiaj - timedelta(days=random.randint(0, 365 * liczba_lat))

    return f"TO_DATE('{dzien_losowy.strftime(format)}', 'YYYY-MM-DD')"


def losowe_imie():
    imiona = ['Adam', 'Barbara', 'Celina', 'Dariusz', 'Ewa', 'Filip', 'Gabriela', 'Henryk', 'Izabela', 'Jan']
    return random.choice(imiona)


def losowe_nazwisko():
    nazwiska = ['Kowalski', 'Nowak', 'Mazur', 'Wójcik', 'Krawczyk', 'Lewandowski', 'Piotrowski', 'Szymański', 'Woźniak']
    return random.choice(nazwiska)


def generuj_kod_pocztowy():
    return f"{random.randint(10, 99)}-{random.randint(100, 999)}"
