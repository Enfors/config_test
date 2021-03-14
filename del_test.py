#!/usr/bin/env python3

user1 = "Birk"
user2 = "Borkason"

user_list = [user1, user2]

print(f"User list: {user_list}")
print(f"User1: {user1}")
print("--------------------------")
print("Deleting user1.")
del user1
print("The 'user1' identifier (but not its value) is now deleted.")
print("The reference to user1 value is still in user_list:")
print(f"User list: {user_list}")
print("But referring to the variable 'user1' now produces an error:")
print(f"User1: {user1}")
