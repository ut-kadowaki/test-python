import tkinter

root = tkinter.Tk()
root.title("スカウト自動化")
root.geometry("300x650")


#ラベルフレームを配置
url_frame = tkinter.LabelFrame(root,text="スプレットシート url",relief="ridge",bd=2)
url_frame.pack(pady=10)

url_box = tkinter.Entry(url_frame,width=30,bd=2)


#url_box = tkinter.Entry(width=30)
#url_box.place(x=40, y=30)
#url_label = tkinter.Label(text="スプレットシート url")
#url_label.place(x=40, y=6)
#read_button = tkinter.Button(text="読込")
#read_button.place(x=220, y=27)

root.mainloop()