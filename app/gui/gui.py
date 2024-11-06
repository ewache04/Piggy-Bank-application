from utils.graphics import Point
from buttons import Button


def create_buttons(win):
    """Creates buttons for the application."""
    buttons = {
        "help": Button(win, Point(330, 35), 120, 25, "Help"),
        "enter": Button(win, Point(330, 75), 120, 25, "Enter"),
        "clear": Button(win, Point(330, 110), 120, 25, "Clear"),
        "quit": Button(win, Point(330, 145), 120, 25, "Exit"),
    }
    for button in buttons.values():
        button.activate()
    return buttons
