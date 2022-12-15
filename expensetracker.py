import os # os.system("cls")
from datetime import date
from dateutil import parser

today_date = date.today()
date_format = "%d/%m/%y"
correct_format_date = today_date.strftime(date_format)
print(correct_format_date)

#maybe i can create dicts with key generated from a counter.
class Tracker: #where we will store the data (dataclasses module?)
    def __init__(self):
        self.code = []
        self.name = []
        self.date = []
        self.value = []
        self.installments = []
        self.category = []


initial = Tracker() #this variable will store data.

class Expense: #where we will create the data
    counter = 1
    
    def __init__(self,name,date,value,installments,category):
        self.code = Expense.counter
        self.name = str(name) 
        self.date = date
        self.value = float(value) 
        self.installments = int(installments)
        self.category = category
        print(f"Expense created successfully with code {self.code}.")
        Expense.counter += 1
        initial.code.append(int(self.code))
        initial.name.append(str(self.name))
        initial.date.append(self.date)
        initial.value.append(float(self.value))
        initial.installments.append(int(self.installments))
        initial.category.append(self.category)
        


#This is the main menu
def startingmenu():
    print("    Expense Tracker Menu    \n") 
    print("Press 1 for Add an expense")
    print("Press 2 for Visualize expenses")
    print("Press 3 for Exit")

