"""
Модуль инициализации базы данных.

Создатель Александр Говорухин, @alexitsochi
"""

import sqlite3


def db_init():
    sqlite_connection = sqlite3.connect('database.db')

    with open('schema.sql') as schema:
        sqlite_connection.executescript(schema.read())


if __name__ == "__main__":
    db_init()