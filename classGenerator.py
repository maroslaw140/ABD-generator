import cx_Oracle
from dotenv import load_dotenv
import os


class Generator:

    def __init__(self):
        self.kursor = None
        self.plik = "plik.txt"

    def polacz(self):
        try:
            load_dotenv()

            dsn = cx_Oracle.makedsn(host=os.getenv("db_host"), port=os.getenv("db_port"), service_name=os.getenv("db_service"))
            connection = cx_Oracle.connect(user=os.getenv("db_user"), password=os.getenv("db_password"), dsn=dsn)
            self.kursor = connection.cursor()
            print("Połączono z bazą")
        except cx_Oracle.Error as error:
            print(error)

    def zapisz_insert_do_pliku(self, insert, dane_do_wstawienia):
        try:
            with open(self.plik, "a") as file:
                for dane in dane_do_wstawienia:
                    linia_insert = insert.format(**dane)
                    if linia_insert[-1] != ';':
                        linia_insert += ';'
                    linia_insert += "\n"
                    file.write(linia_insert)
        except IOError as error:
            print("Błąd zapisu do pliku:", error)
