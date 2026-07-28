class Book:
    def __init__(self, book_id, book_name, author, price):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.price = price

    def display(self):
        print(f"\nBook Id: {self.book_id}")
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

        if self.price >= 1000:
            print("Book Category: Premium")
        elif self.price >= 500:
            print("Book Category: Standard")
        else:
            print("Book Category: Budget")

books = []

book1 = Book(101, "Python", "Guido", 1200)
books.append(book1)

book2 = Book(102, "DBMS", "Korth", 850)
books.append(book2)

book3 = Book(103, "C Programming", "Dennis", 450)
books.append(book3)

print("\nLibrary Book")

for book in books:
    book.display()