# main.py
from user import User
from datetime import datetime

def main():
    # Creating a user instance with proper datetime conversion
    user = User(
        user_id=1001,
        name="Gulum",
        surname="Manasova",
        email="manasovaguluma@gmail.com",
        password="Manasova2005@",
        birthday=datetime.strptime("2005-10-03", "%Y-%m-%d")  # Convert string to datetime
    )

    # Display user details
    print(user.get_details())

    # Display user age
    print("Age:", user.get_age())

if __name__ == "__main__":
    main()





