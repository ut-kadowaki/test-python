import tkinter as Tk

class Tktest(Tk.Frame):
    def __init__(self,master=None):
        Tk.Frame.__init__(self,master)
        self.master.title("自動化システム")
        self.master.geometry("300x650")

        #URL
        url = Tk.LabelFrame(self,text="スプレットシートURL")
        ad_url=Tk.Entry(url,width=20)
        ad_url.pack(side=Tk.LEFT)
        readbut=Tk.Button(url,text="読込")
        readbut.pack(side=Tk.LEFT,)
        url.pack(anchor=Tk.W, fill=Tk.X,ipadx=27)

        #掲載番号
        number = Tk.LabelFrame(self,text="掲載番号")
        OptionList =[" ","1","2","3"]
        variable = Tk.StringVar(number)
        variable.set(OptionList[0])
        opt = Tk.OptionMenu(number, variable, *OptionList)
        opt.config(width = 28)
        opt.pack()
        number.pack(anchor=Tk.W, fill=Tk.X)

        #クライアント名
        clientNamebox = Tk.LabelFrame(self,text="クライアント名")
        clientNamebox.pack(fill=Tk.X)
        c_name=Tk.Entry(clientNamebox)
        c_name.pack(fill=Tk.X)

        #enログインID
        log_id = Tk.LabelFrame(self,text="enログインID")
        log_id.pack(fill=Tk.X)
        en_id=Tk.Entry(log_id)
        en_id.pack(fill=Tk.X)

        #enログインPASSWORD
        log_pass = Tk.LabelFrame(self,text="enログインPASSWORD")
        log_pass.pack(fill=Tk.X)
        en_pass=Tk.Entry(log_pass)
        en_pass.pack(fill=Tk.X)

        #通数
        dev_stock = Tk.LabelFrame(self,text="通数")
        dev_stock.pack(fill=Tk.X)
        d_stock=Tk.Entry(dev_stock)
        d_stock.pack(fill=Tk.X)

        #掲載原稿の職種
        job = Tk.LabelFrame(self,text="掲載原稿の職種")
        job.pack(fill=Tk.X)
        j_name=Tk.Entry(job)
        j_name.pack(fill=Tk.X)

        #検索条件



if __name__ == '__main__':
    f = Tktest()
    f.pack()
    f.mainloop()
