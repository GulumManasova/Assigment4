from datetime import datetime

class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.__email = email  # Private attribute
        self.__password = password  # Private attribute
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name} {self.surname}, Birthday: {self.birthday}"

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

    def set_email(self, new_email):
        self.__email = new_email

    def get_email(self):
        return self.__email

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


