import sqlite3
from datetime import datetime, date
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
# faculty_name, group_name = cursor.execute("""SELECT faculty, group_name FROM User WHERE id = 1008414066""").fetchone()
print(datetime.now().isocalendar()[1] - 35)
print(date(2024, 9, 23).isocalendar()[1] - 35, date(2024, 9, 22).weekday())