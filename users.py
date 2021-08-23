import sqlite3
conn = sqlite3.connect("users.db")

users = [
    ('jack123', 'jsdEHdjf'),
    ('janepretty444', 'jssadff'),
    ('bob123', '30349jjs')
]

user_name = input('Username: ')
user_password = input('Password: ')

select_query = "SELECT * FROM users WHERE user_name= ? AND user_pass = ?"

cursor = conn.cursor()
cursor.execute(select_query, (user_name, user_password))
data = cursor.fetchone()

if(data):
    print("You are logged in!")
else:
    print("Please try again")

conn.commit()

conn.close()
