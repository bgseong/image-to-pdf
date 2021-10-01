from tkinter import *
from typing import List
from tkinter import filedialog, messagebox, Menu
from tkinter.ttk import Progressbar
from PIL import Image
import os
root=Tk()

root.title("image-to-pdf")
root.geometry("200x250")
root.resizable(False,False)



listsbox=Listbox(root,selectmode=MULTIPLE)
listsbox.grid(row=0,column=0,ipadx=10,ipady=30)
def add():
    global listsbox
    root.filename = filedialog.askopenfilename(initialdir='',multiple=True,
    title='파일선택',
    filetypes=(
    ('png files', '*.png'),
    ('jpg files', '*.jpg'),
    ('all files', '*.*')))
    for i in range(len(root.filename)):
        listsbox.insert(END,root.filename[i])

def delete():
    global listsbox
    aaa=listsbox.curselection()
    for i in range(len(aaa)):
        listsbox.delete(aaa[i-1])
    
def pdf():
    global listsbox
    try:
        lists=[]
        new_list=[]

        files=listsbox.get(0,listsbox.size())
        for i in range(len(files)):
            img=Image.open(files[i])
            img=img.convert("RGB")
            lists.append(img)

        img_1=lists[0]
        if len(lists) != 1:
            for i in range(1,len(lists)):
                new_list.append(lists[i])

        img_1.save(os.getcwd()+"/image.pdf", save_all=True,append_images=new_list)
    except:
        messagebox.showerror("ERROR", "파일이 없습니다.")

menu=Menu(root)
menu_item=Menu(menu)
menu_item.add_command(label="불러오기", command=add)
menu_item.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File", menu=menu_item)
root.config(menu=menu)

bt1=Button(root,text="...",command=add)
bt1.grid(row=0,column=1,sticky=N)

bt2=Button(root,text="삭제",command=delete)
bt2.grid(row=0,column=1,sticky=S)

bt3=Button(root,text="변환",command=pdf)
bt3.grid(row=1,column=0)


root.mainloop()
