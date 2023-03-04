"""
Функции для получения/загрузки данных в базу.

Создатель Александр Говорухин, @alexitsochi
"""

import sqlite3


def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def write_to_file(data, kpp_id, count):
    i = count
    while i > 0:
        f = open(f"cache/{kpp_id}_{i}.jpg", 'wb')
        f.write(data)
        f.close()
        i -= 1


sqlite_connection = sqlite3.connect('database.db')


def insert_blob(kpp_number, photo):
    try:
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO photo
                                  (kpp_number, photo) VALUES (?, ?)"""

        conv_photo = convert_to_binary_data(photo)

        data_tuple = (kpp_number, conv_photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение успешно вставлено как BLOB в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def read_blob_data(kpp_number):
    try:
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from photo where kpp_number = ?"""
        cursor.execute(sql_fetch_blob_query, (kpp_number,))
        record = cursor.fetchall()

        sql_count_photo = """SELECT count(kpp_number) from photo where kpp_number = ?"""
        cursor.execute(sql_count_photo, (kpp_number,))
        count_photo = cursor.fetchone()

        for row in record:
            kpp_id = row[1]
            photo = row[2]
            write_to_file(photo, kpp_id, count_photo[0])
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


if __name__ == '__main__':
    insert_blob("1", "test.jpg")
    read_blob_data(1)
