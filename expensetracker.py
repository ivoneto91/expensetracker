import os # os.system("cls")

class Tracker:
    def __init__(self):
        self.name = []
        self.date = []
        self.value = []
        self.installments = []
        self.category = []

class Expense:
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
    print("Select 1 for Household expenses.")
    print("Select 2 for Food expenses.")
    print("Select 3 for Transport expenses.")
    print("Select 4 for Leisure expenses.")
    print("Select 5 for Health expenses.")
    print("Select 6 for Miscellaneous expenses.")



startingmenu()
menuans = int(input())
while menuans != 1 and menuans != 2 and menuans != 3:
    print("Invalid Option. Please select 1, 2 or 3.")
    menuans = int(input())
if menuans == 1:
    os.system("cls")
    categoryexpenses()
    categoryans = int(input())
    while categoryans != 1 and categoryans != 2 and categoryans != 3 and categoryans != 4 and categoryans != 5 and categoryans != 6:
        print("Invalid Option. Press 1, 2, 3, 4, 5 or 6 to create a new expense.")
        categoryans = int(input())
        if categoryans == 1:
            print("Adding a new Household expense.")
        elif categoryans == 2:
            print("Adding a new Food expense.")
        elif categoryans == 3:
            print("Adding a new Transport expense.")
        elif categoryans == 4:
            print("Adding a new Leisure expense.")
        elif categoryans == 5:
            print("Adding a new Health expense.")
        elif categoryans == 6:
            print("Adding a new Miscellaneous expense.")         
elif menuans == 2:
    print("ss2")
elif menuans == 3:
    print("Thanks for using. See you next time : )")
    exit()





       
        