import sqlite3

class SQLCon:
    def __init__(self):
        self.conn = sqlite3.connect('donations.db')
    def setup(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS donations (id varchar(255),username varchar(255) NOT NULL,donationcount int,PRIMARY KEY (username))")
        except:
            pass
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS prefixes (guildid varchar(255),prefix varchar(255) DEFAULT '!',PRIMARY KEY (prefix))")
        except: 
            pass
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS users (userid varchar(255),username varchar(255) NOT NULL, PRIMARY KEY (userid))")
        except:
            pass
        self.conn.commit()
    def UpdateUser(self,username,id):
        self.setup()
        cursor = self.conn.cursor()
        sql = "INSERT INTO donations VALUES ('" + str(id) + "','" +  username + "',1)"
        try:
            cursor.execute(sql)
        except:
            sql = "UPDATE donations SET donationcount = donationcount + 1 WHERE id='" + str(id) + "'"
            cursor.execute(sql)
            pass
        sql = "SELECT * FROM donations WHERE id='" + str(id) + "'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        val = rows[0][2]

        self.conn.commit()
        return val
    def UpdatePrefix(self,prefix,guild):
        self.setup()
        cursor = self.conn.cursor()
        sql = f"INSERT INTO prefixes VALUES ('{str(guild.id)}', '{prefix}')"
        try:
            cursor.execute(sql)
        except:
            sql = f"UPDATE prefixes SET prefix = '{prefix}' WHERE guildid='{str(guild.id)}'"
            cursor.execute(sql)
            pass
        self.conn.commit()

    def GetPrefix(self,guild):
        try:
            cursor = self.conn.cursor()
            sql = f"SELECT * FROM prefixes WHERE guildid='{str(guild.id)}'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            val = rows[0][1]
        except:
            val = "!"

        return val

    def AddUser(self,userid,username):
        try:
            cursor = self.conn.cursor()
            sql = f"INSERT INTO users VALUES ('{userid}','{username}')"
            cursor.execute(sql)
            self.conn.commit()
        except:
            self.setup()

    def GetUser(self,userid):
        try:
            cursor = self.conn.cursor()
            sql = f"SELECT * FROM users WHERE userid='{userid}'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            val = rows[0][1]
            return val
        except:
            pass

        return None

        