from tkinter import *
from tkinter import ttk
import os
import subprocess

class Startpage:
    def __init__(self, master):
        self.master=master
        self.heading = Label(master, text="Choose role", font=('arial 30 bold'), fg='black')
        self.heading.place(x=70, y=20)

        self.btn = Button(master, text="CLIENT", width=20, height=2, bg='green', command=self.clientfunc)
        self.btn.place(x=10, y=80)

        self.btn = Button(master, text="ADMIN", width=20, height=2, bg='yellow', command=self.adminfunc)
        self.btn.place(x=200, y=80)

    def clientfunc(self):
        subprocess.Popen([sys.executable, "./main.py"])
        root.destroy()
    def adminfunc(self):
        subprocess.Popen([sys.executable, "./display.py"])
        root.destroy()
root = Tk()
b = Startpage(root)
root.title("Start page")
root.geometry("400x150+600+350")
root.resizable(False, False)
imgicon = PhotoImage(file=os.path.join('/home/slaer98/Desktop/projects/python/myapp/images/index.ico'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.mainloop()
