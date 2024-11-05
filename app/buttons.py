from utils.graphics import Point, Rectangle, Text

class Button:
    def __init__(self, win, center, width, height, label):
        """Create a button with the given parameters."""
        self.width = width
        self.height = height

        # Create the graphical representation of the button
        self.xmin = center.getX() - width / 2
        self.xmax = center.getX() + width / 2
        self.ymin = center.getY() - height / 2
        self.ymax = center.getY() + height / 2
        self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
        self.rect.setFill("lightgrey")
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)

        self.active = True  # Button is active by default

    def activate(self):
        """Set this button to 'active'."""
        self.active = True
        self.rect.setFill("lightgrey")

    def deactivate(self):
        """Set this button to 'inactive'."""
        self.active = False
        self.rect.setFill("darkgrey")

    def clicked(self, point):
        """Return True if button is clicked, False otherwise."""
        if self.active:
            return (self.xmin < point.getX() < self.xmax) and (self.ymin < point.getY() < self.ymax)
        return False
