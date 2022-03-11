import sqlite3

def gentables():
        charbase = sqlite3.connect("/home/brendan/KelBot/utils/charbase.db")
        charcursor = charbase.cursor()

        charcursor.execute("""CREATE TABLE IF NOT EXISTS users (
        userid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        username text NOT NULL UNIQUE
        )""")

        charcursor.execute("""CREATE TABLE IF NOT EXISTS chars (
            ogcharid integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            charname text NOT NULL,
            charclass text NOT NULL,
            charlevel integer NOT NULL,
            charhealth integer NOT NULL,
            userid integer NOT NULL,
            FOREIGN KEY(userid) REFERENCES users(id)
        )
        """)

        charcursor.execute("""CREATE TABLE IF NOT EXISTS charstats (
            strength integer NOT NULL,
            dexterity integer NOT NULL,
            constitution integer NOT NULL,
            intelligence integer NOT NULL,
            wisdom integer NOT NULL,
            charisma integer NOT NULL,
            charid integer NOT NULL,
            FOREIGN KEY(charid) REFERENCES chars(ogcharid)
        )
        """)
        charbase.commit()
        charbase.close()
        return
def viewtable(db):
    charcursor = db.cursor()
    charcursor.execute("SELECT username FROM users")
    for i in charcursor.fetchone():
        print(i)

def tableinsert(user_name,charname,charclass,charlevel,charhealth,stre,dex,con,int,wis,cha):
    gentables()
    db=sqlite3.connect("/home/brendan/KelBot/utils/charbase.db")
    charcursor = db.cursor()
    charcursor.execute("SELECT charname FROM chars WHERE charname=?",(charname,))
    check = charcursor.fetchone()
    print(check)
    if check is None:
        
        charcursor.execute("INSERT OR IGNORE INTO users VALUES (NULL,?)",(user_name,))
        charcursor.execute("SELECT userid from users WHERE username=?",(user_name,))
        print(user_name)
        temp=charcursor.fetchone()
        userid=temp[0]
        charcursor.execute("INSERT INTO chars VALUES (NULL,?,?,?,?,?)",(charname,charclass,charlevel,charhealth,userid,))
        charidhold=charcursor.lastrowid
        db.commit()
        charcursor.execute("INSERT INTO charstats VALUES (?,?,?,?,?,?,?)",(stre,dex,con,int,wis,cha,charidhold,))
        db.commit()
        viewtable(db)
        db.close()
    else:
        print("already in database")
    return

def searchbychar(name):
    db=sqlite3.connect("/home/brendan/KelBot/utils/charbase.db")
    charcursor=db.cursor()
    charcursor.execute("SELECT charname FROM chars WHERE charname=?",(name,))
    check=charcursor.fetchone()
    return check

def deletechar(name):
    db=sqlite3.connect("/home/brendan/KelBot/utils/charbase.db")
    charcursor=db.cursor()
    charcursor.execute("SELECT charid FROM chars WHERE charname=?"(name,))
    charid=charcursor.fetchone()
    charcursor.execute("DELETE FROM charstats WHERE ogcharid=?"(charid,))
    db.commit()
    charcursor.execute("DELETE FROM chars WHERE charname=?",(name,))
    return
    #NOTE: DELETE USER DATA ATTACHED TO IT AS WELL