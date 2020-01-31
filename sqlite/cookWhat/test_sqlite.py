import sqlite3
import os.path

conn = sqlite3.connect('./XQDCook.db')
cursor = conn.cursor()

for x in range(100000):
    sql = '''insert into xhs_recipes
      (title, image_url)
      values
      ('测试', 'https://www.google.com')'''
    cursor.execute(sql)
    conn.commit()
    pass
