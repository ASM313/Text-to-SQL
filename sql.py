import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object for CRUD ops

cursor = connection.cursor()

# Create a table

table_info = """Create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT     
);
"""

# cursor.execute(table_info)

# Insert records 

# cursor.execute('''Insert into STUDENT values("Atiq",'Gen AI', 'A', 100)''')
# cursor.execute('''Insert into STUDENT values("Adviya",'Azure AI', 'A', 90)''')
# cursor.execute('''Insert into STUDENT values("Ruhan",'Gemini AI', 'A', 80)''')
# cursor.execute('''Insert into STUDENT values("Rayyan",'ML', 'A', 100)''')
# cursor.execute('''Insert into STUDENT values("Aarzu",'DL', 'A', 75)''')
# cursor.execute('''Insert into STUDENT values("Ayan",'NLP AI', 'A', 60)''')
# cursor.execute('''Insert into STUDENT values("Anam",'CV AI', 'A', 18)''')
# cursor.execute('''Insert into STUDENT values("Usman",'Gen AI', 'A', 66)''')
# cursor.execute('''Insert into STUDENT values("Huzair",'Gen AI', 'A', 72)''')
# cursor.execute('''Insert into STUDENT values("Munu",'Gen AI', 'A', 56)''')
# cursor.execute('''Insert into STUDENT values("Chunnu",'CV AI', 'A', 100)''')
# cursor.execute('''Insert into STUDENT values("Zainab",'PyTorch AI', 'A', 88)''')
# cursor.execute('''Insert into STUDENT values("Humera",'Tensorflow AI', 'A', 32)''')
# cursor.execute('''Insert into STUDENT values("Sara",'Gen AI', 'A', 60)''')
# cursor.execute('''Insert into STUDENT values("Muskan",'Gen AI', 'A', 40)''')

# Display all records

data = cursor.execute("Select * from Student")

for row in data:
    print(row)

# Close Connection

connection.commit()
connection.close()
 