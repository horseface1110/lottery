import importlib


import sqlite3

# connect to database
conn = sqlite3.connect('sql.db')
# create cursor object
cursor = conn.cursor()

cur = conn.cursor()
cur.execute("SELECT * FROM "+ "try9" +" WHERE id = " + str(1))

rows = cur.fetchall()

for row in rows:
    print(row[0])