# Program made by: Badi Mirzai.
# Date: 2017-02-16
import tkinter as tk
from library import *
from tkinter.tix import *

LARGE_FONT = ("Veranda", 16)

class Library_application(tk.Tk):
    """The class that the application is run through"""
    def __init__(self, *args, **kvargs) :
        tk.Tk.__init__(self, *args, **kvargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.screens={}

        for Frame in (Start_page, Menu_normal, Menu_admin, Borrow_site, Search_site, My_list_site, List_all_site, Book_site, Account_site, List_site, Register_site):
            screen = Frame(container, self)
            self.screens[Frame] = screen

            screen.grid(row=0, column=0, sticky="nsew")
            #nsew for "north", "south", "east" and "west".
        self.show_screen(Start_page)

    def show_screen(self, cont, site=None, selfside=None):
        """shows the screen through tk.raise. takes the site, selfsite and cont as parameters. site is the previous site that is being deleted
        and cont is where the user will get to."""
        screen = self.screens[cont]
        screen.tkraise()
        if site == None:
            pass
        else:
            site.delete_text(selfside)

class Start_page(tk.Frame):
    """Start page., where the user logs in. depending on personal_ID it shows menu
     through "choose_menu" function. class is run through tk.Frame"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="Welcome to the Library program.\n"
                                    "Login with your personal ID.\n "
                                    "(If this is your first time using this program,"
                                    " please register a new account below.)", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        personal_ID = tk.Label(self, text="Submit your personal ID (YYMMDDXXXX):")
        personal_ID.pack(pady=5, padx=10)

        self.in_personal_ID = tk.Entry(self)
        self.in_personal_ID.pack(pady=4, padx=10)

        login = tk.Button(self, text="Login", command=lambda: Start_page.choose_menu(lib1.login_menu(self.in_personal_ID.get()), controller, self))
        login.pack(pady=3, padx=10)

        register = tk.Button(self, text="Register new user", command = lambda: controller.show_screen(Register_site, Start_page, self))

        register.pack(pady=4, padx=10)

        self.answer = tk.Label(self, text=None)
        self.answer.pack()

        info = tk.Label(self, text="The following are the rules:"
                                       "\n- You have the right to sign up as a user and borrow books"
                                       "\n- When you borrow books you will have a 30 days deadline until the book has to be returned"
                                       "\n- If you don't return the book in time you will be giving a fine at 10 SEK/ week from the deadine"
                                       "\n- Only one user at a time can borrow the same book"
                                       "\n- If you don't behave, an admin user can delete you from the system"
                                       "\n- Only admin users can add & remove books/users", font=("normal", 13))
        info.pack()

    def choose_menu(menu, controller, self):
        """ Takes menu, controller as parameter. calls on the function show_screen"""
        if menu=="normal":
            controller.show_screen(Menu_normal, Start_page, self)
        elif menu=="admin":
            controller.show_screen(Menu_admin, Start_page, self)
        else:
            Borrow_site.write_labels(self, menu)

    def delete_text(self):
        self.in_personal_ID.delete(0, "end")
        self.answer.configure(text="")


class Register_site(tk.Frame):
    """site where user can register."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="Register user", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        name = tk.Label(self, text="Full name")
        name.pack(pady=10, padx=10)
        self.in_name=tk.Entry(self)
        self.in_name.pack(pady=9, padx=10)
        self.in_name.focus_set()

        personal_ID = tk.Label(self, text="Personal ID (YYMMDDXXXX): ")
        personal_ID.pack()
        self.in_personal_ID = tk.Entry(self)
        self.in_personal_ID.pack()
        self.in_personal_ID.focus_set()

        email = tk.Label(self, text="Email (example@email.com): ")
        email.pack()
        self.in_email = tk.Entry(self)
        self.in_email.pack()
        self.in_email.focus_set()

        type = tk.Label(self, text="Submit type (admin or normal): ")
        type.pack()
        self.in_type=tk.Entry(self)
        self.in_type.pack()
        self.in_type.focus_set()

        add_account=tk.Button(self, text="Add account", command=lambda: Account_site.write_labels(self, lib1.add_account(self.in_name.get(), self.in_personal_ID.get(), self.in_email.get(), self.in_type.get())))
        #write_labels function in Account_site class
        add_account.pack(pady=4, padx=10)

        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Start_page, Register_site, self))
        go_back.pack(pady=2, padx=10)

        self.answer = tk.Label(self, text=None)
        self.answer.pack()

    def write_labels(self, label):
        self.answer.configure(text=label)

    def delete_text(self):
        """Deletes the text in the different entryes."""
        self.in_name.delete(0, "end")
        self.in_personal_ID.delete(0,"end")
        self.in_email.delete(0,"end")
        self.in_type.delete(0, "end")
        self.answer.configure(text="")

