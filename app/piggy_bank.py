from utils.graphics import Text, Rectangle, Point, Entry


class PiggyBank:
    def __init__(self, win):
        self.win = win
        self.totalAmount = 0.0
        self.create_input_fields()

    def create_input_fields(self):
        """Initialize input fields for different coins."""
        self.setPennies()
        self.setNickels()
        self.setDimes()
        self.setQuarters()
        self.setDollars()

    def setPennies(self):
        self.pennies_entry = Entry(Point(150, 30), 15)
        self.pennies_entry.setFill("lightblue")
        self.pennies_entry.setText("0.00")  # Set default value
        self.pennies_entry.draw(self.win)
        Text(Point(35, 30), " Pennies  : ").draw(self.win)

    def setNickels(self):
        self.nickels_entry = Entry(Point(150, 60), 15)
        self.nickels_entry.setFill("lightblue")
        self.nickels_entry.setText("0.00")  # Set default value
        self.nickels_entry.draw(self.win)
        Text(Point(35, 60), " Nickels  : ").draw(self.win)

    def setDimes(self):
        self.dimes_entry = Entry(Point(150, 90), 15)
        self.dimes_entry.setFill("lightblue")
        self.dimes_entry.setText("0.00")  # Set default value
        self.dimes_entry.draw(self.win)
        Text(Point(35, 90), " Dimes    : ").draw(self.win)

    def setQuarters(self):
        self.quarters_entry = Entry(Point(150, 120), 15)
        self.quarters_entry.setFill("lightblue")
        self.quarters_entry.setText("0.00")  # Set default value
        self.quarters_entry.draw(self.win)
        Text(Point(35, 120), " Quarters  : ").draw(self.win)

    def setDollars(self):
        self.dollars_entry = Entry(Point(150, 150), 15)
        self.dollars_entry.setFill("lightblue")
        self.dollars_entry.setText("0.00")  # Set default value
        self.dollars_entry.draw(self.win)
        Text(Point(35, 150), " Dollars   : ").draw(self.win)

    def totalDeposit(self):
        """Calculate total deposit from all coin inputs."""
        try:
            # Retrieve and validate input values
            pennies = float(self.pennies_entry.getText())
            nickels = float(self.nickels_entry.getText())
            dimes = float(self.dimes_entry.getText())
            quarters = float(self.quarters_entry.getText())
            dollars = float(self.dollars_entry.getText())

            # Check if all inputs are 0.00
            if (pennies == 0.00 and nickels == 0.00 and dimes == 0.00 and
                    quarters == 0.00 and dollars == 0.00):
                self.totalAmount = 0.00
                return self.totalAmount

            # Calculate the total amount
            self.totalAmount = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25) + (
                    dollars * 1.00)

            return self.totalAmount
        except ValueError:
            raise Exception("Invalid input. Please enter valid numeric values for coins.")

    def loadingBackground(self):
        """Draw the loading background and piggy bank label."""
        rectangleBox = Rectangle(Point(5, 180), Point(395, 390))
        rectangleBox.setFill("red")
        rectangleBox.setOutline("yellow")
        rectangleBox.setWidth(10)
        rectangleBox.draw(self.win)
        piggyBankLabel = Text(Point(200, 270), "Piggy Bank")
        piggyBankLabel.setFill("white")
        piggyBankLabel.setSize(36)
        piggyBankLabel.draw(self.win)

    def displayOutputBox(self):
        """Display output box for messages."""
        outputBox = Rectangle(Point(5, 180), Point(395, 390))
        outputBox.setFill("lightblue")
        outputBox.setOutline("darkblue")
        outputBox.setWidth(4)
        outputBox.draw(self.win)

        self.output_text = Text(Point(200, 200), "Piggy Bank")
        self.output_text.setFill("black")
        self.output_text.draw(self.win)

    def helpMsg(self):
        """Display help message to the user."""
        self.output_text.setText("Help: Enter the amount of coins in each field.")

    def outputMsg(self):
        """Display the total amount message."""
        self.output_text.setText(f"Total Amount: ${self.totalAmount:.2f}")
