from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil

# Create a user
user1 = User(
    user_id=UserUtil.generate_user_id(),
    name="Gulum",
    surname="Mansaova",
    email="manasovaguluma@gmail.com",
    password=UserUtil.generate_password(),
    birthday=datetime(2005, 10, 3)
)

# Display user details
print("User Details:", user1.get_details())

# Check user age
print("User Age:", user1.get_age())

# Add user to UserService
UserService.add_user(user1)
print("Total Users:", UserService.get_number())

# Find user
found_user = UserService.find_user(user1.user_id)
print("Found User:", found_user.get_details() if found_user else "User not found")

# Validate email
is_valid_email = UserUtil.validate_email(user1.email)
print("Is Email Valid?", is_valid_email)
