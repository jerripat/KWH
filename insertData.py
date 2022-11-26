import sqlite3 as sl

conn = sl.connect('KWHCounter.db')

c = conn.cursor()

c.execute('DROP TABLE kwhCounter')
