import tkinter as Tk

class Tktest(Tk.Frame):
    


    #ラベルフレームを配置
    url_frame = Tk.LabelFrame(root, text='スプレットシート url')
    url_frame.pack(anchor=Tk.W, fill=Tk.X)
    root.url = Tk.Entry(url_frame)
    root.url.pack(side=Tk.LEFT) 
    root.url_butt = Tk.Button(url_frame,text="読込")
    root.url_butt.pack(side=Tk.LEFT)
    url_box = Tk.Entry(url_frame,width=30,bd=2)
    url_frame.pack(pady=10)

    
    root = Tk.Tk()
    root.title("スカウト自動化")
    root.geometry("300x650")

    root.mainloop()