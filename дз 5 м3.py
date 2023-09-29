import sqlite3
def delete_users_by_name(cursor, user_name):
    command = '''
DELETE FROM users WHERE name = ?;
'''
    cursor.execute(command,(user_name, ))
with sqlite3.connect('data.db') as cursor:
    delete_users_by_name(cursor,'Дмитрий')