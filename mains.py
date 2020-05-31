import tkinter as Tk

class Tktest(Tk.Frame):
    def __init__(self,master=None):
        Tk.Frame.__init__(self,master)
        self.master.title("自動化システム")
        self.master.geometry("300x650")

        #URL
        url = Tk.LabelFrame(self,text="スプレットシートURL")
        url.pack(anchor=Tk.W, fill=Tk.X,ipadx=27)
        self.txt=Tk.Entry(url,width=20)
        self.txt.pack(side=Tk.LEFT)
        self.but=Tk.Button(url,text="読込")
        self.but.pack(side=Tk.LEFT,)
        url.pack(anchor=Tk.W, fill=Tk.X)



if __name__ == '__main__':
    f = Tktest()
    f.pack()
    f.mainloop()
