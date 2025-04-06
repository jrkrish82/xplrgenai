import sqlite3

## Connect to an SQLite database
connection=sqlite3.connect('example.db')

## Get a cursor object
cursor = connection.cursor()

## Create a Table
cursor.execute('''
Create Table If Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    age Integer,
    department text
    )
''')

## Commit the changes
connection.commit()



#Insert a row of data
cursor.execute('''Insert Into employees (name, age, department) Values ('Krishna', 25, 'Architect')''')
#Insert another row of data
cursor.execute('''Insert Into employees (name, age, department) Values ('Rama', 22, 'Engineering')''')
#Insert another row of data
cursor.execute('''Insert Into employees (name, age, department) Values ('Sita', 23, 'Engineering')''')

## Commit the changes
connection.commit()


    ## Update the data in the table
cursor.execute('''
UPDATE employees
Set age=31
where name="Krish"
''')

connection.commit()


## Delete the data from the table
cursor.execute('''Delete From employees where name="Sita"''')


    #Delete duplicate rows from the table
cursor.execute('''Delete From employees where rowid not in (Select min(rowid) from employees group by name)''')
connection.commit()


## Fetch the result
cursor.execute('Select * From employees')
rows= cursor.fetchall()

for row in rows:
    print(row)
