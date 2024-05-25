import sqlite3

from swagger_server.models.diary_entry import DiaryEntry

class DiaryDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()
    def __del__(self):
        self.close()
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS diaries
                             (date TEXT PRIMARY KEY, content TEXT)''')
        self.conn.commit()

    def get_all_diaries(self):
        self.cursor.execute("SELECT * FROM diaries")
        lst = self.cursor.fetchall()
        return [DiaryEntry(*row) for row in lst]

    def get_diary_by_date(self, date):
        self.cursor.execute("SELECT * FROM diaries WHERE date=?", (date,))
        one=self.cursor.fetchone()
        return DiaryEntry(one[0], one[1])

    def create_diary(self, diary_entry:DiaryEntry):
        self.cursor.execute("INSERT INTO diaries (date, content) VALUES (?, ?)",
                          (diary_entry._date, diary_entry._content))
        self.conn.commit()
        return diary_entry

    def update_diary(self, date, diary_entry:DiaryEntry):
        self.cursor.execute("UPDATE diaries SET content=? WHERE date=?",
                          (diary_entry._content, date))
        self.conn.commit()
        return diary_entry

    def close(self):
        self.conn.close()