#This is the menu with the expenses type
def categoryexpenses():
    print("    Creating a new expense    \n")
    print("Select 1 for Household expenses.")
    print("Select 2 for Food expenses.")
    print("Select 3 for Transport expenses.")
    print("Select 4 for Leisure expenses.")
    print("Select 5 for Healthcare expenses.")
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
        while categoryans not in (1, 2, 3, 4, 5, 6):
            print("Invalid Option. Press 1, 2, 3, 4, 5 or 6 to create a new expense.")
            categoryans = int(input())
        else:
            if categoryans == 1: #creating household expense
                rep = True
                while rep is True: # this while enable create another expense after the first one.
                    os.system("cls")
                    print("Adding a new Household expense.")
                    date = input("Did you made this expense today?(Y/N): ")
                    while date.lower() not in ("y", "yes", "n", "no"):
                        print("Wrong Input. Select Y or N.")
                        date = input("Did you made this expense today?(Y/N): ")
                    else:
                        if date.lower() in ("y", "yes"):
                            #we will import date from module.
                            tempname = input("What was your expense? ")
                            tempvalue = input("What was the value? $")
                            while True:
                                try:
                                    float(tempvalue)
                                except ValueError: 
                                    print("You didnt insert a value.(xx.xx)")
                                    tempvalue = input("What was the value? $:")
                                else:
                                    break

                            tempinstallments = input("How many installments? ")
                            while True:
                                try:
                                    float(tempinstallments)
                                except:                         
                                    print("You didnt insert a number.")
                                    tempinstallments = input("How many installments? ")
                                else:
                                    break

                            temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Household")
                            print("Do you wanna create another expense? (Y/N)")
                            rep1 = input()
                            if rep1.lower() in ("y", "yes"):
                                rep = True
                            elif rep1.lower() in ("n", "no"):
                                rep = False
                        elif date.lower() in ("n", "no"):
                            tempname = input("What was your expense? ")
                            tempdate = input("When you made this expense? (DD/MM/YY) ")
                            while True:
                                try:
                                    bool(parser.parse(tempdate))
                                except ValueError:
                                    print("Incorrect data format. Insert DD/MM/YY")
                                    tempdate = input("When you made this expense? (DD/MM/YY) ")
                                else:
                                    break

                            tempvalue = input("What was the value? $")
                            while True:
                                try:
                                    float(tempvalue)
                                except ValueError: 
                                    print("You didnt insert a value.(xx.xx)")
                                    tempvalue = input("What was the value? $:")
                                else:
                                    break

                            tempinstallments = input("How many installments? ")
                            while True:
                                try:
                                    float(tempinstallments)
                                except:                         
                                    print("You didnt insert a number.")
                                    tempinstallments = input("How many installments? ")
                                else:
                                    break 

                            temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Household")
                            print("Do you wanna create another expense? (Y/N)")
                            rep1 = input()
                            if rep1.lower() in ("y", "yes"):
                                rep = True
                            elif rep1.lower() in ("n", "no"):
                                print("Press 1 if you want to return to Main Meno or 2 for exit the program.")
                                exitquest = int(input())
                                if exitquest == 1:
                                    startingmenu()
                                    menuans = input()
                                else:
                                    break
                                
                                
            elif categoryans == 2: #creating food expense
                os.system("cls")
                print("Adding a new Food expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        tempname = input("What was your expense? ")
                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break

                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Food")
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        tempdate = input("When you made this expense? (DD/MM/YY) ")
                        while True:
                            try:
                                bool(parser.parse(tempdate))
                            except ValueError:
                                print("Incorrect data format. Insert DD/MM/YY")
                                tempdate = input("When you made this expense? (DD/MM/YY) ")
                            else:
                                break

                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break 

                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Food")
            elif categoryans == 3: #creating transport expense
                os.system("cls")
                print("Adding a new Transport expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        tempname = input("What was your expense? ")
                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break

                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Transport")
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        tempdate = input("When you made this expense? (DD/MM/YY) ")
                        while True:
                            try:
                                bool(parser.parse(tempdate))
                            except ValueError:
                                print("Incorrect data format. Insert DD/MM/YY")
                                tempdate = input("When you made this expense? (DD/MM/YY) ")
                            else:
                                break

                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break 

                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Transport")
            elif categoryans == 4: #creating leisure expense
                os.system("cls")
                print("Adding a new Leisure expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        tempname = input("What was your expense? ")
                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break

                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Leisure")
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        tempdate = input("When you made this expense? (DD/MM/YY) ")
                        while True:
                            try:
                                bool(parser.parse(tempdate))
                            except ValueError:
                                print("Incorrect data format. Insert DD/MM/YY")
                                tempdate = input("When you made this expense? (DD/MM/YY) ")
                            else:
                                break

                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break 

                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Leisure")
            elif categoryans == 5: #creating health expense
                os.system("cls")
                print("Adding a new Healthcare expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        tempname = input("What was your expense? ")
                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break

                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Healthcare")
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        tempdate = input("When you made this expense? (DD/MM/YY) ")
                        while True:
                            try:
                                bool(parser.parse(tempdate))
                            except ValueError:
                                print("Incorrect data format. Insert DD/MM/YY")
                                tempdate = input("When you made this expense? (DD/MM/YY) ")
                            else:
                                break

                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break 

                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Healthcare")
            elif categoryans == 6: #creating misc expense
                os.system("cls")
                print("Adding a new Miscellaneous expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"):
                        #we will import date from module.
                        tempname = input("What was your expense? ")
                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break

                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Miscellaneous")
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        tempdate = input("When you made this expense? (DD/MM/YY) ")
                        while True:
                            try:
                                bool(parser.parse(tempdate))
                            except ValueError:
                                print("Incorrect data format. Insert DD/MM/YY")
                                tempdate = input("When you made this expense? (DD/MM/YY) ")
                            else:
                                break

                        tempvalue = input("What was the value? $")
                        while True:
                            try:
                                float(tempvalue)
                            except ValueError: 
                                print("You didnt insert a value.(xx.xx)")
                                tempvalue = input("What was the value? $:")
                            else:
                                break

                        tempinstallments = input("How many installments? ")
                        while True:
                            try:
                                float(tempinstallments)
                            except:                         
                                print("You didnt insert a number.")
                                tempinstallments = input("How many installments? ")
                            else:
                                break

                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Miscellaneous")
    elif menuans == 2:
        #here we will generate reports
        print("ss2")
    elif menuans == 3:
        print("Thanks for using. See you next time : )")
        exit()





        