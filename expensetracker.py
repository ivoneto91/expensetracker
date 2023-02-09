import os # os.system("cls")
from datetime import date
from dateutil import parser
import sqlite3 as db

today_date = date.today()
date_format = "%d/%m/%y"
correct_format_date = today_date.strftime(date_format)

def initsql(): #lets see...
    conn = db.connect("expenses.db")    
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        code INTEGER,
        name TEXT,
        date DATE,
        value REAL,
        installments INTEGER,
        category TEXT
        )
    '''
    cur.execute(sql)
    conn.commit()

class Expense: 
    counter = 1
    
    def __init__(self, name, date, value, installments, category):
        conn = db.connect("expenses.db")    
        cur = conn.cursor()
        cur.execute("SELECT max(code) from expenses")
        result = cur.fetchone()
        if result[0] is not None:
            self.counter = result[0] + 1
        self.code = self.counter
        self.name = str(name) 
        self.date = date
        self.value = float(value)
        self.installments = int(installments)
        self.category = category
        self.conn = db.connect('expenses.db')
        self.cursor = self.conn.cursor()
        sql1 = f"INSERT INTO expenses(code, name, date, value, installments, category) VALUES({self.code}, '{self.name}', '{self.date}', {self.value}, {self.installments}, '{self.category}')"
        self.cursor.execute(sql1)
        self.conn.commit()
        print(f"Expense created successfully with code {self.code}.")
        self.counter += 1

temp = ""
tempname = ""
tempvalue = 0
tempinstallments = 0
tempdate = ""

def menuvalue(): #use this function when need input value
    global tempvalue
    tempvalue = input("What was the value? $")
    while True:
        try:
            float(tempvalue)
        except ValueError: 
            print("You didnt insert a value.(xx.xx)")
            menuvalue()
        else:
            return tempvalue

def menuinstallments(): #input installments
    global tempinstallments
    tempinstallments = input("How many installments? ")
    while True:
        try:
            int(tempinstallments)
        except:                         
            print("You didnt insert a number.")
            menuinstallments()
        else:
            return tempinstallments

def menudate(): #input date
    global tempdate
    tempdate = input("When you made this expense? (DD/MM/YY) ")
    while True:
        try:
            bool(parser.parse(tempdate))
        except ValueError:
            print("Incorrect data format. Insert DD/MM/YY")
            menudate()
        else:
            return tempdate

#This is the main menu
def startingmenu():
    os.system("cls")
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

def creationmenu():
    global temp
    os.system("cls")
    categoryexpenses()
    categoryans = int(input())
    while categoryans not in (1, 2, 3, 4, 5, 6):
        print("Invalid Option. Press 1, 2, 3, 4, 5 or 6 to create a new expense.")
        categoryans = int(input())
    else:
        if categoryans == 1: #creating household expense
            rep = True
            while rep is True: #this while enable create another expense after the first one.
                os.system("cls")
                print("Adding a new Household expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"): #in this case we will import date from module.
                        tempname = input("What was your expense? ")
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Household")
                        print("Do you wanna create another Household expense? (Y/N)")
                        rep1 = input()
                        if rep1.lower() in ("y", "yes"):
                            rep = True
                        elif rep1.lower() in ("n", "no"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        menudate()
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Household")
                        print("Do you wanna create another Household expense? (Y/N)")
                        rep2 = input()
                        if rep2.lower() in ("y", "yes"):
                            rep = True
                        elif rep2.lower not in ("y", "yes"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
        if categoryans == 2: #creating food expense
            rep = True
            while rep is True: #this while enable create another expense after the first one.
                os.system("cls")
                print("Adding a new Food expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"): #in this case we will import date from module.
                        tempname = input("What was your expense? ")
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Food")
                        print("Do you wanna create another Food expense? (Y/N)")
                        rep1 = input()
                        if rep1.lower() in ("y", "yes"):
                            rep = True
                        elif rep1.lower() in ("n", "no"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        menudate()
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Food")
                        print("Do you wanna create another Food expense? (Y/N)")
                        rep2 = input()
                        if rep2.lower() in ("y", "yes"):
                            rep = True
                        elif rep2.lower not in ("y", "yes"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
        if categoryans == 3: #creating transport expense
            rep = True
            while rep is True: #this while enable create another expense after the first one.
                os.system("cls")
                print("Adding a new Transport expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"): #in this case we will import date from module.
                        tempname = input("What was your expense? ")
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Transport")
                        print("Do you wanna create another Transport expense? (Y/N)")
                        rep1 = input()
                        if rep1.lower() in ("y", "yes"):
                            rep = True
                        elif rep1.lower() in ("n", "no"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        menudate()
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Transport")
                        print("Do you wanna create another Transport expense? (Y/N)")
                        rep2 = input()
                        if rep2.lower() in ("y", "yes"):
                            rep = True
                        elif rep2.lower not in ("y", "yes"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
        if categoryans == 4: #creating leisure expense
            rep = True
            while rep is True: #this while enable create another expense after the first one.
                os.system("cls")
                print("Adding a new Leisure expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"): #in this case we will import date from module.
                        tempname = input("What was your expense? ")
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Leisure")
                        print("Do you wanna create another Leisure expense? (Y/N)")
                        rep1 = input()
                        if rep1.lower() in ("y", "yes"):
                            rep = True
                        elif rep1.lower() in ("n", "no"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        menudate()
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Leisure")
                        print("Do you wanna create another Leisure expense? (Y/N)")
                        rep2 = input()
                        if rep2.lower() in ("y", "yes"):
                            rep = True
                        elif rep2.lower not in ("y", "yes"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
        if categoryans == 5: #creating Healthcare expense
            rep = True
            while rep is True: #this while enable create another expense after the first one.
                os.system("cls")
                print("Adding a new Healthcare expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"): #in this case we will import date from module.
                        tempname = input("What was your expense? ")
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Healthcare")
                        print("Do you wanna create another Healthcare expense? (Y/N)")
                        rep1 = input()
                        if rep1.lower() in ("y", "yes"):
                            rep = True
                        elif rep1.lower() in ("n", "no"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        menudate()
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Healthcare")
                        print("Do you wanna create another Healthcare expense? (Y/N)")
                        rep2 = input()
                        if rep2.lower() in ("y", "yes"):
                            rep = True
                        elif rep2.lower not in ("y", "yes"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
        if categoryans == 6: #creating Miscellaneous expense
            rep = True
            while rep is True: #this while enable create another expense after the first one.
                os.system("cls")
                print("Adding a new Miscellaneous expense.")
                date = input("Did you made this expense today?(Y/N): ")
                while date.lower() not in ("y", "yes", "n", "no"):
                    print("Wrong Input. Select Y or N.")
                    date = input("Did you made this expense today?(Y/N): ")
                else:
                    if date.lower() in ("y", "yes"): #in this case we will import date from module.
                        tempname = input("What was your expense? ")
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, correct_format_date, tempvalue, tempinstallments, "Miscellaneous")
                        print("Do you wanna create another Miscellaneous expense? (Y/N)")
                        rep1 = input()
                        if rep1.lower() in ("y", "yes"):
                            rep = True
                        elif rep1.lower() in ("n", "no"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
                    elif date.lower() in ("n", "no"):
                        tempname = input("What was your expense? ")
                        menudate()
                        menuvalue()
                        menuinstallments()
                        temp = Expense(tempname, tempdate, tempvalue, tempinstallments, "Miscellaneous")
                        print("Do you wanna create another Miscellaneous expense? (Y/N)")
                        rep2 = input()
                        if rep2.lower() in ("y", "yes"):
                            rep = True
                        elif rep2.lower not in ("y", "yes"):
                            print("Press 1 if you want to return to Main Menu, 2 if you want to create another expense in a different category and 3 for exit the program.")
                            exitquest = int(input())
                            rep = False
                            if exitquest == 1:
                                mainmenu()
                            if exitquest ==2:
                                creationmenu()
                            else:
                                exit()
    

def mainmenu():
    startingmenu()
    menuans = int(input())
    while menuans not in (1, 2, 3):
        print("Invalid Option. Please select 1, 2 or 3.")
        menuans = int(input())
    else:
        if menuans == 1:
            creationmenu()
        elif menuans == 2: #here we will generate reports
            print("ss2")
        elif menuans == 3:
            print("Thanks for using. See you next time : )")
            exit()

initsql()
mainmenu()

                                                        