# Program made by: Badi Mirzai.
# Date: 2017-02-16
import sys
from datetime import *
from datetime import timedelta

class Book:
    """book class, represents a book"""
    def __init__(self, title, author, status, personalID, time):
        """construction of a book"""
        self.title = title.lower()
        self.author = author.lower()
        self.status = status.lower()
        self.personalID = personalID
        self.time = time

    def __str__(self):
        """for writing out book in right format"""
        return str(self.title + ", " + self.author + ", " + self.status)

class Account:
    """Account class, represents a account"""
    def __init__(self, name, personalID, email, type):
        """Construction of a account"""
        self.name = name
        self.personalID = personalID
        self.email = email
        self.type = type

    def __str__(self):
        """for writing out the account in right format"""
        return str(self.name + "," + self.personalID + ", " + self.email)

class Library:
    """Represents the library. Takes list with books and the personal ID of the current user as argument.
    Functions does certain things in the account/book-list.
    Create account/book, delete account/book, borrowe/return book, login, save book/account,
     writes out diffrent lists of the book.
    Important to know that the time in the book is the deadline time that the user has to return,
     i.e 30 days after the book was borrowed."""

    def __init__(self, booklist, accountlist, personal_ID_user):
        """construction"""
        self.booklist = booklist
        self.accountlist = accountlist
        self.personal_ID_user=personal_ID_user

    def return_account_sting(self, account):
        return """ User name: {0}, Email: {1}""".format(account.name, account.email)

    def return_book_string(self, book):
        return """ Title: {0}, Author: {1}, Status: {2}""".format(book.title, book.author, book.status)

    def fine_counter(self, time):
        """counts the fine of an passed deadline. takes time (the deadline time in book) as argument."""
        days = int(((datetime.today())-time).days)
        weeks = int(days/7)
        final_fine = int(10 + 10*weeks)
        return final_fine

    # goes through alll the books/accounts in booklist/accountlist and formats the books time to a time format.
    # Checks if the dealine time in the book has passed and if so, calls the fine_counter function and
    # puts all the found late unreturned books book:found list, which is being retunred.
    def list_all_outgoing_books(self):
        """goes through alll the books/accounts in booklist/accountlist and formats the books time to a time format.
        Checks if the deadline time in the book has passed and if so, calls the fine_counter function and
        puts all the found late unreturned books book: found list, which is being retunred."""
        books_found=[]
        counter = 0
        for account in self.accountlist:
            for book in self.booklist:
                try:
                    time = datetime.strptime(book.time, "%Y-%m-%d")

                    if (account.personalID == book.personalID) and (book.status == 'borrowed') and ((time).toordinal()) < (datetime.today().toordinal()):
                        counter = counter + 1
                        fine = lib1.fine_counter(time)
                        books_found.append(lib1.return_book_string(book)+", "+lib1.return_account_sting(account)+", Fine:" + str(fine) + " SEK")
                except TypeError:
                    continue
                except ValueError:
                    continue
        if counter == 0:
            books_found.append("There are no outgoing books.")
        return books_found


    def add_new_book(self, in_title, in_author):
        """function to the menu. makes sure all inputs are lower case and checks if input is correctlly.
        checks if the book eitn title and author (as the inputs) exsists in the file, otherwise adds the book"""
        title = in_title.lower()
        author = in_author.lower()
        if title and not title.isspace() and author and not author.isspace():
            if any(charecters.isdigit() for  charecters in author)== True:
                return "Write letters as author"
            else:
                if (any(charecters.isalpha() for charecters in title) or any(characters.isdigit() for characters in title))== False or any(characters.isalpha() for characters in author)== False:
                    return "Fill in author AND title"
                else:
                    new_book = True
                    for book in self.booklist:
                        if book.title == title and book.author == author:
                            return "The book already exsists"
                    if new_book:
                        self.booklist.append(Book(title+"", author+"", "avalible", "nothing", "notimeset"))
                        return "The book is now added"
        else:
            return "Fill in title AND author"


    def help_to_sort_by_author(self):
        """Helps the function "writeOutAllBooksInLibrary" to sort all the book by author."""
        return self.author

    def write_out_all_books(self):
        """sorts all the books by author in self.booklist and then prints them out"""
        all_books_list = []
        #print('\nAll the books in the library [Author, Title (status)]: ')
        self.booklist.sort(key=Library.help_to_sort_by_author) # key sorting by the authors name
        for book in self.booklist:
            all_books_list.append("%s, %s (%s)" % (book.title, book.author, book.status))
        return all_books_list

    def my_borrowed_books(self):
        """checks all the book that has a personal ID matching the current users. Calls on the fine counter and puts all
            the found books in books_found list which is being returned."""
        books_found = []
        found = False
        for book in self.booklist:
            try:
                time_book = datetime.strptime(book.time, "%Y-%m-%d")
                fine = lib1.fine_counter(time_book)
                if (book.personalID == self.personal_ID_user) and (book.status == 'borrowed') and ((time_book).toordinal()) < (datetime.today().toordinal()):
                    found = True
                    books_found.append(lib1.return_book_string(book) + "[DATE HAS PASSED]. Fine:" + str(fine) + " SEK")
                elif (book.personalID == self.personal_ID_user) and (book.status == 'borrowed') and ((time_book).toordinal()) > (datetime.today().toordinal()):
                    found = True
                    books_found.append(lib1.return_book_string(book) + ", " + "Date passes: " + book.time )
            except TypeError:
                continue
            except ValueError:
                continue
        if found == False:
            books_found.append("You don't have any borrowed books.")
        return books_found


    def search_author(self, in_author):
        """Makes sure the input author is lowerspace and correctlly written. Goes through all the authors in booklist
        appends found matching book in list_of_authors list, which is bering returned. """
        author = in_author.lower()
        list_of_authors = []
        if author and not author.isspace():
            no_author=True
            for book in self.booklist:
                if book.author == author:
                    list_of_authors.append(Library.return_book_string(self, book))
                    no_author=False
            if no_author:
                list_of_authors.append("Author not found")
        else:
            list_of_authors.append("Write in Author")
        return list_of_authors

    def search_title(self, in_title):
        """Makes sure the input title (in_title) is lowerspace and correctlly written.
        Goes through all the authors in booklist, makes dure the right use
        appends found matching book in title_list, which is bering returned. """

        title = in_title.lower()
        title_list = []
        if title and not title.isspace():
            not_title = True
            for book in self.booklist:
                if book.title == title:
                    title_list.append(lib1.return_book_string(book))
                    not_title = False
            if not_title:
                title_list.append("Title not found")
        else:
            title_list.append("Fill in title")
        title_list = list(set(title_list))
        return title_list

    def borrow_book(self, in_title, in_author):
        """in_title and in_author parameters. checks matching book in self.booklist. borrowes by giving
        book.status= borrowed. isspace() checks if string empty. lower() makes lower case. returns string to user."""
        title=in_title.lower()
        author=in_author.lower()
        if title and not title.isspace() and author and not author.isspace():
            for book in self.booklist:
                if book.title == str(title) and book.author == str(author):
                            if book.status == "avalible":
                                book.status = "borrowed"
                                book.personalID = self.personal_ID_user
                                now = datetime.today() + timedelta(days=30)
                                time_in_book = now + timedelta(days=30)
                                book.time = time_in_book.strftime("%Y-%m-%d")
                                return("The book is now borrowed")
                            elif book.status == "borrowed" and book.personalID == self.personal_ID_user:
                                return("You have already borrowed the book")
                            else:
                                return("The book is already borrowed by another user.")
            else:
                return("The book does not exsist")
        else:
            return ("Fill in title AND author")

    def return_book(self, in_title, in_author):
        """in_title and in_author arguments. returns book by giving book.status= avalible.
        isspace() checks if string empty. lower() makes lower case. returns string to user.  """
        title = in_title.lower()
        author = in_author.lower()
        if title and not title.isspace() and author and not author.isspace():
            for book in self.booklist:
                if book.title == title and book.author == author:
                    if book.status == "borrowed" and book.personalID == str(self.personal_ID_user):
                        book.status = "avalible"
                        book.personalID = "nothing"
                        book.time = "notimeset"
                        return ("The book is now returned")
                    else:
                        return ("You must first borrow the book to return it")
            else:
                return ("The book does not exsist in the Library.")
        else:
            return ("Fill in title AND author")

    def remove_book(self, in_title, in_author):
        """in_title and in_author as parameters. checks each book if title and author match, and if status avalible.
         removes book from booklist. checks if the book is borrowed, which means not able to remove.
         isspace() checks if string empty. lower() makes lower case. returns string to user.  """
        title=in_title.lower()
        author=in_author.lower()
        if title and not title.isspace() and author and not author.isspace():
            for book in self.booklist:
              if book.title==title and book.author==author and book.status=="avalible":
                self.booklist.remove(book)
                return("The book is now deleted")
              elif book.title==title and book.author==author and book.status=="borrowed":
                  return("The book must be retured back, can therefor not be removed.")
            else:
              return("Book not found.")
        else:
            return "Fill in title AND author"

    def remove_account(self, in_personal_ID):
        """takes _in_personal_ID as input as the account that user wats to remove. Checks if it's corretlly filled in and
        and makes sure that you cannot remove the accountt you are logged in with. Also checks that the acccount
        being removed doesn't have any unreturned books"""
        digit_list= []
        for digit in in_personal_ID:
            digit_list.append(digit)
        if in_personal_ID and not in_personal_ID.isspace():
            if not(all(charecters.isdigit() for charecters in in_personal_ID))==True and len(digit_list)!=10:
                   return "Submit a 10 digit personalID!"
            elif str(self.personal_ID_user) == str(in_personal_ID):
                return "You cannot remove the account you are currentlly logged in with."
            else:
                not_borrowed=True
                for book in self.booklist:
                    if book.personalID==in_personal_ID:
                        return "Account can not be removed, they have borrowed books"
                if not_borrowed:
                    for account in self.accountlist:
                        if account.personalID == in_personal_ID:
                            self.accountlist.remove(account)
                            not_borrowed = False
                            return("Account now removed.")
                    if not_borrowed:
                        return "account could not be found"
        else:
            return ("fill in personal ID")


    def write_all_borrowed_accounts(self):
        """Checks all account and books in account/book list. if account personalID and book.personalID is the same
        and book.status borrowed, puts it in user and books list and then deletes all duplicates in users_that_has_borrowed.
        puts all accounts with books that they have borrowed in final_list_to_write, which is being returned."""
        users_that_has_borrowed = []
        books_borrowed = []
        final_list_to_write = []
        found = False
        for account in self.accountlist:
            for book in self.booklist:
                if book.status == 'borrowed' and account.personalID == book.personalID:
                    found = True
                    users_that_has_borrowed.append(account)
                    books_borrowed.append(book)
        # removes all dublicates in in list of accounts
        users_that_has_borrowed = list(set(users_that_has_borrowed))
        if found == False:
            return ("There are no users that has borrowed books.")
        else:
            for account in users_that_has_borrowed:
                final_list_to_write.append("\n%s has borrowed the following books (title, author):\n" %account)
                for book in books_borrowed:
                    if book.status == "borrowed":
                        timeInBook = datetime.strptime(book.time, "%Y-%m-%d")
                        if book.personalID == account.personalID and ((datetime.today()).toordinal()) >= (timeInBook.toordinal()):
                            final_list_to_write.append("%s, %s [DATE HAS PASSED]" % (book.title, book.author))
                        elif book.personalID == account.personalID:
                            final_list_to_write.append("%s, %s (date passes: %s)" %(book.title, book.author, book.time))
        return final_list_to_write

    def add_account(self, in_name, in_personal_ID, in_email, in_type):
        """Creates an account with name, personalID, email, och type as parameters.
        isspace() checks if string empty. lower() makes lower case. returns string to user. Returns awnser to user"""
        name= in_name.lower()
        personal_ID = in_personal_ID.lower()
        email = in_email.lower()
        type = in_type.lower()
        if name and not name.isspace() and personal_ID and not personal_ID.isspace() and email and not email.isspace() and type and not type.isspace():
            if any(charecters.isdigit() for charecters in name)==True:
                return "Submit the name in letters!"
            else:
                if not(all(charecters.isdigit for charecters in personal_ID))==True or len(personal_ID)!=10:
                    return "Submit your personal ID with 10 digits!"
                else:
                    new_account=True
                    for account in self.accountlist:
                        if account.personalID==personal_ID:
                            return "There already exsist an account with that personal ID"
                    if new_account:
                        if type=="normal" or type=="admin":
                            self.accountlist.append(Account(name, personal_ID, email, type))
                            return "The account is now successfully created!"
                        else:
                            return "Submit type as admin or normal"
        else:
            return "Fill in everything"


    def closeProgramFormat(self):
        """Formats all the books accounts in book/account-list into the files 'information.txt' and 'accounts.txt'.
        closes file when done."""
        with open('information.txt', 'w') as fileWithAllBooks:
            for book in self.booklist:
                fileWithAllBooks.write("%s; %s; %s; %s; %s\n" % (book.title, book.author, book.status, str(book.personalID), book.time))
            fileWithAllBooks.close()
        with open('accounts.txt', "w") as accountfile:
            for account in self.accountlist:
                accountfile.write("%s; %s; %s; %s\n" % (account.name, str(account.personalID), account.email, account.type))
            accountfile.close()

    def login_menu(self, personal_ID_user):
        """checks who is trying to login with personal_ID_user as parameter. also checks if the is bookfile
        or errors in files. if personal_ID_user exsists in account, chekcs what kind of user. returns type of user."""
        for book in self.booklist:
            if book == "No book file":
                return "you can not login the Library, there are no book file!"
            elif book == "IndexError":
                return "An error has occured (IndexError), ask an admin to look at the book file"
        for account in self.accountlist:
            if account == "No account file":
                return "you can not login the Library, there are no account file!"
            elif account == "IndexError":
                return "An error has occured (IndexError), ask an admin to look at the book file"
        if personal_ID_user and not personal_ID_user.isspace():
            if not (all(signs.isdigit() for signs in personal_ID_user)) == True or len(personal_ID_user) != 10:
                return "You must submit a 10 digit personal ID!"
            else:
                not_valid = True
                for account in self.accountlist:
                    if account.personalID == personal_ID_user:
                        type = account.type
                        self.personal_ID_user = personal_ID_user
                        not_valid = False
                        if type == "normal":
                            return type
                        elif type == "admin":
                            return type
                if not_valid:
                    return "Personal ID not valid, try again!"
        else:
            return "You must submit personal ID"


    def save_books(self):
        """opens file and writed in list with books in the file. sys.exit(0) turn off the program."""
        if self.booklist[0] == "IndexError":
            sys.exit(0)
        elif self.booklist[0] == "No book file":
            sys.exit(0)

        else:
            file=open("information.txt", 'w', encoding="UTF-8")
            for book in self.booklist:
                file.write(str(book))
            file.close()


    def save_accounts(self):
        """opens file and writed in list with accounts in the file. sys.exit(0) turn off the program. program closes
        if error or no file."""
        if self.accountlist[0] == "IndexError":
            sys.exit(0)
        elif self.accountlist[0] == "No account file":
            sys.exit(0)
        else:
            file = open("accounts.txt", "w", encoding="UTF-8")
            for account in self.accountlist:
                file.write(str(account))
            file.close()

