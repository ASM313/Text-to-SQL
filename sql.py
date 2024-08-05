import sqlite3

# Connect to sqlite
connection = sqlite.connect("student.db")

# Create a cursor object for CRUD ops

cursor = connection.cursor()

# Create a table

