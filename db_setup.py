import sqlite3

DB_NAME = 'aeromissions.db'

def get_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.execute('PRAGMA foreign_keys = ON;')
    return connection

def setup_database():
    connection = get_connection()
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS missions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT,
            launch_date TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS engineer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            specialization TEXT,
            mission_id INTEGER,
            FOREIGN KEY (mission_id) REFERENCES missions(id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            mission_id INTEGER,
            FOREIGN KEY (mission_id) REFERENCES missions(id)
        );
    """)

    connection.commit()
    connection.close()
