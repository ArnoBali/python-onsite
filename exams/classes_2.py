'''
Assume the Book class we built before.

* What do we get when running the following code snippets?

'''


# our Book class from before
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


# let's instantiate some popular book objects...
b1 = Book(title='Twilight', author='Meyer', total_pages=498)
b2 = Book(title='Breaking Dawn', author='Meyer', total_pages=756)

# 1) what does it print?
print(b1)

# 2) what does it print?
print(b1.title)

# 3) what does it print?
b1.fame = 'very!'
print(b1.fame)
print(b2.fame)

# 4) what does it print?
b2.read(10)
print(b2.current_page)
print(b1.current_page)