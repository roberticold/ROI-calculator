from os import system


class Property():
    def __init__(self, value=0):
        self.value = value
        self.monthly_expenses = {}
        self.out_of_pocket_expenses = {}
        self.rental_income = 0

    def totalmontlyexpenses(self):
        total_montly_expenses = sum([
            values for values in self.monthly_expenses.values()])
        return total_montly_expenses

    def rentalmonth(self):
        while True:
            try:
                self.rental_income = float(
                    input("For how much are you planning to rent the property (USD): "))
                break
            except:
                system("cls")
                print("Please enter a valid value")

    def totaloutofpocket(self):
        total_oop = sum([
            values for values in self.out_of_pocket_expenses.values()])
        return total_oop

    def outofpocketmethod(self):
        while True:
            print("Press -0- at any time to go back to the main menu")
            expense = input("Name of the expense: ")
            system("cls")
            if expense == "0":
                break
            while True:
                try:
                    oop = float(input(f"How much for the {expense} (USD): "))
                    system("cls")
                    break

                except:
                    system("cls")
                    print("Please enter a valid value")
            if expense == 0:
                break
            self.out_of_pocket_expenses[expense] = oop

    def monthlyexpenses(self):
        while True:
            print("Press -0- at any time to go back to the main menu")
            expense = input("Name of the expense: ")
            system("cls")
            if expense == "0":
                break
            while True:
                try:
                    oop = float(input(f"How much for the {expense} (USD): "))
                    system("cls")
                    break

                except:
                    system("cls")
                    print("Please enter a valid value")

            if expense == 0:
                break
            self.monthly_expenses[expense] = oop

    def housevalue(self):
        while True:
            try:
                self.value = float(
                    input("Please enter the value of the property (USD): "))
                break

            except:
                system("cls")
                print("Please enter a valid value")

    def cashflow(self):
        return (self.rental_income - self.totalmontlyexpenses())

    def roimethod(self):
        anualcashflow = self.cashflow()*12
        totalinvestment = self.totaloutofpocket()
        if totalinvestment == 0:
            return anualcashflow*100
        else:
            return round((anualcashflow/totalinvestment)*100, 2)

    def finalpage(self):
        if self.value != 0 and self.rental_income != 0 and len(self.monthly_expenses) != 0 and len(self.out_of_pocket_expenses) != 0:
            print("""
-------------------------------------------------------------------
Value of the property -
-----------------------
    """)
            print(f"Total: ${self.value}")
            print("""
-------------------------------------------------------------------
Montly Expenses -
-----------------
    """)
            for key, values in self.monthly_expenses.items():
                print(f'{key} ${values}')
            print(f"Total: ${self.totalmontlyexpenses()}")
            print("""
-------------------------------------------------------------------
Out Of Pocket Expenses -
------------------------
    """)
            for key, values in self.out_of_pocket_expenses.items():
                print(f'{key} ${values}')
            print(f"Total: ${self.totaloutofpocket()}")

            print("""
-------------------------------------------------------------------
Rent per month -
----------------
    """)
            print(f"Total: ${self.rental_income}")

            print("""
********************************************************************
Return of the investment *
**************************
    """)

            print(
                f"The return of your investment will be {self.roimethod()}% annualy")

            print("""
********************************************************************

    """)
            print(input("Press -Enter- to exit"))
            exit()

        else:
            print("Please add all the requested information before")


def main():

    print("""
     1- Add the value of the property you want to buy
     2- Add all the out of pocket expenses for buying the property
     3- Add the amount you want to rent the property for
     4- Add the expenses you will have monthly to mantain the property
     5- Check for the return of the investment (Please have the above 4 steps completed before)
     6- Exit 
     
""")
    try:
        global feedback
        feedback = input("Option: ")
        system("cls")
        return feedback

    except:
        print("Please enter a valid option")


def banner():
    print("""
********************************************************************************************
Check the return of your Investment here !!!   ---------------------------------------------
********************************************************************************************
""")


house = Property()


while True:
    banner()
    main()

    if feedback == "6":
        break
    if feedback == "1":
        system("cls")
        house.housevalue()
        system("cls")
    if feedback == "2":
        system("cls")
        house.outofpocketmethod()
        system("cls")
    if feedback == "3":
        system("cls")
        house.rentalmonth()
        system("cls")
    if feedback == "4":
        system("cls")
        house.monthlyexpenses()
        system("cls")
    if feedback == "5":
        system("cls")
        house.finalpage()
