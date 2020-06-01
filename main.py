import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.master.geometry("300x650")
        self.master.title("自動化システム")
        self.create_widgets()

    def create_widgets(self):
        #URL
        url = tk.LabelFrame(self,text="スプレットシートURL")
        self.ad_url=tk.Entry(url,width=20)
        self.ad_url.pack(side=tk.LEFT)
        self.readbut=tk.Button(url,text="読込")
        self.readbut.pack(side=tk.LEFT,)
        url.pack(anchor=tk.W, fill=tk.X,ipadx=27)

        #掲載番号
        number = tk.LabelFrame(self,text="掲載番号")
        OptionList =[" ","1","2","3"]
        self.variable = tk.StringVar(number)
        self.variable.set(OptionList[0])
        self.opt = tk.OptionMenu(number, self.variable, *OptionList)
        self.opt.config(width = 28)
        self.opt.pack()
        number.pack(anchor=tk.W, fill=tk.X)

        #クライアント名
        clientNamebox = tk.LabelFrame(self,text="クライアント名")
        clientNamebox.pack(fill=tk.X)
        self.c_name=tk.Entry(clientNamebox)
        self.c_name.pack(fill=tk.X)

        #enログインID
        log_id = tk.LabelFrame(self,text="enログインID")
        log_id.pack(fill=tk.X)
        self.en_id=tk.Entry(log_id)
        self.en_id.pack(fill=tk.X)

        #enログインPASSWORD
        log_pass = tk.LabelFrame(self,text="enログインPASSWORD")
        log_pass.pack(fill=tk.X)
        self.en_pass=tk.Entry(log_pass)
        self.en_pass.pack(fill=tk.X)

        #通数
        dev_stock = tk.LabelFrame(self,text="通数")
        dev_stock.pack(fill=tk.X)
        self.d_stock=tk.Entry(dev_stock)
        self.d_stock.pack(fill=tk.X)

        #掲載原稿の職種
        job = tk.LabelFrame(self,text="掲載原稿の職種")
        job.pack(fill=tk.X)
        self.j_name=tk.Entry(job)
        self.j_name.pack(fill=tk.X)

        #検索条件
        search = tk.LabelFrame(self,text="検索条件")
        search.pack(fill=tk.X)

        searchlist=["条件１","条件2","条件3"]
        self.searchCondition = tk.StringVar(self)
        self.searchConditionText = tk.Entry(search, textvariable=self.searchCondition).pack(fill=tk.X)
        self.searchConditionOption = tk.OptionMenu(search,self.searchCondition, *searchlist)
        self.searchConditionOption.pack(fill=tk.X)

        #年齢下限
        miniage = tk.LabelFrame(self,text="年齢下限")
        miniage.pack(fill=tk.X)
        self.mini_age=tk.Entry(miniage)
        self.mini_age.pack(fill=tk.X)

        #年齢上限
        maxage = tk.LabelFrame(self,text="年齢上限")
        maxage.pack(fill=tk.X)
        self.max_age=tk.Entry(maxage)
        self.max_age.pack(fill=tk.X)

        #性別
        number = tk.LabelFrame(self,text="性別")
        OptionList =["なし","男","女"]
        self.variable = tk.StringVar(number)
        self.variable.set(OptionList[0])
        self.opt = tk.OptionMenu(number, self.variable, *OptionList)
        self.opt.config(width = 28)
        self.opt.pack()
        number.pack(anchor=tk.W, fill=tk.X)

        #市区町村（「,」区切りで複数入力可能）
        aa_dd = tk.LabelFrame(self,text="市区町村「,」区切りで複数入力可能")
        aa_dd.pack(fill=tk.X)
        self.ad_txt=tk.Entry(aa_dd)
        self.ad_txt.pack(fill=tk.X)

        #その他言語
        ln_ge = tk.LabelFrame(self,text="その他言語が「---」の人以外も対象にする")
        ln_ge.pack(fill=tk.X)
        self.chk_but = tk.Checkbutton(ln_ge)
        self.chk_but.pack(fill=tk.X) 

        #テスト実行
        test_mode = tk.LabelFrame(self,text="実際に追加しない（テスト実行）")
        test_mode.pack(fill=tk.X)
        self.intvar2 = tk.IntVar()
        self.intvar2.set(True)
        self.chk2 = tk.Checkbutton(test_mode,variable=self.intvar2,)
        self.chk2.pack()

        #実行ボタン
        apButton = tk.Button(text=u'実行', width=40)
        apButton.pack(pady=10)

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()