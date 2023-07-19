import os
import json
from classes import *
from defines import *
import time


while True:
    os.system("cls")
    print("1-sign up \n2-login ")
    x = input("-->")
    if x == "1":
        signup()
    elif x == "2":
        usertype = login()
        usernp = f"{usertype[1]} {usertype[2]}"
        # region login a manager
        if usertype[0] == "manager":
            while True:
                os.system("cls")
                print("login as manager")
                print("Manager Options:")
                print("1. Manage Members")
                print("2. Manage Facilities")
                print("3. Manage Coaches")
                print("4. Financial Management")
                print("5. Logout")

                option = input("Enter your choice: ")

                if option == "1":
                    manager = Manager()
                    while True:
                        os.system("cls")
                        print("1-show members\n2-add\n3-remove\n\n4-Back")
                        choise = input("-->")
                        if choise == "1":
                            manager.print_members()
                            d = input("enter any key to continue")
                        elif choise == "2":
                            manager.add_member()
                        elif choise == "3":
                            manager.print_members()
                            removed_person = pointer()
                            manager.remove_member(removed_person)

                        elif choise == "4":
                            break
                        else:
                            print("invalid entry")
                            time.sleep(0.5)
                elif option == "2":
                    while True:
                        os.system("cls")
                        print(
                            "1-show Facilities\n2-add Facilities\n3-remove Facilities\n\n4-back"
                        )
                        n = input("-->")
                        if n == "1":
                            pass
                        elif n == "2":
                            pass
                        elif n == "3":
                            pass
                        elif n == "4":
                            break
                        else:
                            print("invalid entry")
                            time.sleep(0.5)
                elif option == "3":
                    manager = Manager()
                    while True:
                        os.system("cls")
                        print(
                            "1-show coaches\n2-add coaches\n3-remove coaches\n\n4-back"
                        )
                        n = input("-->")
                        if n == "1":
                            manager.coach_printer()
                        elif n == "2":
                            manager.add_coach()
                        elif n == "3":
                            manager.coach_printer()
                            x = pointer()
                            manager.remove_coach(x)
                        elif n == "4":
                            break
                        else:
                            print("invalid entry")
                            time.sleep(0.5)
                elif option == "4":
                    manager = Manager()
                    while True:
                        os.system("cls")
                        print(
                            "1-Show member and their wallet balance\n2-Add to their wallet balance\n3-Deduct from wallet balance\n\n4-back"
                        )
                        q = input("-->")
                        if q == "1":
                            manager.wallet_printer()
                            d = input("enter any key to continue")
                        elif q == "2":
                            manager.wallet_printer()
                            point_person = pointer()
                            flag1 = True
                            while True:
                                if not flag1:
                                    break
                                if manager.checker(point_person):
                                    point_money = None
                                    while point_money is None:
                                        try:
                                            point_money = int(
                                                input(
                                                    "Amount of money you want to add: "
                                                )
                                            )
                                            manager.add_wallet_balance(
                                                point_person, point_money
                                            )
                                            flag1 = False
                                            break

                                        except ValueError:
                                            print(
                                                "Invalid input. Please enter a number."
                                            )
                                else:
                                    print("user not found")
                                    point_person = pointer()
                        elif q == "3":
                            manager.wallet_printer()
                            point_person = pointer()
                            flag2 = True
                            while True:
                                if not flag2:
                                    break
                                if manager.checker(point_person):
                                    point_money = None
                                    while point_money is None:
                                        try:
                                            point_money = int(
                                                input(
                                                    "Amount of money you want to add: "
                                                )
                                            )
                                            manager.deduct_wallet_balance(
                                                point_person, point_money
                                            )
                                            flag2 = False
                                            break

                                        except ValueError:
                                            print(
                                                "Invalid input. Please enter a number."
                                            )
                                else:
                                    print("user not found")
                                    point_person = pointer()
                        elif q == "4":
                            break
                        else:
                            print("invalid entry")
                            time.sleep(0.5)
                elif option == "5":
                    print("Logged out successfully.")
                    time.sleep(1)
                    os.system("cls")
                    break
                else:
                    print("Invalid option. Please try again.")
                    time.sleep(1)
        # endregion
        # region login a coach
        elif usertype[0] == "coach":
            while True:
                print("login as coach")
                print("Coach Options:")
                print("1. View Schedule")
                print("2. View Members")
                print("\n\n3. Logout")
                option = input("Enter your choice: ")

                if option == "1":
                    while True:
                        os.system("cls")
                        print("1-print your schedule\n2-change your schedule\n\n3-Back")
                        x = input("-->")
                        if x == "1":
                            pass
                        elif x == "2":
                            pass
                        elif x == "3":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            time.sleep(1)
                elif option == "2":
                    while True:
                        os.system("cls")
                        print(
                            "1-print your members list\n2-change your schedule\n\n3-Back"
                        )
                        x = input("-->")
                        if x == "1":
                            pass
                        elif x == "2":
                            pass
                        elif x == "3":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            time.sleep(1)
                elif option == "3":
                    print("Logged out successfully.")
                    time.sleep(1)
                    os.system("cls")
                    break
        # endregion
        # region login as member
        elif usertype[0] == "member":
            member = Member()
            while True:
                os.system("cls")
                print("Login as member")
                print("Member Options:")
                print("1. Reserve Facility")
                print("2. View Schedule")
                print("3. View Coach List")
                print("4. view profile")
                print("5. logout")

                option = input("Enter your choice: ")

                if option == "1":
                    while True:
                        os.system("cls")
                        print("1-print your facility\n2-reserve facility\n\n3-Back")
                        x = input("-->")
                        if x == "1":
                            pass
                        elif x == "2":
                            pass
                        elif x == "3":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            time.sleep(1)

                elif option == "2":
                    while True:
                        os.system("cls")
                        print("1-print your schedule\n2-change your schedule\n\n3-Back")
                        x = input("-->")
                        if x == "1":
                            pass
                        elif x == "2":
                            pass
                        elif x == "3":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            time.sleep(1)

                elif option == "3":
                    while True:
                        os.system("cls")
                        print("1-print coaches list\n2-change your coach\n\n3-Back")
                        x = input("-->")
                        if x == "1":
                            member.coach_list()
                        elif x == "2":
                            pass
                        elif x == "3":
                            break
                        else:
                            print("Invalid option. Please try again.")
                            time.sleep(1)

                elif option == "4":
                    while True:
                        os.system("cls")
                        print("1-Wallet\n2-change password\n\n3-Back")
                        p = input("-->")
                        if p == "1":
                            while True:
                                os.system("cls")
                                print(
                                    "1-Show Wallet Balance\n2-Deposit\n3-Withdraw\n\n4-Back"
                                )
                                j = input("-->")
                                if j == "1":
                                    member.wallet_printer(usernp)
                                    e = input("Press Enter")
                                elif j == "2":
                                    point_money = None
                                    while point_money is None:
                                        try:
                                            point_money = int(
                                                input(
                                                    "Amount of money you want to add: "
                                                )
                                            )
                                            member.wallet_deposit(usernp, point_money)
                                            break

                                        except ValueError:
                                            print(
                                                "Invalid input. Please enter a number."
                                            )
                                elif j == "3":
                                    point_money = None
                                    while point_money is None:
                                        try:
                                            point_money = int(
                                                input(
                                                    "Amount of money you want to withdraw: "
                                                )
                                            )
                                            member.wallet_withdraw(usernp, point_money)
                                            break

                                        except ValueError:
                                            print(
                                                "Invalid input. Please enter a number."
                                            )
                                elif j == "4":
                                    break
                                else:
                                    print("invalid")
                                    time.sleep(0.5)
                        elif p == "2":
                            member.change_pass(usernp)
                        elif p == "3":
                            break
                        else:
                            print("invalid")
                            time.sleep(0.5)
                elif option == "5":
                    print("Logged out successfully.")
                    time.sleep(1)
                    os.system("cls")
                    break

                else:
                    print("Invalid option. Please try again.")
        # endregion
    elif x != "1" and x != "2":
        j = input("Invalid input.Press any key to continue.")
