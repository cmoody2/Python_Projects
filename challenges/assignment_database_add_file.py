
import sqlite3


fileList = ('information,docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# ----------------------------------------------------------------
# This creates our database named file.db with two columns:
# ID(which will be the primary key) and FileName
# ----------------------------------------------------------------

conn = sqlite3.connect('file.db')

with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Txt_Files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            FileName TEXT UNIQUE\
            )")
    conn.commit()
conn.close()



# ----------------------------------------------------------------
# This iterates through the file list and grabs each file
# with the .txt type and enters them into the table under FileName
# ----------------------------------------------------------------
print("Search results for .txt files: \n")

for i in fileList:
    if '.txt' in i:
        fileName = [i]
        conn = sqlite3.connect('file.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO Txt_Files(FileName) VALUES (?)", \
                           (fileName))
            conn.commit()
        conn.close()



# ----------------------------------------------------------------
# This is our query to retrieve all records under column 'FileName'
# ----------------------------------------------------------------
conn = sqlite3.connect('file.db')

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT FileName FROM Txt_Files")
    varFiles = cursor.fetchall()
    for item in varFiles:
        msg = "File Name: {}\n".format(item[0])
        print(msg)
conn.close()