class Menu_normal(tk.Frame):
    """Menu site for normal user, where there is diffrent buttons/choices. """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="Main menu", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        search = tk.Button(self, text="Search title/author", command= lambda: controller.show_screen(Search_site))
        search.pack(pady=4, padx=10)

        borrow = tk.Button(self, text="Borrow/Return book", command = lambda: controller.show_screen(Borrow_site))
        borrow.pack()

        list_my_borrowed = tk.Button(self, text="List my borrowed book", command= lambda: controller.show_screen(My_list_site))
        list_my_borrowed.pack()

        list_all_books = tk.Button(self, text="List all books", command = lambda: controller.show_screen(List_all_site))
        list_all_books.pack()

        logout = tk.Button(self, text='Logout', command = lambda: controller.show_screen(Start_page))
        logout.pack(pady=3, padx=10)

        help_for_user = tk.Label(self, text="Friedly advice!\nList all the books if this is your first time using this program!")
        help_for_user.pack(pady=2, padx=10)

class Menu_admin(tk.Frame):
    """A menu site for the admin user. choice through the buttons menu."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        handle_book = tk.Button(self, text="Add/Remove book", command= lambda: controller.show_screen(Book_site))
        handle_book.pack(pady=4, padx=10)

        handle_account = tk.Button(self, text="Add/Remove account", command = lambda: controller.show_screen(Account_site))
        handle_account.pack()

        list_outgoing_books = tk.Button(self, text = "List All/Borrowed/Outgoing books", command = lambda: controller.show_screen(List_site))
        list_outgoing_books.pack()

        logout = tk.Button(self, text="Logout", command = lambda: controller.show_screen(Start_page))
        logout.pack(pady=3, padx=10)


class Search_site(tk.Frame):
    """Site where user can search for author or title"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text = "Submit title:")
        title.pack(pady=10, padx=10)
        self.in_title = tk.Entry(self)
        self.in_title.pack(pady=9, padx=10)
        self.in_title.focus_set()

        author_submit = tk.Label(self, text="Submit Author:")
        author_submit.pack(pady=8, padx=10)
        self.author = tk.Entry(self)
        self.author.pack(pady=7, padx=10)
        self.author.focus_set()


        search_title = tk.Button(self, text="Search title", command = lambda: List_all_site.write_text(self, lib1.search_title(self.in_title.get())))
        search_title.pack(pady=4, padx=10)

        search_author = tk.Button(self, text="Search author", command=lambda: List_all_site.write_text(self, lib1.search_author(self.author.get())))
        search_author.pack(pady=3, padx=10)

        go_back = tk.Button(self, text='Go back', command= lambda: controller.show_screen(Menu_normal, Search_site, self))
        go_back.pack(pady=2, padx=10)

        self.listbox=tk.Listbox(self, width=100)
        self.listbox.pack(side="left", fill="y")

        self.scrollbar=tk.Scrollbar(self, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listbox.yview)

    def delete_text(self):
        """deletes the entry text when user goes to diffrent screen"""
        self.in_title.delete(0, "end")
        self.author.delete(0, "end")
        self.listbox.delete(0, "end")

