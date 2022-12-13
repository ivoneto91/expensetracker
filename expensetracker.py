import os # os.system("cls")
from datetime import date

class Tracker: #where we will store the data
    def __init__(self):
        self.name = []
        self.date = []
        self.value = []
        self.installments = []
        self.category = []

class Expense: #where we will create the data
    def __init__(self,name,date,value,installments,category):
        self.name = str(name) 
        self.date = date
        self.value = float(value) 
        self.installments = int(installments)
        self.category = category

#This is the main menu
def startingmenu():
    print("    Expense Tracker Menu    \n") 
    print("Press 1 for add an expense")
    print("Press 2 for visualize expenses")
    print("Press 3 for exit")

#This is the menu with the expenses type
def categoryexpenses():
    print("    Creating a new expense    \n")
    print("Select 1 for Household expenses.")
    print("Select 2 for Food expenses.")
    print("Select 3 for Transport expenses.")
    print("Select 4 for Leisure expenses.")
    print("Select 5 for Health expenses.")
    print("Select 6 for Miscellaneous expenses.")

startingmenu()
menuans = int(input())
while menuans not in (1, 2, 3):
    print("Invalid Option. Please select 1, 2 or 3.")
    menuans = int(input())
else:
    if menuans == 1:
        os.system("cls")
        categoryexpenses()
        categoryans = int(input())
        while categoryans not in (1, 2, 3, 4, 5, 6,):
            print("Invalid Option. Press 1, 2, 3, 4, 5 or 6 to create a new expense.")
            categoryans = int(input())
        else:
            if categoryans == 1:
                os.system("cls")
                print("Adding a new Household expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        print("yfortest")
                    elif date.lower() in ("n", "no"):
                        #we will ask for user data
                        print("nfortest")
            elif categoryans == 2:
                os.system("cls")
                print("Adding a new Food expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        print("yfortest")
                    elif date.lower() in ("n", "no"):
                        #we will ask for user data
                        print("nfortest")
            elif categoryans == 3:
                os.system("cls")
                print("Adding a new Transport expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        print("yfortest")
                    elif date.lower() in ("n", "no"):
                        #we will ask for user data
                        print("nfortest")
            elif categoryans == 4:
                os.system("cls")
                print("Adding a new Leisure expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        print("yfortest")
                    elif date.lower() in ("n", "no"):
                        #we will ask for user data
                        print("nfortest")
            elif categoryans == 5:
                os.system("cls")
                print("Adding a new Health expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        print("yfortest")
                    elif date.lower() in ("n", "no"):
                        #we will ask for user data
                        print("nfortest")
            elif categoryans == 6:
                os.system("cls")
                print("Adding a new Miscellaneous expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        print("yfortest")
                    elif date.lower() in ("n", "no"):
                        #we will ask for user data
                        print("nfortest")         
    elif menuans == 2:
        #here we will generate reports
        print("ss2")
    elif menuans == 3:
        print("Thanks for using. See you next time : )")
        exit()





       
        