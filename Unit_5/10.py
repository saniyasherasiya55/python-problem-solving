# Program 50: Write a program to retrieve database records using fetchone, fetchmany and fetchall methods.
import sqlite3
con = sqlite3.connect("college.db")
cur = con.cursor()
cur.execute("drop table if exists student")
cur.execute("create table student(id integer, name text)")
cur.executemany("insert into student values(?, ?)", [(1, "Amit"), (2, "Riya"), (3, "Neha"), (4, "Karan")])
con.commit()
cur.execute("select name from student order by name")
print("One :", cur.fetchone())
print("Many :", cur.fetchmany(2))
print("All remaining :", cur.fetchall())
con.close()
