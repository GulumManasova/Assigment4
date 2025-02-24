import random
import re
from datetime import datetime

class UserUtil:
    @staticmethod
    def generate_user_id():
        year = datetime.today().year % 100
        return f"{year}{random.randint(100000, 999999)}"

    @staticmethod
    def generate_password():
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(characters) for _ in range(8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return False
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "@$!%*?&" for c in password)

        return has_lower and has_upper and has_digit and has_special

    # Test examples
    print(is_strong_password("Abc@1234"))  # True
    print(is_strong_password("abc12345"))  # False

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        return bool(re.match(r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$', email))