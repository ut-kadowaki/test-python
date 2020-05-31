import tkinter as Tk
class UItest(Tk.Frame):

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Pack Three Labels')
     
        # First Label
        la = Tk.Label(self, text='Hello everybody. How are you?',  bg='yellow', relief=Tk.RIDGE, bd=2)
        la.pack()
     
        # Second Label
        lb = Tk.Label(self, text='Oh My God!', bg='red', relief=Tk.RIDGE, bd=2)
        lb.pack()
     
        # Third Label
        lc = Tk.Label(self, text='See you tomorrow.', bg='LightSkyBlue', relief=Tk.RIDGE, bd=2)
        lc.pack()
     
    ##----------------
if __name__ == '__main__':
    f = UItest()
    f.pack()
    f.mainloop()