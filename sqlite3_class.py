import sqlite3

db = sqlite3.connect('class.db')
cursor = db.cursor()
print('Connect ok')
