import mysql.connector
from fastapi import HTTPException


class Dao:
    def __init__(self):
        pass

    def connect_to_db(self) -> mysql.connector.MySQLConnection:
        connection = mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            port="3306",
            database="inventario",
        )

        return connection
