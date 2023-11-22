"""
Author: Jeremiah E. Ochepo
Last Edited: April/22/2021 (7PM)
Application: Piggy bank
Description: This application takes user input, processes the entered input, and tells if the user has enough money to buy a gift card. Finally, it tells the user what their remaining balance is.
"""

import math
from graphics import *
from button import Button

win = GraphWin("Piggy Bank", 400, 400)
win.setBackground("#fdcece")


# For better organization, this program will use class, method and functions to get the desired result.
class PiggyBank:

    # Constructor
    # Error_found is a list for storing any error found
    # If empty or length equal zero, then no error was found
    # Else if not empty or length greater than zero, then error was found

    def __init__(self, error_found=[]):
        self.error_found = error_found  # Stores error found

    # setPennies method draw the input box for user to enter penny value
    # It also set the default value to 0.00
    # Entry must be a number

    def setPennies(self, pennies_entry=0.0):
        self.pennies_entry = pennies_entry

        Text(Point(35, 30), " Pennies  : ").draw(win)
        self.pennies_entry = Entry(Point(150, 30), 15)
        self.pennies_entry.setFill("lightblue")
        self.pennies_entry.setText(pennies_entry)
        self.pennies_entry.draw(win)

    # getPennies function gets user input
    # Check to make sure user input is a valid number
    # Returns the value entered by user for processing

    def getPennies(self, penniesToDollars=0.0):
        self.penniesToDollars = penniesToDollars

        try:
            self.penniesToDollars = float(self.pennies_entry.getText())
            self.penniesToDollars = (self.penniesToDollars * 0.01)
            print("\nPennies to Dollars: " + str(self.penniesToDollars))

            if "Pennies_error" in self.error_found:
                self.error_found.remove("Pennies_error")
            else:
                pass

        except:

            if "Pennies_error" in self.error_found:
                self.error_found.remove("Pennies_error")
            else:
                self.error_found.append("Pennies_error")
                print(self.error_found)

    # setNickels method draw the input box for user to enter nickels value
    # It also set the default value to 0.00
    # Entry must be a number

    def setNickels(self, nickels_entry=0.0):
        self.nickels_entry = nickels_entry

        Text(Point(35, 60), " Nickels   : ").draw(win)
        self.nickels_entry = Entry(Point(150, 60), 15)
        self.nickels_entry.setFill("lightblue")
        self.nickels_entry.setText(nickels_entry)
        self.nickels_entry.draw(win)

    # getNickels function gets user input
    # Check to make sure user input is a valid number
    # Returns the value entered by user for processing

    def getNickels(self, nicklesToDollars=0.0):
        self.nicklesToDollars = nicklesToDollars

        try:
            self.nicklesToCents = float(self.nickels_entry.getText())
            self.nicklesToDollars = (self.nicklesToDollars * 0.05)
            print("Nickels to Dollars: " + str(self.nicklesToDollars))

            if "Nickles_error" in self.error_found:
                self.error_found.remove("Nickles_error")
            else:
                pass

        except:

            if "Nickles_error" in self.error_found:
                self.error_found.remove("Nickles_error")
            else:
                self.error_found.append("Nickles_error")
                print(self.error_found)

    # setDimes method draw the input box for user to enter dimes value
    # It also set the default value to 0.00
    # Entry must be a number

    def setDimes(self, dimes_entry=0.0):
        self.dimes_entry = dimes_entry

        Text(Point(35, 90), " Dimes    : ").draw(win)
        self.dimes_entry = Entry(Point(150, 90), 15)
        self.dimes_entry.setFill("lightblue")
        self.dimes_entry.setText(dimes_entry)
        self.dimes_entry.draw(win)

    # getDimes function gets user input
    # Check to make sure user input is a valid number
    # Returns the value entered by user for processing

    def getDimes(self, dimesToDollars=0.0):
        self.dimesToDollars = dimesToDollars

        try:
            self.dimesToDollars = float(self.dimes_entry.getText())
            self.dimesToDollars = (self.dimesToDollars * 0.01)
            print("Dimes to Dollars: " + str(self.dimesToDollars))

            if "Dimes_error" in self.error_found:
                self.error_found.remove("Dimes_error")
            else:
                pass

        except:

            if "Dimes_error" in self.error_found:
                self.error_found.remove("Dimes_error")
            else:
                self.error_found.append("Dimes_error")
                print(self.error_found)

    # setQuarters method draw the input box for user to enter quarter value
    # It also set the default value to 0.00
    # Entry must be a number

    def setQuarters(self, quarters_entry=0.0):
        self.quarters_entry = quarters_entry

        Text(Point(35, 120), " Quarters : ").draw(win)
        self.quarters_entry = Entry(Point(150, 120), 15)
        self.quarters_entry.setFill("lightblue")
        self.quarters_entry.setText(quarters_entry)
        self.quarters_entry.draw(win)

    # getQuarters function gets user input
    # Check to make sure user input is a valid number
    # Returns the value entered by user for processing

    def getQuarters(self, quartersToDollars=0.0):
        self.quartersToDollars = quartersToDollars

        try:
            self.quartersToDollars = float(self.quarters_entry.getText())
            self.quartersToDollars = (self.quartersToDollars * 25.00)

            self.quartersToDollars = self.quartersToDollars * 0.01

            print("Quarters to Dollars: " + str(self.quartersToDollars))

            if "Quarters_error" in self.error_found:
                self.error_found.remove("Quarters_error")
            else:
                pass

        except:

            if "Quarters_error" in self.error_found:
                self.error_found.remove("Quarters_error")
            else:
                self.error_found.append("Quarters_error")
                print(self.error_found)

    # setDollars method draw the input box for user to enter dollar value
    # It also set the default value to 0.00
    # Entry must be a number

    def setDollars(self, dollars_entry=0.0):
        self.dollars_entry = dollars_entry

        Text(Point(35, 150), " Dollars   : ").draw(win)
        self.dollars_entry = Entry(Point(150, 150), 15)
        self.dollars_entry.setFill("lightblue")
        self.dollars_entry.setText(dollars_entry)
        self.dollars_entry.draw(win)

    # getDollars function gets user input
    # Check to make sure user input is a valid number
    # Returns the value entered by user for processing

    def getDollars(self, dollarAmount=0.0):
        self.dollarAmount = dollarAmount

        try:
            self.dollarAmount = float(self.dollars_entry.getText())

            # Verify if entry is valid
            def isValidEntry():
                isValidDollars = self.dollarAmount
                return isValidDollars

            isValidEntry = isValidEntry()

            if int(isValidEntry) == 0 or int(isValidEntry) == 1 or int(isValidEntry) == 5 or int(
                    isValidEntry) == 20 or int(isValidEntry) == 100:
                self.dollarAmount = isValidEntry
                print("Dollars: " + str(self.dollarAmount))

                if "Dollars_error" in self.error_found:
                    self.error_found.remove("Dollars_error")
                else:
                    pass

            else:
                raise Exception("Value entered is not any of the following $0.0 or $1, or $5 or $20 or $100 dollars")

        except:

            if "Dollars_error" in self.error_found:
                self.error_found.remove("Dollars_error")
            else:
                self.error_found.append("Dollars_error")
                print(self.error_found)

    # totalDeposite method uses the accumulator functioin to add up all the valid valuse entered by user
    # If no error found, the total amount in dollars will be return for processing'
    # if error is found, a text will be displayes telling the user that an invalid entry was made.
    def totalDeposite(self, totalAmount=0.0):

        self.totalAmount = totalAmount

        try:
            if len(self.error_found) == 0:

                self.totalAmount += self.penniesToDollars
                self.totalAmount += self.nicklesToDollars
                self.totalAmount += self.dimesToDollars
                self.totalAmount += self.quartersToDollars
                self.totalAmount += self.dollarAmount
                self.totalAmount = round(self.totalAmount, 2)

                print("Account balance in dollars: " + str(self.totalAmount))
                print("Account balance in cents: " + str(self.totalAmount))

            else:
                raise Exception("Error found!")

        except:

            set(self.error_found)

        finally:

            if (len(self.error_found) == 0):
                return (self.totalAmount)

            else:
                print("\nError found in the following places: ")
                for index, error in enumerate(set(self.error_found)):
                    index += 1

                    print(str(index) + "." + str(error))

                errorMsg = "Invalid entry click help for instructions"
                return errorMsg

    # This Transaction method checks to see how many gift card the user can afford
    # ALso print out balance of the user in dollars and cent
    def Transaction(self, untPrice=50.0, qty=0, totalCost=0.0, balance=0, dollarsBalance=0, centsBalance=0):

        self.untPrice = untPrice
        self.qty = qty
        self.totalCost = totalCost
        self.balance = balance
        self.dollarsBalance = dollarsBalance
        self.centsBalance = centsBalance

        def trasactionCalculations():
            self.qty = int(self.totalAmount // self.untPrice)
            self.totalCost = self.qty * self.untPrice
            self.balance = round((self.totalAmount - (self.qty * self.untPrice)), 2)
            self.dollarsBalance = str(int(self.balance // 1))
            self.centsBalance = str(round((self.balance % 1), 2))

        def transactionSummary():
            print()
            print("qty: " + str(self.qty))
            print("Unit Price: " + str(self.untPrice))
            print("Total Cost: " + str(self.totalCost))
            print("Account Balance : " + str(self.balance))
            print("Account Balance Dollars: " + str(self.dollarsBalance))
            print("Account Balance Cents: " + str(self.centsBalance))
            print()

        try:
            if len(self.error_found) == 0:
                trasactionCalculations()
                transactionSummary()

            else:
                raise Exception("Error found!")

        except:

            set(self.error_found)

        finally:

            if (len(self.error_found) == 0):
                return (self.totalAmount)

            else:

                print("\nError found in the following places: ")
                for index, error in enumerate(set(self.error_found)):
                    index += 1

                    print(str(index) + "." + str(error))

                errorMsg = "Invalid entry click help for instructions"
                return errorMsg

    # Rectangle box for welcome background
    def loadingBackground(self):

        rectangleBox = Rectangle(Point(5, 180), Point(395, 390))
        rectangleBox.setFill("red")
        rectangleBox.setOutline("yellow")
        rectangleBox.setWidth(10)
        rectangleBox.draw(win)
        piggyBankLabel = Text(Point(200, 270), "Piggy Bank")
        piggyBankLabel.setFill("white")
        piggyBankLabel.setSize(36)
        piggyBankLabel.draw(win)

    # Rectangle box for displaying outcome
    def displayOutputBox(self):

        rectangleBox = Rectangle(Point(5, 180), Point(395, 390))
        rectangleBox.setFill("lightblue")
        rectangleBox.setOutline("darkblue")
        rectangleBox.setWidth(4)
        rectangleBox.draw(win)
        piggyBankLabel = Text(Point(200, 200), "Piggy Bank").draw(win)

    # This method print out user instructions
    def helpMsg(self):

        Text(Point(200, 230), "Coins : Numbers only").draw(win)
        Text(Point(200, 260), "Dolars: $1 or $5 or $20 or $100").draw(win)
        Text(Point(200, 290), "Enter : To check number of gift you can buy").draw(win)
        Text(Point(200, 320), "Clear : Delete items displayed on screen").draw(win)
        Text(Point(200, 350), "Quit  : To exit App").draw(win)

    # This method display message showing the number of gift card a user can affors
    def outputMsg(self):

        Text(Point(200, 230),
             "You are able to buy " + str(self.qty) + " " + " $" + str(self.untPrice) + " gift card from Wegmans").draw(
            win)
        Text(Point(200, 260),
             "Your balance is " + str(self.dollarsBalance) + " dollars and " + str(self.centsBalance) + " cents ").draw(
            win)


piggy_bank = PiggyBank()


# All these methods are used as setters
def setter_methods():
    piggy_bank.setPennies()
    piggy_bank.setNickels()
    piggy_bank.setDimes()
    piggy_bank.setQuarters()
    piggy_bank.setDollars()


setter_methods()


def accountBalance():
    piggy_bank.getPennies()
    piggy_bank.getNickels()
    piggy_bank.getDimes()
    piggy_bank.getQuarters()
    piggy_bank.getDollars()
    piggy_bank.totalDeposite()
    return piggy_bank.Transaction()


# Control Buttons
def helpButton():
    button = Button(win, Point(330, 35), 120, 25, "Help")
    button.activate()
    return button


def enterButton():
    button = Button(win, Point(330, 75), 120, 25, "Enter")
    button.activate()
    return button


def clearButton():
    button = Button(win, Point(330, 110), 120, 25, "Clear")
    button.activate()
    return button


def quitButton():
    button = Button(win, Point(330, 145), 120, 25, "Exit")
    button.activate()
    return button


def main(active_flag=True):
    piggy_bank.loadingBackground()
    getHelp = helpButton()
    enterNow = enterButton()
    clearNow = clearButton()
    quitApp = quitButton()

    pointClicked = win.getMouse()

    while active_flag:

        if getHelp.clicked(pointClicked):

            piggy_bank.displayOutputBox()
            piggy_bank.helpMsg()


        elif enterNow.clicked(pointClicked):

            try:
                if type(int(accountBalance())) == int:
                    piggy_bank.displayOutputBox()
                    piggy_bank.outputMsg()
                else:
                    raise Exception("Entry error")

            except:
                piggy_bank.displayOutputBox()
                piggy_bank.helpMsg()


        elif clearNow.clicked(pointClicked):
            piggy_bank.loadingBackground()


        elif quitApp.clicked(pointClicked):
            print("Quit")
            win.close()
            active_flag = False

        else:
            pass

        pointClicked = win.getMouse()


if __name__ == '__main__':
    try:
        main()
    except:
        pass
