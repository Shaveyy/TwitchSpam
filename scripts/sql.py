import sqlite3

class SQLCon:
    def __init__(self):
        self.conn = sqlite3.connect('donations.db')
    def setup(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS donations (id varchar(255),username varchar(255) NOT NULL,donationcount int,PRIMARY KEY (username))")
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
    

        