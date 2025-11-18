class publisher:
    def __init__(self):
        pass
    def show(self):
        pass
class book(publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def show(self):
        print("Title:",self.title)
        print("Author:",self.author)
class python(book):
    def __init__(self,title,author,price,pages):
        super().__init__(title,author)
        self.price=price
        self.pages=pages
    def show(self):
        super().show()
        print("price:",self.price)
        print("number of pages:",self.pages)
title=input("Enter the title of the book:")
author=input("Enter the author of the book:")
price=float(input("Enter the price of the book:"))
pages=int(input("Enter the number of pages in the book:"))

python_book=python(title,author,price,pages)
python_book.show()
