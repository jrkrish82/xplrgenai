import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

# Create a table
#cursor.execute('''
#CREATE TABLE IF NOT EXISTS EMPLOYEES (    id INTEGER PRIMARY KEY,
#    name TEXT,
#    age INTEGER,
#    department TEXT,
#    salary REAL,
#    location TEXT,
#    hire_date TEXT,
#    termination_date TEXT,
#    status TEXT      
           
#)
#''')



employees = [
    (1, 'Krishna Raj', 30, 'Engineering', 9170000, 'New York', '2021-01-15', None, 'Active'),
    (2, 'Raj Kumar', 25, 'Sales', 500000, 'Chicago', '2020-03-22', None, 'Active'),
    (3, 'Alice Johnson', 35, 'HR', 600000, 'San Francisco', '2019-07-10', None, 'Active'),
    (4, 'Bob Brown', 40, 'Engineering', 800000, 'New York', '2018-11-05', None, 'Active'),
    (5, 'Charlie Davis', 28, 'Sales', 550000, 'Chicago', '2021-06-18', None, 'Active')
]

cursor.executemany('''
INSERT INTO EMPLOYEES (id, name, age, department, salary, location, hire_date, termination_date, status)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', employees)

conn.commit()


# Query the database
cursor.execute('SELECT * FROM EMPLOYEES')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()