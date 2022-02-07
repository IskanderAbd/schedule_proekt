import json

users = []

with open('../db.json', 'r+') as f:
    python_data = json.load(f)
    # print(python_data)
    users = python_data['users']


def send_message(users):
    for user in users:
        if int(user['age']) >=18:
            print(f"Hello, {user['name']} We have special offer for you!")

send_message(users)