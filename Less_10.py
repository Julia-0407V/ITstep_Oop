import sqlite3

connection  = sqlite3.connect("itstep_DB.sl3",5)
cur = connection.cursor()

#cur.execute("CREATE TABLE first_table (name TEXT);")
#cur.execute("DROP TABLE sqlite_master ;")
#cur.execute("INSERT INTO first_table (name) VALUES ('Zahar') ;")
#cur.execute("SELECT rowid, name FROM first_table ;")

#cur.execute("UPDATE first_table SET name = 'Marina' WHERE rowid=2 ;")

#cur.execute("DELETE FROM first_table WHERE rowid=3 ;")
#cur.execute("DELETE FROM first_table  ;")


#cur.execute("CREATE TABLE students (ID INT, name TEXT, age INT);")
#cur.execute("INSERT INTO students (ID, name, age ) VALUES (3, 'Maks', 14);")
cur.execute(" SELECT rowid, name, age FROM students WHERE age>6")


connection.commit()

res = cur.fetchall()
print(res)

connection.close()
