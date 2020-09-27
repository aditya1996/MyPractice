import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (                              # Ran once to create table and then commented it 
           first text,
           last text,
           pay integer
          )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first': emp.first,'last': emp.last, 'pay': emp.pay})

def get_emp_by_name(lastname):
    c.execute(" SELECT * FROM employees WHERE last=:last",{'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Jane','Vettel',90000)

print(emp_1)
print(emp_2)

conn.close()

