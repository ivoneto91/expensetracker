import os # os.system("cls")


print("    Expense Tracker Menu    \n")
print("Press 1 for add an expense")
print("Press 2 for visualize expenses")
print("Press 3 for exit")
menuans = int(input())

while menuans != 1 or 2 or 3:
    print("Invalid Option. Please select 1, 2 or 3.")
    menuans = int(input())
    if menuans == 1:
        pass
    elif menuans == 2:
        pass
    elif menuans == 3:
        print("Thanks for using. See you next time : )")
        exit()




class Expense:
    def __init__(self,date,name,value,installments,category):
        self.date = date
        self.name = str(name) 
        self.value = float(value) 
        self.installments = int(installments)
        self.category = category
