import json
import os
import time
import re
from classes import Person
from defines import *


# region signup

def signup():
    os.system("cls")
    name = input("Enter your username: ")
    user_lname = input("Enter your last name: ")
    with open("user.json", "r") as f:
        data = json.load(f)
    usernames = [f'{user["name"]} {user["last name"]}' for user in data]
    if f"{name} {user_lname}" in usernames:
        print("This username already exists. Please choose a different username.")
        time.sleep(1)
        signup()
    user_type = input("Enter your user type (manager, coach, member): ").lower()
    while user_type not in ["manager", "coach", "member"]:
        user_type = input("Invalid user type. Enter again (manager, coach, member): ")
    user_name = input("Enter your phone number or email: ")
    while not (re.match(r'^[0-9]{11}$', user_name) or re.match(r'^[\w.-]+@\w+\.\w+$', user_name)):
        print("Invalid input. Please try again.")
        user_name = input("Enter your phone number or email: ")
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Your password should be at least 8 characters long.")
        password = input("Enter your password: ")
    person = Person(name, user_lname, user_type, user_name, password)
    user_data = {
        "name": person.name,
        "last name": person.lname,
        "user type": person.utype,
        "user name": person.uphnum,
        "user password": person.password,
        "user wallet": 0,
        "user coach": "",
    }
    if os.path.exists("user.json") and os.stat("user.json").st_size > 0:
        with open("user.json", "r") as f:
            data = json.load(f)
            data.append(user_data)
    else:
        data = [user_data]
    with open("user.json", "w") as f:
        json.dump(data, f, indent=2)
    if user_type == "coach":
        coaches_file_path = "coaches.json"
        coaches_data = []
        if os.path.exists(coaches_file_path) and os.stat(coaches_file_path).st_size > 0:
            with open(coaches_file_path, "r") as f:
                coaches_data = json.load(f)
                coaches_data.append(person.name)
            with open(coaches_file_path, "w") as f:
                json.dump(coaches_data, f, indent=2)
                print("Coach added successfully!")
        else:
            coaches_data = [person.name]
            with open(coaches_file_path, "w") as f:
                json.dump(coaches_data, f, indent=2)
                print("Coach added successfully!")
    return


# endregion
# region login
def login():
    os.system("cls")
    user_name = input("Enter your phone number or email: ")
    password = input("Enter your password: ")
    os.system("cls")
    with open("user.json", "r") as f:
        data = json.load(f)
    usertype = None
    for user in data:
        if user["user name"] == user_name and user["user password"] == password:
            usertype = user["user type"]
            break
    else:
        usertype = None
        print("User not found")
        print("please try again")
        time.sleep(0.75)
        login()
    return [usertype,user_name,password]


# endregion




def pointer():
    point_name = input("enter name : ")
    point_lname = input("enter last name : ")
    return f"{point_name} {point_lname}"

