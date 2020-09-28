import sqlite3

conn = sqlite3.connect('names.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_names( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('names.db')

with conn:
    cur = conn.cursor()
    files = ('information.docx','Hellow.txt','myImage.png','myMovies.mpg','World.txt','data.pdf','myPhoto.jpg')
    length = len(files)
    for i in range(length):
        if files[i].endswith('.txt'):
            cur.execute("INSERT INTO tbl_names(col_files) VALUES (?)",[files[i]])
            print(files[i])
            
conn.commit()
conn.close()
