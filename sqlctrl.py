import sqlite3

from debugpy import connect

conn = sqlite3.connect('sql.db')

cursor = conn.cursor()
cursor.execute('SELECT * FROM `try9`;')

records = cursor.fetchall()
print(records)

appDesc = ""

isRun = True
while isRun:
    
    cursor.execute('SELECT * FROM `try`;')
    records = cursor.fetchall()
    
    for r in records:
        print(r)
    
    ctrl = input(appDesc)
    if ctrl == '0':
        isRun = False
    elif ctrl == '1':
        pass
    elif ctrl == '2':
        pass
    elif ctrl == '3':
        pass
    

cursor.close()
conn.close() 