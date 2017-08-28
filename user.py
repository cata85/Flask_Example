import sqlite3


def get_user(username):
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()

    return c.execute('SELECT * FROM users WHERE username = (?)', (username,)).fetchone()


def create_user(username, password):
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()

    c.execute('INSERT INTO users (username, password)  VALUES (?, ?)', (username, password))
    conn.commit()
    pass


def check_username_aval(username):
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()

    checker = c.execute('SELECT * FROM users WHERE username = (?)', (username,)).fetchone()
    return checker is None


def check_login(username, password):
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()

    checker = c.execute('SELECT * FROM users WHERE username = (?) AND password = (?)',
                        (username, password)).fetchone()
    return checker is not None


def compare_pass(pass1, pass2):
    return pass1 == pass2
