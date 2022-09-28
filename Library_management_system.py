import sys

# Creating a Library class
class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} available books are: ")
        for book in self.books: 
            print(" --- " + book)  # display all books available
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(f"{bookname} book is not availble either taken by someone else, wit until he returned.\n") # no book available print not available
        else:
            track.append({name: bookname})
            print("Thank you, book is issued please keep it with care and return on time.\n")
            self.books.remove(bookname) # if book available keep track of the book and remove the book from available books

    def returnBook(self, bookname):
        print("Thank you!, Book is returned\n")
        self.books.append(bookname) # append the book to available books

    def donateBook(self, bookname):
        print("Thank you for helping our library\n")
        self.books.append(bookname) # append the book donated to available books


# Create a student class
class Student():
    def requestBook(self):
        self.book = input("Enter name of the book you want to borrow: ") # take input of book required to be borrowed
        return self.book

    def returnBook(self):
        name = input("Enter your name: ") # name of person who is returning the book
        self.book = input("Enter name of the book you want to return: ") 
        if {name: self.book} in track:
            track.remove({name: self.book}) # remove book from track since its returned
        return self.book

    def donateBook(self):
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    collegeLibrary = Library(["Harry Potter", "And Then There Were None", "Alice's Adventures in Wonderland", "Pinocchio", "Catcher in the Rye", "Anne of Green Gables", "Twenty Thousand Leagues Under the Sea"]) # Creating an instance of class and entering books
    student = Student() # Creating an instance of student
    track = [] # Array to track the books borrowed from library

    print("\t\t\t\t\t\t------- WELCOME TO THE COLLEGE LIBRARY -------\n")
    print("""Choose an option:-\n1. Display all books\n2. Borrow a book\n3. Return book\n4. Donate book\n5. Track books\n6. Exit the library\n""")

    while (True):
        try:
            response = int(input("Enter your choice: ")) # Creating a field to enter the choice for an action to perform

            if response == 1:
                collegeLibrary.displayAvailableBooks() # display books
            elif response == 2:
                collegeLibrary.borrowBook(
                    input("Enter your name: "), student.requestBook()) # borrow book
            elif response == 3:
                collegeLibrary.returnBook(student.returnBook()) # returing book borrowed
            elif response == 4:
                collegeLibrary.donateBook(student.donateBook()) # donating a book to library
            elif response == 5:
                for i in track:
                    for key, value in i.items():
                        print(f"{value} book is taken by {key}.") # print the books borrowed and name
                print("\n")
                if len(track) == 0:
                    print("No books issued!. \n")

            elif response == 6:
                print("THANK YOU! \n")
                sys.exit() # end the program
            else:
                print("INVAILD INPUT!!! \n")  # if input is incorrect returning invalid input
        except Exception as e:
            print(f"{e} ---> INVALID INPUT!!! \n") # catch errors