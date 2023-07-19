import tkinter as tk
from tkinter import messagebox
import os
import json
from classes import *
import time

import os
import json
from classes import *
from defines import *
import time


def clear_screen():
    os.system("cls")


def show_message_box(message):
    messagebox.showinfo("Message", message)




def clear_screen():
    os.system("cls")


def show_message_box(message):
    messagebox.showinfo("Message", message)


def signup():
    clear_screen()

    def submit():
        name = name_entry.get()
        last_name = last_name_entry.get()
        user_type = user_type_var.get()
        user_name = user_name_entry.get()
        password = password_entry.get()

        with open("user.json", "r") as f:
            data = json.load(f)
        usernames = [f'{user["name"]} {user["last name"]}' for user in data]
        if f"{name} {last_name}" in usernames:
            show_message_box(
                "This username already exists. Please choose a different username."
            )
            return

        person = Person(name, last_name, user_type, user_name, password)
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
            if (
                os.path.exists(coaches_file_path)
                and os.stat(coaches_file_path).st_size > 0
            ):
                with open(coaches_file_path, "r") as f:
                    coaches_data = json.load(f)
                    coaches_data.append(person.name)
                with open(coaches_file_path, "w") as f:
                    json.dump(coaches_data, f, indent=2)
                    show_message_box("Coach added successfully!")
            else:
                coaches_data = [person.name]
                with open(coaches_file_path, "w") as f:
                    json.dump(coaches_data, f, indent=2)
                    show_message_box("Coach added successfully!")

        root.destroy()

    root = tk.Tk()
    root.title("Sign Up")

    name_label = tk.Label(root, text="Enter your username:")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    last_name_label = tk.Label(root, text="Enter your last name:")
    last_name_label.pack()
    last_name_entry = tk.Entry(root)
    last_name_entry.pack()

    user_type_label = tk.Label(root, text="Enter your user type:")
    user_type_label.pack()
    user_type_var = tk.StringVar(root)
    user_type_var.set("manager")  # Default value
    user_type_optionmenu = tk.OptionMenu(
        root, user_type_var, "manager", "coach", "member"
    )
    user_type_optionmenu.pack()

    user_name_label = tk.Label(root, text="Enter your phone number or email:")
    user_name_label.pack()
    user_name_entry = tk.Entry(root)
    user_name_entry.pack()

    password_label = tk.Label(root, text="Enter your password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()

    root.mainloop()


def login():
    clear_screen()

    def submit():
        user_name = user_name_entry.get()
        password = password_entry.get()

        with open("user.json", "r") as f:
            data = json.load(f)

        user_type = None
        for user in data:
            if user["user name"] == user_name and user["user password"] == password:
                user_type = user["user type"]
                break
        else:
            show_message_box("User not found. Please try again.")
            return

        root.destroy()
        return [user_type, user_name, password]

    root = tk.Tk()
    root.title("Login")

    user_name_label = tk.Label(root, text="Enter your phone number or email:")
    user_name_label.pack()
    user_name_entry = tk.Entry(root)
    user_name_entry.pack()

    password_label = tk.Label(root, text="Enter your password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()

    root.mainloop()


def main_menu():
    clear_screen()

    def signup_button_clicked():
        signup()

    def login_button_clicked():
        usertype = login()
        if usertype == "manager":
            manager_menu()
        elif usertype == "coach":
            coach_menu()
        elif usertype == "member":
            member_menu()

    root = tk.Tk()
    root.title("Main Menu")

    signup_button = tk.Button(root, text="Sign Up", command=signup_button_clicked)
    signup_button.pack()

    login_button = tk.Button(root, text="Login", command=login_button_clicked)
    login_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main_menu()
