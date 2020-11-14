import sqlite3

peopleData = (("Jean-Baptiste Zorg", "Human", 122), ("Korben Dallas", "Meat Popsicle", 100), ("Ak'not", "Mangalore", -5))


with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE People(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleData)
    c.execute("SELECT Name, Species, IQ FROM People")
    c.execute("UPDATE People SET Species='Human' WHERE Name='Korben Dallas'")
    c.execute("SELECT Name, Species, IQ FROM People WHERE Species='Human'")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
