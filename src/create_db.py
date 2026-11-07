import sqlite3
import contextlib import contextmanager

@contextmanager
def create_db():
    # читаємо файл зі скриптом для створення БД
    with open("task.sql", "r") as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect("school.db") as con:
        cur = con.cursor()
        try:
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)
        except sqlite3.RunTimeError as e:
            print(e)
            con.rollback()
        finally:
            cur.close()


if __name__ == "__main__":
    create_db()
