# main_user.py
from user import User
from user_service import UserService
from user_util import UserUtil
from datetime import datetime

# User input
name = input("Enter your name: ")
surname = input("Enter your surname: ")
domain = input("Enter email domain (e.g., example.com): ")
email = UserUtil.generate_email(name, surname, domain)
password = UserUtil.generate_password()
birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

# Creating a user
user = User(
    user_id=UserUtil.generate_user_id(),
    name=name,
    surname=surname,
    email=email,
    password=password,
    birthday=birthday
)

# Adding user to the service
UserService.add_user(user)

# Retrieving user details
print("\nUser Created Successfully!")
print(user.get_details())
print("Age:", user.get_age())

# Fetch user from service
found_user = UserService.find_user(user.user_id)
if found_user:
    print("User found:", found_user.get_details())

# Total users count
print("Total users:", UserService.get_number())

# Validate email
print("Is email valid?:", UserUtil.validate_email(user.email))

# Check password strength
print("Is password strong?:", UserUtil.is_strong_password(user.password))
