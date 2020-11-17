import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#create a new table with AUTO INCREMENTING ID that doesnt already exist
create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #i.e when adding a new user you only specify username/password
cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text,price real)" #real is float for sql
cursor.execute(create_items_table)

connection.commit()
connection.close()