# bulk inserting - https://stackoverflow.com/questions/18219779/bulk-insert-huge-data-into-sqlite-using-python

import sqlite3

person = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
]

con = sqlite3.connect("app.db")

# Create the table
con.execute("create table customer(firstname, lastname, age, country)")

# Fill the table
con.executemany("insert into customer(firstname, lastname, age country) values (?,?)", persons)