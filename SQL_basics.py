import sqlite3
#establing the connection
conn = sqlite3.connect('employee.db')
c = conn.cursor() #cursor in making
#crating the table
'''
c.execute("""CREATE TABLE employees(
            first text,
            last text,
            income integer)""")
'''
#inserting values into the table
#c.execute("INSERT INTO employees VALUES('Bhavishya','Pandit',100000)")
c.execute('SELECT * FROM EMPLOYEES')
#fetching value
print(c.fetchone())
#commits the change
conn.commit()
#closing the connection
conn.close()