class Borrow_site(tk.Frame):
    """Page where you can borrow or return book. write_labels gives answer with respect to users input.
        delete_text deletes the users input when screen changes."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        title=tk.Label(self, text="Borrow/Return book", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        title = tk.Label(self, text="Submit title: ")
        title.pack(pady=10, padx=10)
        self.in_title=tk.Entry(self)
        self.in_title.pack(pady=9, padx=10)
        self.in_title.focus_set()

        author = tk.Label(self, text="Submit author:")
        author.pack(pady=7, padx=10)
        self.in_author = tk.Entry(self)
        self.in_author = tk.Entry(self)
        self.in_author.pack(pady=6, padx=10)
        self.in_author.focus_set()

        borrow = tk.Button(self, text="Borrow", command = lambda: Borrow_site.write_labels(self, lib1.borrow_book((self.in_title).get(), (self.in_author).get())))
        borrow.pack(pady=4, padx=10)

        return_book = tk.Button(self, text="Return book", command=lambda: Borrow_site.write_labels(self, lib1.return_book((self.in_title).get(), (self.in_author).get())))
        return_book.pack(pady=3, padx=10)

        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Menu_normal, Borrow_site, self))
        go_back.pack(pady=2, padx=10)

        self.answer=tk.Label(self, text=None)
        self.answer.pack()

    def write_labels(self, label):
        """Takes label as input and updates self.awnser text to label."""
        self.answer.configure(text=label)

    def delete_text(self):
        """Delets entry text for in_title, in_author and the label for self.awnser."""
        self.in_title.delete(0, "end")
        self.in_author.delete(0, "end")
        self.answer.configure(text="")
        self.answer.configure(text="")

class My_list_site(tk.Frame):
    """Site that writes out the users borrowed books"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="My borrowed books", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        search = tk.Button(self, text="List my books", command=lambda: List_all_site.write_text(self, lib1.my_borrowed_books()))
        search.pack(pady=4, padx=10)

        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Menu_normal, List_all_site, self))
        go_back.pack(pady=3, padx=10)

        self.listbox = tk.Listbox(self, width=100)
        self.listbox.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

class List_all_site(tk.Frame):
    """Page where all books are printed for the user."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="List all books", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        print_all_books = tk.Button(self, text="List all books", command=lambda: List_all_site.write_text(self, lib1.write_out_all_books()))
        print_all_books.pack(pady=4, padx=10)

        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Menu_normal, List_all_site, self))
        go_back.pack(pady=3, padx=10)

        self.listbox = tk.Listbox(self, width=100)
        self.listbox.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    #takes a list as input and writes it out in a listbox
    def write_text(self, list):
        """takes a list as input and writes it out in a listbox"""
        self.listbox.delete(0, "end")
        for element in list:
            self.listbox.insert(END, element)

    def delete_text(self):
        """deletes the list in the listbox"""
        self.listbox.delete(0, "end")


    # page where user can delete/create book
class Book_site(tk.Frame):
    """Page where (admin) user can delete/create book"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_for_book = tk.Label(self, text="Add/Remove book", font=LARGE_FONT)
        title_for_book.pack(pady=10, padx=10)

        title_text = tk.Label(self, text="Submit title: ")
        title_text.pack(pady=10, padx=10)
        self.in_title = tk.Entry(self)
        self.in_title.pack(pady=9, padx=10)
        self.in_title.focus_set()

        author = tk.Label(self, text="Submit author: ")
        author.pack(pady=7, padx=10)
        self.in_author = tk.Entry(self)
        self.in_author.pack(pady=6, padx=10)
        self.in_author.focus_set()

        add_book = tk.Button(self, text="Add book", command=lambda: Borrow_site.write_labels(self, lib1.add_new_book(self.in_title.get(), self.in_author.get())))
        add_book.pack(pady=4, padx=10)

        remove_book = tk.Button(self, text="Detele book", command=lambda: Borrow_site.write_labels(self, lib1.remove_book(self.in_title.get(), self.in_author.get())))
        remove_book.pack(pady=3, padx=10)

        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Menu_admin, Borrow_site, self))

        go_back.pack(pady=2, padx=10)

        self.answer = tk.Label(self, text=None)
        self.answer.pack()


