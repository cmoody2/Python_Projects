
import sqlite3


fileList = ('information,docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('file.db')


with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Txt_Files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            FileName TEXT \
            )")
    conn.commit()
conn.close()




for i in fileList:
    if '.txt' in i:
        fileName = [i]
        conn = sqlite3.connect('file.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Txt_Files(FileName) VALUES (?)", \
                           (fileName))
            conn.commit()
        conn.close()


