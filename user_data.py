import sqlite3

conn = sqlite3.connect('userdata.db')

c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users(
             id INTEGER PRIMARY KEY,
             username TEXT UNIQUE NOT NULL,
             password TEXT NOT NULL
             )
         ''')
