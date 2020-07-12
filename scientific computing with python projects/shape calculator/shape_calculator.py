class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        string = "Rectangle(width={}, height={})".format(self.width, self.height)
        return string

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            too_big = "Too big for picture."
            return too_big
        else:
            for i in range(self.height):
                line = "*" * self.width
                picture = picture + line + "\n"
        return picture

    def get_amount_inside(self, shape):
        vertical = self.width // shape.width
        horizontal = self.height // shape.height
        amount = vertical * horizontal
        return amount


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.height = side
        self.width = side

    def __str__(self):
        string = "Square(side={})".format(self.width, self.height)
        return string

    def set_side(self, side):
        self.height = side
        self.width = side
