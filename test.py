import sqlite3
import csv

with sqlite3.connect("db.sqlite3") as connection:
    csvWriter = csv.writer(open("output.csv", "w"))
    c = connection.cursor()
    rows = c.fetchall()

    for x in rows:
        csvWriter.writerows(x)