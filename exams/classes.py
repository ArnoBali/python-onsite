'''
CLASSES AND OOP
===============

Define a python class that describes a book object.

Every instance of the class should have:
a title,
an author,
a total page number,
and a current page number (where the reader is at)
    that defaults to 0

Also, define a method that allows the user to read the book
for a certain number of pages
Calling the method should update the current page number
accordingly.

Inform the user if they've reached the end of the book! :)

Have fun, and no cheating ;)

'''

class Book:
    def __init__(self, title, author, total_pages, current_page=0):
        """Describes a book."""
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read(self, num_pages):
        """Increases the current page number by the number of pages read."""
        if self.current_page + num_pages > self.total_pages:
            return f"can't read that much! the book only has {self.total_pages} pages."
        elif self.current_page + num_pages == self.total_pages:
            self.current_page += num_pages
            return "yay! read all the way to the end!"
        else:
            self.current_page += num_pages


b1 = Book(title='Twilight', author='Meyer', total_pages=498)
b2 = Book(title='Breaking Dawn', author='Meyer', total_pages=756)
