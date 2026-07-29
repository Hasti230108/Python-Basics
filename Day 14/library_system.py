class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class IssueBook(Book):
    def __init__(self, book_id, title, author, stud_id, issue_date):
        super().__init__(book_id, title, author)
        self.stud_id = stud_id
        self.issue_date = issue_date

    def display_IssueBook(self):
        self.display_book()
        print(f"Student ID: {self.stud_id}")
        print(f"Issue Book: {self.issue_date}")

b_id = int(input("Enter Book ID: "))
b_title = input("Enter Book Title: ")
b_author = input("Enter Book Author: ")
issue = input("Want to issue Book? (yes or no): ")
issue = issue.lower() 
if issue == "yes":
    Student_id = int(input("Enter Student id: "))
    IssueDate = input("Enter Issue Date: ")
    book = IssueBook(b_id, b_title, b_author, Student_id, IssueDate)
    print("\nIssuing Book:")
    book.display_IssueBook()
elif issue == "no":
    print("\nBook Details:")
    book = Book(b_id, b_title, b_author)
    book.display_book()
else:
    print("Wrong command entered.")