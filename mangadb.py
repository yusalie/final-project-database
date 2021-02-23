import sqlite3
import base64

ecImg = ""

with open("pictures/Senryū_Shōjo_volume_1_cover.jpg","rb") as imageFile:
    ecImg = base64.b64encode(imageFile.read())

def init_sqlite_db():
    
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS manga (id INTEGER PRIMARY KEY AUTOINCREMENT,img TEXT, title TEXT, titleJp TEXT,written_by TEXT,published_by TEXT, genre TEXT, synopsis TEXT)')
    print("Table created successfully")
    insertImg = "INSERT INTO manga(img, title, titleJp, written_by, published_by, genre, synopsis) VALUES(?, ?, ?, ?, ?, ?, ?)" 
    imgdata = (str(ecImg),'Senryū Shōjo', '川柳少女','Masakuni Igarashi', 'Kodansha', 'Comedy Romance School Life Slice Of Life', 'lorem ispum')
    conn.execute(insertImg, imgdata)
    conn.commit()
    print("added")
    conn.close()

init_sqlite_db()