def format_books():
    """function that takes the info from file 'information.txt' and transfers them to booklist.
    ckecks diffrent errors. returns formated list with books."""
    list_with_books = [] # list that all the book will be transfered to.
    try:
        readFileVariable=open('information.txt', 'r', encoding="UTF-8")
        for line in readFileVariable:
            try:
                makebook = line.strip('\n')
                parts = makebook.split('; ')
                # Every line in file is a book which is seperated into parts; title, author and status.
                if len(parts) == 5:
                    list_with_books.append(Book (parts[0], parts[1], parts [2], parts[3], parts[4]))
            except IndexError:
                del list_with_books[:]
                list_with_books.append("IndexError")
                break
        readFileVariable.close()
    except FileNotFoundError:
        """in case of the file does not exist/found"""
        list_with_books.append("No book file")
        #return ('You cannot login, the file book file was not found. Contact admin.')
    return list_with_books


def format_accounts():
    """function that takes the info from file 'accounts.txt' and transfers them to accountlist.
       ckecks diffrent errors. returns formated list with accounts."""
    list_with_accounts = []
    try:
        read_acconts = open ('accounts.txt', 'r', encoding="UTF-8")
        for line in read_acconts:
            try:
                makeAccount = line.strip('\n')
                parts = makeAccount.split('; ')
                if len(parts) == 4:
                    list_with_accounts.append(Account (parts[0], parts[1], parts[2], parts [3]))
            except IndexError:
                del list_with_accounts[:]
                list_with_accounts.append("IndexError")
                break
        read_acconts.close()
    except FileNotFoundError:
        list_with_accounts.append("No account file")
    return list_with_accounts

accountlist = format_accounts() # formats the accounts from file to accountlist
booklist = format_books() # format alll the book from file to booklist
lib1 = Library(booklist, accountlist, None) # lib1 is the library instance from the Library class.
# parameters, booklist, accountlist and None for personalID
