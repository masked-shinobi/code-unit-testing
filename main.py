# # def get_weather(temp):
# #     if temp > 20:
# #         return "hot"
# #     else:
# #         return "cold"
    
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
        
#     def add_user(self, username, email):
#         if username in self.users:
#             raise ValueError("User exists")
#         self.users[username] = email
#         return True
    
#     def get_user(self, username):
#         return self.users.get(username)

# import pytest
# class Database:
#     def __init__(self):
#         self.data = {}
        
#     def add_user(self, user_id, name):
#         if user_id in self.data:
#             raise ValueError("User exists")
#         self.data[user_id] = name

#     def get_user(self, user_id):
#         return self.data.get(user_id, None)
        
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