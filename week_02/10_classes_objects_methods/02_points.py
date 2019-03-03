'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({int(self.x)},{int(self.y)})"

class Rectangle:
    def __init__(self, width, height, corner_x, corner_y):
        self.width = width
        self.height = height
        self.corner_x = corner_x # corner is a Point object that specifies the lower-left corner
        self.corner_y = corner_y

    def find_center(self):
        p_x = self.corner_x + (self.width / 2)
        p_y = self.corner_y + (self.height / 2)
        p = Point(p_x, p_y)
        return p

    def grow_rectangle(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

r = Rectangle(10, 4, 1, 2)
print(r.find_center())

r.grow_rectangle(3, 5)
print(r.find_center())
