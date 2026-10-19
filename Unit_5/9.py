# Program 49: Write a program to connect Python with a database and execute SQL queries.
import sqlite3
con = sqlite3.connect("college.db")
cur = con.cursor()
cur.execute("drop table if exists student")
cur.execute("create table student(id integer, name text)")
cur.execute("insert into student values(1, 'Amit')")
cur.execute("insert into student values(2, 'Riya')")
con.commit()
cur.execute("select * from student")
print(cur.fetchall())
con.close()
