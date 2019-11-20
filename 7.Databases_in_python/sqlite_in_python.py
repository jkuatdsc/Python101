import sqlite3

connection = sqlite3.connect('albert.db')
cursor = connection.cursor()
cursor.execute('drop table vick')
cursor.execute('Create table vick(name text primary key,age integer,languages text)')
cursor.execute('Insert into vick VALUES(?, ?, ?)', ('victor kamau', 20, 'English'))

vs = cursor.execute('Select * from vick WHERE name LIKE (?)', 'v')
print(vs)
vick = [{'name': row[0], 'age': row[1], 'language': row[2]} for row in cursor.fetchall()]
for contents in vick:
    print('')
    print(contents)

connection.commit()
connection.close()
