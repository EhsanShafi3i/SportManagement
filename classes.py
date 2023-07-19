import os
import json
import time


class Person:
    def __init__(self, name, lname, utype, uphnum, password):
        self.name = name
        self.lname = lname
        self.utype = utype
        self.uphnum = uphnum
        self.password = password


class Manager(Person):
    def __init__(self):
        with open("user.json", "r") as f:
            self.data = json.load(f)

    def print_members(self):
        with open("user.json", "r") as f:
            data = json.load(f)

        for user in data:
            if user["user type"] == "member":
                print(f"Name: {user['name']} Last Name: {user['last name']}")

    def remove_member(self, x):
        with open("user.json", "r") as file:
            self.data = json.load(file)

        self.x = x

        for i in range(len(self.data)):
            if x == f"{self.data[i]['name']} {self.data[i]['last name']}":
                del self.data[i]
                with open("user.json", "w") as file:
                    json.dump(self.data, file, indent=2)
                print("removed successfully")
                time.sleep(1)
                break
        else:
            print(f"There is no member that named {x}")
            print("try again")
            time.sleep(1)

    def add_member(self):
        os.system("cls")
        name = input("enter your user name : ")
        user_lname = input("enter your last name : ")
        user_name = input("enter your phone number or email : ")
        while len(user_name) == 0:
            print(
                """invalid
    try again"""
            )
            user_name = input("enter your phone number or email : ")
        password = input("password : ")
        while len(password) < 7:
            print("!!!your password should be at least 8 charcter!!!")
            password = input("password : ")
        user_type = "member"
        person = Person(name, user_lname, user_type, user_name, password)
        user_data = {
            "name": person.name,
            "last name": person.lname,
            "user type": person.utype,
            "user name": person.uphnum,
            "user password": person.password,
            "user wallet": 0,
        }
        with open("user.json", "r") as f:
            data = json.load(f)

        usernames = [user["user name"] for user in data]
        if user_name in usernames:
            print("This username already exists. Please choose a different username.")
            time.sleep(1)
        file_path = "user.json"

        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path, "r") as f:
                data = json.load(f)
                data.append(user_data)
        else:
            data = []
            data.append(user_data)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
        print("new member add successfully")
        z = input("Enter any key to continue")

    def facility_printer(self):
        pass

    def add_facility(self):
        pass

    def remove_facility(self):
        pass

    def coach_printer(self):
        for user in self.data:
            if user["user type"] == "coach":
                print(f"Name: {user['name']} Last Name: {user['last name']}")

    def add_coach(self):
        os.system("cls")
        name = input("enter your user name : ")
        user_lname = input("enter your last name : ")
        user_name = input("enter your phone number or email : ")
        while len(user_name) == 0:
            print(
                """invalid
    try again"""
            )
            user_name = input("enter your phone number or email : ")
        password = input("password : ")
        while len(password) < 7:
            print("!!!your password should be at least 8 charcter!!!")
            password = input("password : ")
        user_type = "coach"
        person = Person(name, user_lname, user_type, user_name, password)
        user_data = {
            "name": person.name,
            "last name": person.lname,
            "user type": person.utype,
            "user name": person.uphnum,
            "user password": person.password,
            "user wallet": 0,
        }
        with open("user.json", "r") as f:
            data = json.load(f)

        usernames = [user["user name"] for user in data]
        if user_name in usernames:
            print("This username already exists. Please choose a different username.")
            time.sleep(1)
        file_path = "user.json"

        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path, "r") as f:
                data = json.load(f)
                data.append(user_data)
        else:
            data = []
            data.append(user_data)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
        print("new couch add successfully")
        z = input("Enter any key to continue")

    def remove_coach(self, x):
        with open("user.json", "r") as file:
            self.data = json.load(file)

        self.x = x

        for i in range(len(self.data)):
            if x == f"{self.data[i]['name']} {self.data[i]['last name']}":
                del self.data[i]
                with open("user.json", "w") as file:
                    json.dump(self.data, file, indent=2)
                break
        else:
            print(f"There is no coach that named {x}")
            print("try again")
            time.sleep(0.5)

    def wallet_printer(self):
        with open("user.json", "r") as f:
            self.data = json.load(f)
        for user in self.data:
            if user["user type"] == "member":
                print(
                    f"Name: {user['name']} Last Name: {user['last name']} Wallet balance : {user['user wallet']}"
                )

    def add_wallet_balance(self, full_name, amount):
        with open("user.json", "r") as f:
            data = json.load(f)

        for user in data:
            if f"{user['name']} {user['last name']}" == full_name:
                user["user wallet"] += amount
                break
        with open("user.json", "w") as f:
            json.dump(data, f, indent=2)

    def deduct_wallet_balance(self, full_name, amount):
        with open("user.json", "r") as f:
            data = json.load(f)

        for user in data:
            if f"{user['name']} {user['last name']}" == full_name:
                user["user wallet"] -= amount
                break

        with open("user.json", "w") as f:
            json.dump(data, f, indent=2)

    def checker(self, full_name):
        with open("user.json", "r") as f:
            data = json.load(f)

        for user in data:
            if f"{user['name']} {user['last name']}" == full_name:
                return True
        return False


class Coach(Person):
    pass


class Member(Person):
    def __init__(self):
        with open("user.json", "r") as f:
            self.data = json.load(f)

    def watch_profile(self, x):
        with open("user.json", "r") as a:
            data = json.load(a)
        self.x = x
        for user in data:
            if x == f"{user['user name']} {user['user password']}":
                print("\n".join([f"{key}: {value}" for key, value in user.items()]))

    def wallet_printer(self, x):
        with open("user.json", "r") as f:
            data = json.load(f)
        for user in data:
            if x == f"{user['user name']} {user['user password']}":
                print(f"Wallet Balance :{user['user wallet']} $")

    def wallet_deposit(self, x, y):
        with open("user.json", "r") as f:
            data = json.load(f)
        for user in data:
            if x == f"{user['user name']} {user['user password']}":
                user["user wallet"] += y
        with open("user.json", "w") as f:
            json.dump(data, f, indent=2)
        print("The operation was successful")
        a = input("Press Enter")

    def wallet_withdraw(self, x, y):
        with open("user.json", "r") as f:
            data = json.load(f)

        for user in data:
            if x == f"{user['user name']} {user['user password']}":
                user["user wallet"] -= y
        with open("user.json", "w") as f:
            json.dump(data, f, indent=2)
        print("The operation was successful")
        a = input("Press Enter")

    def change_pass(self, x):
        with open("user.json", "r") as f:
            data = json.load(f)
        y = input("Enter new password : ")
        while len(y) < 8:
            print("Your password should be at least 8 characters long.")
            y = input("Enter your password: ")
        for user in data:
            if x == f"{user['user name']} {user['user password']}":
                user["user password"] = y
        with open("user.json", "w") as f:
            json.dump(data, f, indent=2)
        print("The operation was successful")
        a = input("Press Enter")

    def coach_list(self):
        with open("coaches.json", "r") as f:
            data = json.load(f)
        print("\n".join([f"name {name}" for name in data]))
        x = input("Press Enter to continue")

# manager = Manager()
# initial_balance = manager.data[0]["user wallet"]
# manager.add_wallet_balance("ehsan sh", 100)
# assert manager.data[0]["user wallet"] == initial_balance + 100


# initial_balance = manager.data[0]["user wallet"]
# manager.deduct_wallet_balance("ehsan sh", 50)
# assert manager.data[0]["user wallet"] == initial_balance - 50