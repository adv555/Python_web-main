import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="university",
            user="postgres",
            password="postgres",
        )
        print("Connection established")
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()
