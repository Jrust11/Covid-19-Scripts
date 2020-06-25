from tkinter import Tk, ttk, Frame, Button, Label, Entry, Text, Checkbutton, \
    Scale, Listbox, Menu, BOTH, RIGHT, RAISED, N, E, S, W, \
    HORIZONTAL, END, FALSE, INSERT, IntVar, StringVar, messagebox as box
from tkinter import *


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Simple Window")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.centreWindow()
        self.pack(fill=BOTH, expand=1)


        firstNameLabel = Label(self, text="First Name")
        firstNameLabel.grid(row=0, column=0, sticky=W+E)
        lastNameLabel = Label(self, text="Last Name")
        lastNameLabel.grid(row=1, column=0, sticky=W+E)
        countryLabel = Label(self, text="Country")
        countryLabel.grid(row=2, column=0, sticky=W+E)

        firstNameText = Entry(self, width=20)
        firstNameText.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        lastNameText = Entry(self, width=20)
        lastNameText.grid(row=1, column=1, padx=5, pady=5, ipady=2, sticky=W+E)



        addressText = Text(self, padx=5, pady=5, width=20, height=6)
        addressText.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        closeBtn = Button(self, text="Close", width=10, command=self.onExit)
        closeBtn.grid(row=5, column=1, padx=5, pady=3, sticky=W+E)

    def centreWindow(self):
        w = 300
        h = 300
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onExit(self):
        self.quit()





def main():
    root = Tk()
    #root.geometry("250x150+300+300")    # width x height + x + y
    # we will use centreWindow instead
    root.resizable(width=FALSE, height=FALSE)
    # .. not resizable
    

    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
