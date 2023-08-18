from tkinter import *
import random, time

class Password_Gen(Frame):
    def __init__(self, master):
        super(Password_Gen, self).__init__(master)
        self.grid()
        self.genButton()


    def displayReplace(self, text):
        self.display1.delete(0, END)
        self.display1.insert(0, text)


    def passwordGen(self):
        x = self.slider.get()
        letter_set = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = "".join(random.sample(letter_set, x))
        self.displayReplace(password)


    def saveFunc(self, text):
        file = open("logins.txt", "a")
        file.write(self.display.get())
        file.write(" : ")
        file.write(self.display1.get())
        file.write("\n")
        file.close()
        self.display.delete(0, END)
        self.display1.delete(0, END)
        self.display2.delete(0, END)
        self.display2.insert(0, text)


    def genButton(self):
        self.label = Label(self, font = ("Calibri", 22), text = "Application:")
        self.label.grid(row = 1, column = 0, sticky = E)

        self.label = Label(self, font = ("Calibri", 22), text = "Password:")
        self.label.grid(row = 2, column = 0, sticky = E)

        self.label = Label(self, font = ("Calibri", 22), text = "Status:")
        self.label.grid(row = 3, column = 0, sticky = E)
        
        self.label = Label(self, font = ("Calibri", 22), text = "Length:")
        self.label.grid(row = 0, column = 0)
        
        self.button = Button(self, font = ("Calibri", 22), text = "Generate new password", fg = "red", relief = RAISED, command = lambda: self.passwordGen())
        self.button.grid(row = 4, column = 1, sticky = W)
        
        self.button1 = Button(self, font = ("Calibri", 22), text = "Save", fg = "red", relief = RAISED, command = lambda: self.saveFunc("Password Saved"))
        self.button1.grid(row = 4, column = 0)
        
        self.display = Entry(self, font = ("Calibri", 22), relief = RAISED)
        self.display.grid(row = 1, column = 1)

        self.display1 = Entry(self, font = ("Calibri", 22), relief = RAISED)
        self.display1.grid(row = 2, column = 1)

        self.display2 = Entry(self, font = ("Calibri", 22), relief = RAISED)
        self.display2.grid(row = 3, column = 1)

        self.slider = Scale(self, from_=0, to=14, tickinterval = 2, length = 300, orient = HORIZONTAL)
        self.slider.grid(row = 0, column = 1, sticky = W)
        
    
    
root = Tk()
root.title("Password Generator - JG")
root.geometry("460x255")
root.resizable(width = FALSE, height = FALSE)
app = Password_Gen(root)
root.mainloop()

##        self.display1 = Spinbox(self, font = ("Calibri", 22), relief = RAISED)
##        self.display1.grid(row = 2, column = 1)
