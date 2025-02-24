# User Management System

## Overview
This project is a user management system with classes and methods for managing user information, validating user credentials, and handling basic operations like adding, updating, and deleting users.

## Classes

### User
Represents a user with attributes like ID, name, surname, email, password, and birthday. Methods include getting user details, computing age, and more.

### UserService
Manages users, including adding, finding, deleting, and updating users. It also tracks the number of users.

### UserUtil
Provides utility functions for generating user IDs, passwords, emails, and validating them.

## Running the Tests

### Installation

1. Clone this repository.
2. Install dependencies (if any) using:
    ```
    pip install -r requirements.txt
    ```

3. Run the tests:
    ```
    python -m unittest discover
    ```

## Sample Runs

### Example 1:
```python
user = User(user_id=1001, name="Gulum", surname="Manasova", birthday=datetime(2005, 10, 3))
print(user.get_details())