class Account_site(tk.Frame):
    """ Page where (admin) user can remove/create account"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="Add/Remove account", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        name = tk.Label(self, text="Submit name: ")
        name.pack(pady=10, padx=10)
        self.in_name = tk.Entry(self)
        self.in_name.pack(pady=9, padx=10)
        self.in_name.focus_set()

        personal_ID = tk.Label(self, text="Submit personal ID (YYMMDDXXXX):")
        personal_ID.pack()
        self.in_personal_ID = tk.Entry(self)
        self.in_personal_ID.pack()
        self.in_personal_ID.focus_set()

        email = tk.Label(self, text="Submit email: ")
        email.pack()
        self.in_email = tk.Entry(self)
        self.in_email.pack()
        self.in_email.focus_set()

        type = tk.Label(self, text='Submit type ("normal" or "admin"):')
        type.pack()
        self.in_type = tk.Entry(self)
        self.in_type.pack()
        self.in_type.focus_set()

        add_account = tk.Button(self, text="Add account", command=lambda: Account_site.write_labels(self, lib1.add_account(self.in_name.get(), self.in_personal_ID.get(), self.in_email.get(), self.in_type.get())))
        add_account.pack(pady=4, padx=10)

        remove_account = tk.Button(self, text="Remove account", command=lambda: Account_site.write_labels(self, lib1.remove_account(self.in_personal_ID.get())))
        remove_account.pack(pady=3, padx=10)

        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Menu_admin, Account_site, self))
        go_back.pack(pady=2, padx=10)

        self.answer = tk.Label(self, text=None)
        self.answer.pack()

        help_to_user = tk.Label(self, text="Friendly advice\nTo delete an account you only need to fill in the personal ID!")
        help_to_user.pack()

    def write_labels(self, label):
        """Takes label as parameter and updates self.awnser to label"""
        self.answer.configure(text=label)

    def delete_text(self):
        """Deletes the text from the Entry to names, personalID and types, when user goes to diffrent screen"""
        self.in_name.delete(0, "end")
        self.in_personal_ID.delete(0, "end")
        self.in_email.delete(0, "end")
        self.in_type.delete(0, "end")
        self.answer.configure(text="")


class List_site(tk.Frame):
    """site where user can list all the book, borrowed books och utgoing books"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="List books", font=LARGE_FONT)
        title.pack(pady=10, padx=10)

        list_all_books = tk.Button(self, text="List all books", command=lambda: List_all_site.write_text(self, lib1.write_out_all_books()))
        list_all_books.pack(pady=4, padx=10)

        list_all_borrowed = tk.Button(self, text="List all users that has borrowed books", command=lambda: List_all_site.write_text(self, lib1.write_all_borrowed_accounts()))
        list_all_borrowed.pack(pady=3, padx=10)

        list_all_outgoing_books = tk.Button(self, text="List all outgoing books", command=lambda: List_all_site.write_text(self, lib1.list_all_outgoing_books()))
        list_all_outgoing_books.pack(pady=5,padx=10)


        go_back = tk.Button(self, text="Go back", command=lambda: controller.show_screen(Menu_admin, List_all_site, self))
        go_back.pack(pady=6, padx=10)

        self.listbox = tk.Listbox(self, width=100)
        self.listbox.pack(side="left", fill="y")
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

app = Library_application() # creates a library istance from the Library_application() class.
accountlist = format_accounts() # format the accounts from the accountfile to the accountlist.
booklist = format_books() #formats the books from the files to the booklist.
lib1 = Library(booklist, accountlist, None) # lib1 is the library instance from the Library class.
app.mainloop() # runs the mainloop for the Library_application class that handles all the screenes.
Library.closeProgramFormat(lib1) # saves all the objects from the instance lib1 to the files. uses Librarys own function closeProgramFormat that does this.