import sqlite3
import os

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "medicines.db")

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    # MEDICINES TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_name TEXT NOT NULL,
            company_name TEXT NOT NULL,
            net_rate REAL NOT NULL,
            mrp REAL NOT NULL,
            stockiest TEXT NOT NULL,
            paid_status TEXT NOT NULL,     -- Paid / Unpaid / Half Paid
            paid_amount REAL DEFAULT 0,
            remaining_amount REAL DEFAULT 0,
            date_added DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert default admin if not exists
    cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, ("admin", "admin123", "admin"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")
