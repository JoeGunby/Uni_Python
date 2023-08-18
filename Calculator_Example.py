from tkinter import *

class Calculator(Frame):
    def __init__(self, master):
        super(Calculator, self).__init__(master)
        self.grid()
        self.createWidgets()
        
##        self.file = Menu(self, tearoff = 0)
##        self.add_command(label = "Quit", command = quit())
##        self.file.add_cascade(label = "File", menu = filemenu)

    def clear(self):
        self.displayReplace("0")

    def calculation(self):
        self.expression = self.display.get()
##        self.expression = self.expression.replace("%", "/100")
        try:
            self.result = eval(self.expression)
            self.displayReplace(self.result)
        except:
            messagebox = messagebox.showinfo("Error")
            messagebox()
        
    def displayReplace(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def displayAppend(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)
        if self.entryText == "0":
            self.displayReplace(text)
        else:
            self.display.insert(self.textLength, text)
        
    def createWidgets(self):
        self.display = Entry(self, font = ("TimesNewRoman", 20), relief = RAISED, justify = RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row = 0, column = 0, columnspan = 5)
        
        self.button1 = Button(self, text = "7", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("7"))
        self.button1.value = 7
        self.button1.grid(row = 1, column = 0, sticky = W)
        
        self.button2 = Button(self, text = "8", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("8"))
        self.button2.value = 8
        self.button2.grid(row = 1, column = 1, sticky = W)
        
        self.button3 = Button(self, text = "9", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("9"))
        self.button3.value = 9
        self.button3.grid(row = 1, column = 2, sticky = W)
        
        self.button4 = Button(self, text = "4", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("4"))
        self.button4.value = 4
        self.button4.grid(row = 2, column = 0, sticky = W)
        
        self.button5 = Button(self, text = "5", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("5"))
        self.button5.value = 5
        self.button5.grid(row = 2, column = 1, sticky = W)
        
        self.button6 = Button(self, text = "6", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("6"))
        self.button6.value = 6
        self.button6.grid(row = 2, column = 2, sticky = W)
        
        self.button7 = Button(self, text = "1", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("1"))
        self.button7.value = 1
        self.button7.grid(row = 3, column = 0, sticky = W)

        self.button8 = Button(self, text = "2", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("2"))
        self.button8.value = 2
        self.button8.grid(row = 3, column = 1, sticky = W)

        self.button9 = Button(self, text = "3", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("3"))
        self.button9.value = 3
        self.button9.grid(row = 3, column = 2, sticky = W)

        self.button0 = Button(self, text = "0", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("0"))
        self.button0.value = 0
        self.button0.grid(row = 4, column = 1, sticky = W)

        self.buttonDot = Button(self, text = ".", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("."))
        self.buttonDot.grid(row = 4, column = 2, sticky = W)

        self.buttonAdd = Button(self, text = "+", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("+"))
        self.buttonAdd.grid(row = 1, column = 3, sticky = W)

        self.buttonMinus = Button(self, text = "-", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("-"))
        self.buttonMinus.grid(row = 2, column = 3, sticky = W)

        self.buttonTimes = Button(self, text = "*", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("*"))
        self.buttonTimes.grid(row = 3, column = 3, sticky = W)

        self.buttonDivide = Button(self, text = "/", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.displayAppend("/"))
        self.buttonDivide.grid(row = 4, column = 3, sticky = W)

        self.buttonEquals = Button(self, text = "=", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.calculation())
        self.buttonEquals.grid(row = 4, column = 0, sticky = W)

        self.buttonClear = Button(self, text = "C", font = ("Calibri", 12), height = 3, width = 6, borderwidth = 1, bg = "cyan", command = lambda: self.clear())
        self.buttonClear.grid(row = 1, column = 4, sticky = W)






root = Tk()
root.title("Calculator - JG")
root.geometry("301x325")
root.resizable(width = FALSE, height = FALSE)
app = Calculator(root)
root.mainloop()
