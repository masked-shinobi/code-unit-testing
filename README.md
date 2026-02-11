# Unit Testing Project

This project demonstrates various unit testing techniques in Python using `pytest` and `mocker`.

## Source Code (`main.py`)

```python
# # def get_weather(temp):
# #     if temp > 20:
# #         return "hot"
# #     else:
# #         return "cold"
#    
# def add(a, b):
#     return a + b

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot be divided by zero")
#     else:
#         return a / b

# class UserManager:
#     def __init__(self):
#         self.users = {}
#        
#     def add_user(self, username, email):
#         if username in self.users:
#             raise ValueError("User exists")
#         self.users[username] = email
#         return True
#    
#     def get_user(self, username):
#         return self.users.get(username)

# import pytest
# class Database:
#     def __init__(self):
#         self.data = {}
#        
#     def add_user(self, user_id, name):
#         if user_id in self.data:
#             raise ValueError("User exists")
#         self.data[user_id] = name

#     def get_user(self, user_id):
#         return self.data.get(user_id, None)
#        
#     def delete_user(self, user_id):
#         if user_id in self.data:
#             del self.data[user_id]

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# import requests

# def get_weather(city):
#     response = requests.get(f"https://api.weather.com/v1/{city}")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise ValueError("Could not Fetch anything")

import sqlite3

def save_user(name, age):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", (name, age))
    conn.commit()
    conn.close()
```

## Testing Code (`test_main.py`)

```python
# # from main import get_weather

# # def test_get_weather():
# #     assert get_weather(21) == "hot"
# #     assert get_weather(21) == "cold"

# from main import add, divide
# import pytest

# def test_add():
#     assert add(2,3) == 5, "2 + 3 should be 5"
#    
# def test_divide():
#     with pytest.raises(ValueError, match="Cannot be divided by zero"):
#         divide(4, 0)


# import pytest
# from main import UserManager
# @pytest.fixture
# def user_manager():
#     return UserManager()

# def test_add_user(user_manager):
#     assert user_manager.add_user("sanjay", "sanjaybaskar.in@gmail.com") == True
#     assert user_manager.get_user("sanjay") == "sanjaybaskar.in@gmail.com"
#    
# def test_add_duplicate_user(user_manager):
#     user_manager.add_user("sanjay", "sanjaybaskar.in@gmail.com")
#     with pytest.raises(ValueError):
#         user_manager.add_user("sanjay", "sanjaybaskar.in@gmail.com")

# import pytest
# from main import Database

# @pytest.fixture
# def db():
#     database = Database()
#     yield database
#     database.data.clear()
#    
# def test_add_user(db):
#     db.add_user(1, "Alice")
#     assert db.get_user(1) == "Alice"
#    
# def test_add_duplicate_user(db):
#     db.add_user(1, "Alice")
#     with pytest.raises(ValueError, match="User exists"):
#         db.add_user(1, "Bob")

# def test_delete_user(db):
#     db.add_user(2, "Bob")
#     db.delete_user(2)
#     assert db.get_user(2) is None

# import pytest
# from main import is_prime

# @pytest.mark.parametrize("num, expected", [
#     (3, True),
#     (4, False),
#     (7, True),
# ])

# def test_is_prime(num, expected):
#     assert is_prime(num) == expected

# import pytest
# from main import get_weather

# def test_get_weather(mocker):
#     mock_get = mocker.patch("main.requests.get")
#    
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = {"temperature":25, "condition":"sunny"}
#    
#     result = get_weather("Dubai")
#    
#     assert result == {"temperature":25, "condition":"sunny"}
#    
#     mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")

import pytest
from main import save_user

def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value
    
    save_user("Alice",30)
    
    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?,?)", ("Alice", 30)
    )
    
# actual code for advances for class is mocker.Mock()
```
