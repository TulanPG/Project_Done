from tkinter import *
from tkinter import ttk
import tkinter.messagebox


#TO DO if you want more...

class atm:

    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(110* blank_space + "ATM BANK by Tulan")
        self.root.geometry("800x760+280+0")
        self.root.configure(background ='gainsboro')

        MainFrame = Frame(self.root, bd=20, width = 784, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width = 734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column =0, padx = 12)

        TopFrame2 = Frame(MainFrame, bd=7, width = 734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column =0, padx = 8)

        TopFrame2left = Frame(TopFrame2, bd=5, width = 190, height=300, relief=RIDGE)
        TopFrame2left.grid(row=0, column =0, padx = 8)

        TopFrame2mid = Frame(TopFrame2, bd=5, width = 200, height=300, relief=RIDGE)
        TopFrame2mid.grid(row=0, column =1, padx = 8)

        TopFrame2right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2right.grid(row=0, column=2, padx=8)


        self.txtReceipt = Text(TopFrame2mid, height = 17, width=42, bd=12, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0, column =0)

        self.img_arrow_Left = PhotoImage(file = 'arrowL.png')



if __name__=="__main__":
    root=Tk()
    application = atm(root)
    root.mainloop()