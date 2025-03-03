import unittest
from user import User
from user_service import UserService
from datetime import datetime

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(user_id=123456789, name="Gulum", surname="Mansaova", email="test@example.com",
                         password="StrongPass1!", birthday=datetime(2005, 10, 3))
        UserService.add_user(self.user)

    def test_add_user(self):
        self.assertEqual(len(UserService.users), 1)

    def test_find_user(self):
        found_user = UserService.find_user(123456789)
        self.assertIsNotNone(found_user)

    def test_delete_user(self):
        UserService.delete_user(123456789)
        self.assertIsNone(UserService.find_user(123456789))

    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 1)

if __name__ == '__main__':
    unittest.main()
import unittest
from datetime import datetime
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(user_id=123456789, name="Gulum", surname="Mansaova", email="test@example.com",
                         password="StrongPass1!", birthday=datetime(2005, 10, 3))

    def test_get_details(self):
        self.assertIn("Gulum Mansaova", self.user.get_details())

    def test_get_age(self):
        age = self.user.get_age()
        self.assertTrue(age > 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from user_util import UserUtil

class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(str(user_id)), 8, f"Generated user_id: {user_id}")

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password), f"Generated password: {password}")

    def test_is_strong_password(self):
        self.assertFalse(UserUtil.is_strong_password("abc123"))
        self.assertFalse(UserUtil.is_strong_password("PASSWORD1"))
        self.assertTrue(UserUtil.is_strong_password("Str0ng@Pass!"))

    def test_generate_email(self):
        email = UserUtil.generate_email("Gulum", "Mansaova", "example.com")
        self.assertEqual(email, "gulum.mansaova@example.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("test.user@example.com"))
        self.assertFalse(UserUtil.validate_email("test.user@com"))

if __name__ == '__main__':
    unittest.main()

