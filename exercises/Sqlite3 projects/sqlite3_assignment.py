import sqlite3
connection = sqlite3.connect("test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

##c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit()

##connection = sqlite3.connect(':memory:')

##c.execute("DROP TABLE IF EXISTS People")
##
##connection.close()

##with sqlite3.connect("test_database.db") as connection:
##    # perfomr any SQL operation using connection here

##with sqlite3.connect('test_database.db') as connection:
##    c = connection.cursor()
##    c.executescript("""DROP TABLE IF EXISTS People;
##                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
##                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
##                    """)
##
##peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling',28))
##
##c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
##

