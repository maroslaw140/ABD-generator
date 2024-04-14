import cx_Oracle
from dotenv import load_dotenv
import os
import csv


class Generator:

    def __init__(self):
        self.plik = "plik.txt"

    def polacz(self):
        try:
            load_dotenv()

            dsn = cx_Oracle.makedsn(host=os.getenv("db_host"), port=os.getenv("db_port"), service_name=os.getenv("db_service"))
            connection = cx_Oracle.connect(user=os.getenv("db_user"), password=os.getenv("db_password"), dsn=dsn)
            self.kursor = connection.cursor()
            print("Połączono z SQLDeveloper :)")
        except cx_Oracle.Error as error:
            print(error)




