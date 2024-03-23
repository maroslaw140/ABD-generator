import cx_Oracle
from dotenv import load_dotenv
import os

load_dotenv()

try:
    dsn = cx_Oracle.makedsn(host=os.getenv("db_host"), port=os.getenv("db_port"), service_name=os.getenv("db_service"))
    connection = cx_Oracle.connect(user=os.getenv("db_user"), password=os.getenv("db_password"), dsn=dsn)
    cursor = connection.cursor()
    print("Połączono z SQLDeveloper :)")
except cx_Oracle.Error as error:
    print("Wystąpił błąd podczas łączenia z bazą danych:", error)
finally:
    if 'connection' in locals():
        connection.close()
