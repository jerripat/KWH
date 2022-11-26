import sqlite3

conn = sqlite3.connect("KWHCounter.db")

c = conn.cursor()
# Data Types
# INTEGER,TEXT,REAL,NULL,BLOB

c.execute("""
CREATE TABLE kwhCounter (

tblIndex INTEGER PRIMARY KEY AUTOINCREMENT,
testItem text NOT NULL,
date text NOT NULL,
kwhHoursTested real,
KWHReading real,
totalKWH real
) """)

conn.commit()
conn.close()
