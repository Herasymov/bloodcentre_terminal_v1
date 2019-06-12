from tkinter import *
from tkinter import messagebox
import os
import sqlite3
import datetime
import subprocess
#db connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

#list of ids from db
ids = []

#main program
class Myapp:
    def __init__(self, master):
        self.master = master

        self.left = Frame(master, width= 600, height= 300, bg='silver')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=300, height=300, bg="#4A586E")
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="SIGN UP FOR BLOOD TESTS", font=('arial 30 bold'), fg='black', bg='silver')
        self.heading.place(x=15, y=20)

        #form
        self.login = Label(self.left, text="Login", font=('arial 18 bold'), fg='black', bg='silver')
        self.login.place(x=60, y=90)

        self.password = Label(self.left, text="Password", font=('arial 18 bold'), fg='black', bg='silver')
        self.password.place(x=60, y=130)

        self.textreg = Label(self.left, text="Don't have an online account?\nBecome a blood donor", font=('arial 9'), fg='black', bg='silver')
        self.textreg.place(x=210, y=220)

        self.btn = Button(self.left, text="REGISTER", width=10, height=1, bg='green', command=self.func)
        self.btn.place(x=240, y=250)

        self.login = Entry(self.left, width=30)
        self.login.place(x=260, y=90)

        self.password = Entry(self.left, width=30, show="*")
        self.password.place(x=260, y=130)

        self.submit = Button(self.left, text="SIGN UP", width=20, height=2, bg='gold', command=self.func_signup)
        self.submit.place(x=200, y=170)

        self.backbtn = Button(self.left, text="GO TO PREVIOUS PAGE", width=20, height=2, bg='silver', command=self.back)
        self.backbtn.place(x=10, y=230)

        sql2 = "SELECT COUNT(ID) FROM Applications WHERE Status NOT LIKE ?"
        self.result = c.execute(sql2, ('Processed',))
        for self.row in self.result:
            self.id = self.row[0]
        if self.id =='':
            self.id=0
        self.box = Text(self.right, width=34, height=13)
        self.box.insert(END, "At the moment, " + str(self.id) + " applications have not been processed.\n")

        self.box.place(x=10, y=10)

    def back(self):
        subprocess.Popen([sys.executable, "./main.py"])
        root.destroy()
    def func(self):
        subprocess.Popen([sys.executable, "./registration.py"])
        root.destroy()
    def func_signup(self):
        self.val1 = self.login.get()
        self.val2 = self.password.get()
        squ = "SELECT name, id FROM Clients WHERE phone LIKE ? and password LIKE ?"
        self.res = c.execute(squ, (self.val1,self.val2,))
        self.pasres=[]
        for self.row in self.res:
            self.pasres.append(self.row[0])
            self.pasres.append(self.row[1])
        if (self.pasres == []):
            messagebox.showinfo("Warning", "Oops, something did not work out\nIncorrect phone/password combination.")
        else:
                sq = "SELECT Count(id) FROM Applications WHERE Client LIKE ? and Status NOT LIKE ?"
                self.res = c.execute(sq,(self.pasres[1], 'Processed', ))
                for self.r in self.res:
                    self.countres=int(self.r[0])
                if (self.countres !=0):
                    messagebox.showinfo("Warning", "You're already in queue!")
                else:
                    sql = "INSERT INTO Applications (time, Client, Status) VALUES(?,?,?)"
                    c.execute(sql, (datetime.datetime.now(), self.pasres[1], 'Waiting'))
                    conn.commit()
                    messagebox.showinfo("Success", "Application successfully created, please wait.")
                    sql3 = "SELECT id FROM Applications WHERE Client LIKE ?"
                    self.result1 = c.execute(sql3, (self.pasres[1],))
                    for self.row in self.result1:
                        self.id1 = self.row[0]
                    self.box.insert(END,str(self.pasres[0])+ " your number is " + str(self.id1)+"\n")
        self.login.delete(0, 'end')
        self.password.delete(0, 'end')
root = Tk()
b = Myapp(root)
root.title("Appointment")
root.geometry("900x300+400+300")
root.resizable(False, False)
imgicon = PhotoImage(file=os.path.join('/home/slaer98/Desktop/projects/python/myapp/images/index.ico'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.mainloop()
