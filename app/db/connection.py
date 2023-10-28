import mysql.connector
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()


class Dao:
    def __init__(self):
        pass

    def connect_to_db(self) -> mysql.connector.MySQLConnection:
        connection = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_DATABASE"),
        )

        return connection
