import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
# faculty_name, group_name = cursor.execute("""SELECT faculty, group_name FROM User WHERE id = 1008414066""").fetchone()

faculty_name = cursor.execute('''SELECT faculty FROM User WHERE id = ?''', (1008414066, )).fetchone()[0]
print(faculty_name)