import sqlite3

from debugpy import connect

conn = sqlite3.connect('sql.db')

cursor = conn.cursor()
cursor.execute('SELECT * FROM `try`;')

records = cursor.fetchall()
print(records)

cursor.close()
conn.close() 