import sqlite3

def get_db_connection():
    connection = sqlite3.connect('tickets.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_db_connection()
    connection.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            tags TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()