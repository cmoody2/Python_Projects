import sqlite3


# get personal data from user and insert into a tuple
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

# execute insert statment for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = ("INSERT INTO People VALUES (?, ?, ?)", personData)

