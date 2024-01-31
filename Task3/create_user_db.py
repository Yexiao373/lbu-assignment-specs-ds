#!/usr/bin/env python3

import sqlite3


def create_user_table():

    conn = sqlite3.connect('users.db')

    if conn:
        conn.execute('DROP TABLE IF EXISTS users')
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY,
                        username text NOT NULL UNIQUE,
                        name text NOT NULL,
                        password text NOT NULL,
                        admin boolean NOT NULL
                        )
                    ''')

    conn.close()


if __name__ == '__main__':
    create_user_table()
