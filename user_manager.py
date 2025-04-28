import json
import os

class UserManager:
    def __init__(self, file_path='users.json'):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def load_users(self):
        if os.stat(self.file_path).st_size == 0:
            return []
        with open(self.file_path, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []
        return users

    def save_users(self, users):
        with open(self.file_path, 'w') as f:
            json.dump(users, f, indent=4)

    def register(self, username, password):
        users = self.load_users()
        for user in users:
            if user['username'] == username:
                return False  # Username already exists
        users.append({'username': username, 'password': password})
        self.save_users(users)
        return True

    def login(self, username, password):
        users = self.load_users()
        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
        return False
