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
    # Print a Point object in human-readable format.
        return f"({self.x},{self.y})"

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner # corner is a Point object that specifies the lower-left corner


    def find_center(self):
        p = Point()
        p.x = (self.corner.x + self.width) / 2
        p.y = (self.corner.y + self.height) / 2
        return p

    def grow_rectangle(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

p = Point(1,0)
print(p)


#  def main():
#     blank = Point(3 ,4)
#
#     print(blank.print_point)
#
#     box = Rectangle(100, 200, Point(0, 0))
#
#     print(box.find_center)
#
#     print(box.width)
#     print(box.height)
#     print('grow')
#     box.grow_rectangle(50, 100)
#     print(box.width)
#     print(box.height)
#
#
# if __name__ == '__main__':
#     main()