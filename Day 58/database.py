import sqlite3 as sq

connection = sq.connect("Users.db")

cursor = connection.cursor()

cursor.execute("""
    create table if not exists users(
        user_id integer primary key autoincrement,
        username text not null,
        password text not null
    )"""
)

connection.commit()