import sqlite3

def connect_to_db(db_name="orders.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print(f"Successfully connected to database: {db_name}")
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to database: {e}")
        raise e
    return conn
