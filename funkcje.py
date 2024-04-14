import random
import string
from datetime import datetime, timedelta
import names


def losowy_ciag(max_dl, zawiera_spacje=True, zawiera_cyfry=False):
    try:
        zestaw_znakow = string.ascii_letters
        if zawiera_cyfry:
            zestaw_znakow += string.digits
        if zawiera_spacje:
            zestaw_znakow += ' '

        dlugosc = random.randint(1, max_dl)
        pierwszy_znak = random.choice(string.ascii_letters.upper())
        reszta_ciagu = ''.join(random.choices(zestaw_znakow.lower(), k=dlugosc - 1))
        return pierwszy_znak + reszta_ciagu
    except Exception as error:
        zapisz_blad(error)


def generuj_date(liczba_lat=10):
    try:
        dzisiaj = datetime.now()
        dzien_losowy = dzisiaj - timedelta(days=random.randint(0, 365 * liczba_lat))
        return dzien_losowy
    except Exception as error:
        zapisz_blad(error)


def losowe_imie():
    try:
        return names.get_first_name()
    except Exception as error:
        zapisz_blad(error)


def losowe_nazwisko():
    try:
        return names.get_last_name()
    except Exception as error:
        zapisz_blad(error)


def generuj_kod_pocztowy():
    try:
        return f"{random.randint(10, 99)}-{random.randint(100, 999)}"
    except Exception as error:
        zapisz_blad(error)


def generuj_mail(domena="gmail.com", dlugosc=200):
    try:
        uzytkownik = ''.join(random.choices(string.ascii_letters + string.digits, k=dlugosc))
        return f"{uzytkownik}@{domena}"
    except Exception as error:
        zapisz_blad(error)


def generuj_nr_telefonu():
    try:
        numer = ''.join(random.choices('0123456789', k=9))
        return f"+48 {numer[:3]} {numer[3:6]} {numer[6:]}"
    except Exception as error:
        zapisz_blad(error)


def zapisz_blad(blad):
    try:
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("bledy.txt", "a") as plik:
            plik.write(f"{data}: {blad}\n")

    except Exception as error:
        print("Błąd zapisywania błędu:", error)
