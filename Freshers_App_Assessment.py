from tkinter import *


class ChesterApplication(Frame):
    def __init__(self, master):
        super(ChesterApplication, self).__init__(master)
        self.grid()
        self.nameTags()
        self.homePage()

    def nameTags(self):
        self.banner = Label(self, font = ("Helvetica", 18), fg = "firebrick3", text = "Chester Information Application")
        self.banner.grid(column = 0, row = 0, columnspan = 5, padx = 5, sticky = N)

        self.button1 = Button(self, font = ("Helvetica", 14), fg = "firebrick3", text = "Home", relief = RAISED, command = lambda: self.homePage())
        self.button1.grid(column = 0, row = 1, ipady = 12, pady = 5, sticky = N)

        self.button2 = Button(self, font = ("Helvetica", 14), fg = "firebrick3", text = "Helpful\nLinks", relief = RAISED, command = lambda: self.linkPage())
        self.button2.grid(column = 1, row = 1, pady = 5, sticky = N)

        self.button3 = Button(self, font = ("Helvetica", 14), fg = "firebrick3", text = "Dining\nOptions", relief = RAISED, command = lambda: self.diningPage())
        self.button3.grid(column = 2, row = 1, pady = 5, sticky = N)

        self.button4 = Button(self, font = ("Helvetica", 14), fg = "firebrick3", text = "Transport\nOptions", relief = RAISED, command = lambda: self.transportPage())
        self.button4.grid(column = 4, row = 1, pady = 5, sticky = N)

        self.content_box = Text(self, font = ("Helvetica", 12), fg = "firebrick3", height = 10, width = 40, wrap = WORD)
        self.content_box.grid(column = 0, row = 2, columnspan = 5, sticky = N)

    def displayReplace(self, text):
        self.content_box.delete(0.0, END)
        self.content_box.insert(0.0, text)

    def homePage(self):
        text = """This is the University of Chester freshers app, it is designed to help you orient yourselves in your first few weeks at the university.\n\nClick one of the buttons above for information in that area"""
        self.displayReplace(text)

    def linkPage(self):
        text = """Website: https://www1.chester.ac.uk\nPortal: https://portal1.chester.ac.uk\neVision: https://sipr-evision.chester.ac.uk\n"""
        self.displayReplace(text)

    def diningPage(self):
        text = """There are various places to eat on the Parkgate Campus, they include: \n\nWhites Dining Halls, The Garden Dining Rooms, Crusty Corner, Senate House, Grab & Go and various other outlets such as Starbucks and Costa."""
        self.displayReplace(text)

    def transportPage(self):
        text = """There is a bus shuttle service to provide transport to and from the Thornton Science Park at 08:15, 09:30, 10:30, 12:30 & 13:30 .\n\nThere is also a shuttle to and from the Warrington Campus leaving Chester at 08:45, 13:00 & 16:00"""
        self.displayReplace(text)

root = Tk()
root.title("Chester App")
root.geometry("365x300")
root.resizable(width = FALSE, height = FALSE)
app = ChesterApplication(root)
root.mainloop()
