import sqlite3

DB_NAME = 'database.db'

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
            name TEXT NOT NULL,
            status TEXT CHECK(status IN ('Pending', 'Ongoing', 'Completed', 'Cancelled')) NOT NULL,
            launch_date TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS engineer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS engineer_mission (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            engineer_id INTEGER NOT NULL,
            mission_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            FOREIGN KEY (engineer_id) REFERENCES engineer(id) ON DELETE CASCADE,
            FOREIGN KEY (mission_id) REFERENCES missions(id) ON DELETE CASCADE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            mission_id INTEGER NOT NULL,
            FOREIGN KEY (mission_id) REFERENCES missions(id) ON DELETE CASCADE
        );
    """)

    connection.commit()
    connection.close()
