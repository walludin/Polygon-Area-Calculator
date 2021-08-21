
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Set function (width)
    def set_width(self, width):
        self.width = width

    # Set function (height)
    def set_height(self, height):
        self.height = height

    # Get Area of the shape
    def get_area(self):
        return self.width * self.height

    # Get Perimeter of the shape
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    # Get Diagonal
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)

    # Get (*) picture
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            return ((("*" * self.width) + "\n") * self.height)

    # Get No of shape(Sqaure| Rectangle) can occupy in the given Shape
    def get_amount_inside(self, obj):
        return (self.width // obj.width) * (self.height // obj.height)

class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    # Set Function (side)
    def set_side(self, side):
        self.height = side
        self.width = side

    # Set function (width)
    def set_width(self, side):
        self.width = side

    # Set function (height)

    def set_height(self, side):
        self.height = side

    # String representation of Object
    def __str__(self):
        return f"Square(side={self.width})"
