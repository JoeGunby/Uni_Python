from tkinter import *
import csv

class Login(Frame):
    def __init__(self, master):
        super(Login, self).__init__(master)
        self.grid()
        self.loginBoxes()
        self.nameTags()

#   Name tags for the entry forms.
    def nameTags(self):
        self.loginLabel = Label(self, text = "Username:", font = ("Calibri", 16), fg = "red")
        self.loginLabel.grid(row = 0, column = 0, sticky = W)

        self.passwordLabel = Label(self, text = "Password:", font = ("Calibri", 16), fg = "red")
        self.passwordLabel.grid(row = 1, column = 0, sticky = W)

        self.statusLabel = Label(self, text = "Status:", font = ("Calibri", 16), fg = "red")
        self.statusLabel.grid(row = 3, column = 0, sticky = W)

#   Input buttons and entry areas and hashed password.  
    def loginBoxes(self):
        self.loginBox = Entry(self, font = ("Calibri", 16), relief = RAISED, bd = 1)
        self.loginBox.insert(0, "")
        self.loginBox.grid(row = 0, column = 1, columnspan = 10)

        self.passwordBox = Entry(self, show = "*", font = ("Calibri", 16), relief = RAISED, bd = 1)
        self.passwordBox.insert(0, "")
        self.passwordBox.grid(row = 1, column = 1, columnspan = 10)

        self.button1 = Button(self, text = "Create new\nlogin", height = 2, width = 10, font = ("Calibri", 12))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = Button(self, text = "Login", height = 2, width = 10, font = ("Calibri", 12), command = lambda: self.loginCheck())
        self.button2.grid(row = 2, column = 1, sticky = W)

        self.status = Entry(self, font = ("Calibri", 16), relief = RAISED, bd = 1)
        self.status.grid(row = 3, column = 1, sticky = W)

#   Problem area, even if I pass a correct username into the entry box the return
#   is still negative, I put an else clause to try to catch any funky business going on.
#   for now the output is just in the console, easier to type and less to go wrong.
    def loginCheck(self):
        with open("passwords.csv") as csvfile:
            checkUser = csv.reader(csvfile, delimiter = ",")
            userNames = []
            passWords = []
            for row in checkUser:
                userName = row[0]
                passWord = row[1]
                userNames.append(userName)
                passWords.append(passWord)
            print(userNames, passWords)
            if self.loginBox in userNames:
                print("USER, WEHEY!")
                # This will continue to do much the same check for the password
            elif self.loginBox not in userNames:
                print("NO USER")
            else:
                print("NOPE")


root = Tk()
root.title("Login Window")
root.geometry("325x175")
root.resizable(width = FALSE, height = FALSE)
app = Login(root)
root.mainloop()


# This is just code for copy/pasting later to speed things up

##                    self.userFound = Label(self, text = "User found", font = ("Calibri", 16), fg = "red")
##                    self.userFound.grid(row = 4, column = 1, sticky = W)

##                    self.noUser = Label(self, text = "No such user", font = ("Calibri", 16), fg = "red")
##                    self.noUser.grid(row = 4, column = 1, sticky = W)
