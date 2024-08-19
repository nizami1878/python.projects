import sqlite3
conn=sqlite3.connect("my_database.db")
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS footballers")
cursor.execute( '''
 CREATE TABLE  footballers(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 surname TEXT,
 team TEXT,
 number INTEGER
)
'''
)
cursor.execute("INSERT INTO footballers(name,surname,team,number)VALUES(?,?,?,?)",("Marcus","Rashford","Manchester United",10))
cursor.execute("INSERT INTO footballers(name,surname,team,number)VALUES(?,?,?,?)",("Scott","Mctominay","Manchester United",39))
cursor.execute("INSERT INTO footballers(name,surname,team,number)VALUES(?,?,?,?)",("Juninho","Olavio","Karabakh",16))
cursor.execute("INSERT INTO footballers(name,surname,team,number)VALUES(?,?,?,?)",("Marko","Jankovic","Karabakh",8))
cursor.execute("UPDATE footballers SET number=18 WHERE name='Juninho'")
cursor.execute("SELECT * FROM footballers")
football=cursor.fetchall()
for footballers in football:
    print(footballers)
conn.commit()
conn.close()