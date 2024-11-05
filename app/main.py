from utils.graphics import GraphWin
from piggy_bank import PiggyBank
from gui import create_buttons


def main():
    win = GraphWin("Piggy Bank", 400, 400)
    win.setBackground("#fdcece")

    piggy_bank = PiggyBank(win)
    piggy_bank.loadingBackground()

    # Create buttons
    buttons = create_buttons(win)

    # Main interaction loop
    active_flag = True

    while active_flag:

        if win.isClosed():
            break  # Exit loop if window is closed

        pointClicked = win.getMouse()

        if buttons["help"].clicked(pointClicked):
            piggy_bank.displayOutputBox()
            piggy_bank.helpMsg()

        elif buttons["enter"].clicked(pointClicked):
            try:
                piggy_bank.totalDeposit()
                piggy_bank.displayOutputBox()
                piggy_bank.outputMsg()
            except Exception as e:
                piggy_bank.displayOutputBox()
                piggy_bank.helpMsg()

        elif buttons["clear"].clicked(pointClicked):
            # Close the current window
            win.close()
            # Restart the application
            main()  # Call main() to restart the application

        elif buttons["quit"].clicked(pointClicked):
            print("Quit")
            win.close()
            active_flag = False


if __name__ == '__main__':
    main()
