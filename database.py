import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Создать подключение к базе данных SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """ Создать таблицу для хранения результатов сортировки """
    try:
        sql_create_results_table = """CREATE TABLE IF NOT EXISTS results (
                                        id integer PRIMARY KEY,
                                        algorithm text NOT NULL,
                                        original text NOT NULL,
                                        sorted text NOT NULL
                                    );"""
        c = conn.cursor()
        c.execute(sql_create_results_table)
    except Error as e:
        print(e)

def insert_result(conn, algorithm, original, sorted_result):
    """ Вставить новый результат в таблицу results """
    sql = ''' INSERT INTO results(algorithm, original, sorted)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (algorithm, original, sorted_result))
    conn.commit()
    return cur.lastrowid

def fetch_results(conn):
    """ Получить все результаты из таблицы results """
    cur = conn.cursor()
    cur.execute("SELECT * FROM results")
    rows = cur.fetchall()
    return rows
