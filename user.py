# user.py
from datetime import datetime


class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}"

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age


# user_service.py
class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id].__dict__.update(user_update.__dict__)

    @classmethod
    def get_number(cls):
        return len(cls.users)


# user_util.py
import random
import re
from datetime import datetime


class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.now().year)[2:]
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        import string
        import secrets

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(8))
        return password

    @staticmethod
    def is_strong_password(password):
        return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


