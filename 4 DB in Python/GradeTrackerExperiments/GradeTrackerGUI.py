from tkinter import *
from math import sqrt as sqr


class Gradetracker(Frame):
    """
    A gradetracking app developed using the Tkinter GUI.
    """

    def __init__(self, master):
        """
        Initializes the frame.
        :param master: root.Tk()
        """
        Frame.__init__(self, master)
        self.entry = Entry(master, width=35, font=("Arial",25))
        self.entry.grid(row=0, column=0, columnspan=6, rowspan=3, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        #self.bind_buttons(master)
        self.grid()
        
    def add_chr(self, char, btn=None):
        """
        Concatenates a character passed from a button press (or key type) 
        to a string.
        :param char: string to add passed from a button
        :param btn: button name to use if key is pressed (to flash)
        :return: None
        """
        self.entry.configure(state="normal")
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")


    def login(self):
        global nameEL
        global pwordEL # More globals :D
        global loginWindow
    
        loginWindow = Tk() # This now makes a new window.
        loginWindow.title('Login') # This makes the window title 'login'
    
        intruction = Label(loginWindow, text='Please Login\n') # More labels to tell us what they do
        intruction.grid(sticky=E) # Blahdy Blah
    
        nameL = Label(loginWindow, text='Username: ') # More labels
        pwordL = Label(loginWindow, text='Password: ') # ^
        nameL.grid(row=1, sticky=W)
        pwordL.grid(row=2, sticky=W)
    
        nameEL = Entry(loginWindow) # The entry input
        pwordEL = Entry(loginWindow, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)
    
        loginB = Button(loginWindow, text='Login', command=self.checkLogin) # This makes the login button, which will go to the CheckLogin def.
        loginB.grid(columnspan=2, sticky=W)
    
        rmuser = Button(loginWindow, text='Delete User', fg='red', command=lambda: self.add_chr("delete user")) # This makes the deluser button. blah go to the deluser def.
        rmuser.grid(columnspan=2, sticky=W)
        loginWindow.mainloop()
    
    def checkLogin(self):      
        uname = "Dominic"
        pword = "Thomas"

        if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
            self.add_chr("Logged in!")
        else:
            self.add_chr("Login Failed")
        
    def clear_all(self):
        """
        Allows user to clear the full entry.
        :return: None
        """
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def create_widgets(self):
        """
        Creates the widgets to be used in the grid.
        :return: None
        """
        self.login_bttn = Button(self, text="Login", width=9, height=3, command=lambda: self.login())
        self.login_bttn.grid(row=3, column=0)

        self.add_grades_bttn = Button(self, text="Add Grades", width=9, height=3, command=lambda: self.add_chr("adding grades"))
        self.add_grades_bttn.grid(row=3, column=1)

        self.delete_bttn = Button(self, text="Delete", width=9, height=3, command=lambda: self.add_chr("deleting"))
        self.delete_bttn.grid(row=3, column=2)

        self.risk_bttn = Button(self, text="At Risk", width=9, height=3, command=lambda: self.add_chr("finding at risk"))
        self.risk_bttn.grid(row=3, column=4)

        self.average_bttn = Button(self, text="Avg", width=9, height=3, command=lambda: self.add_chr('averaging'))
        self.average_bttn.grid(row=3, column=5)

        self.clear_bttn = Button(self, text="Clear", width=9, height=3, command=lambda: self.clear_all())
        self.clear_bttn.grid(row=3, column=6)

root = Tk()
root.geometry()
root.title("GradeTracker")
app = Gradetracker(root)
root.mainloop()