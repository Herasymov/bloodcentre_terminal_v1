from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import datetime
import subprocess

conn = sqlite3.connect('database.db')
c = conn.cursor()

#list of limitation
age=[x for x in range(datetime.datetime.now().year-80, datetime.datetime.now().year-16)]
weight_list=[x for x in range(50,161)]

class Application:
    def __init__(self, master):
        self.master = master
        self.heading = Label(master, text="Blood donation history", font=('arial 40 bold'), fg='black')
        self.heading.place(x=200, y=30)

        self.name = Label(master, text="Enter phone", font=('arial 28 bold'))
        self.name.place(x=10, y = 110)

        self.namenet = Entry(master, width=25)
        self.namenet.place(x=240, y=125)

        self.pass1 = Label(master, text="Enter password", font=('arial 28 bold'))
        self.pass1.place(x=460, y = 110)

        self.passnet = Entry(master, width=25, show="*")
        self.passnet.place(x=750, y=125)

        self.search = Button(master, text="Search", width=20, height=2, bg='gold', command=self.search_db)
        self.search.place(x=380, y=170)

        self.backbtn = Button(self.master, text="GO TO PREVIOUUS PAGE", width=20, height=2, command=self.back)
        self.backbtn.place(x=80, y=750)
    def search_db(self):
        self.input = self.namenet.get()
        self.input2 = self.passnet.get()
        sql = "SELECT id, name FROM Clients WHERE phone LIKE ? and password Like ?"
        self.res = c.execute(sql, (self.input, self.input2,))
        self.n=0
        for self.row in self.res:
            self.rid=self.row[0]
            self.rname= self.row[1]
            self.n=1
        if (self.n==0):
            messagebox.showinfo("Warning", "Oops, something did not work out\nIncorrect phone/password combination.")
        else:
            self.box = Text(self.master, width=100, height=30)
            self.box.insert(END,str(self.rname) + "'s blood donation history \n********************************************\n")
            self.box.place(x=100, y=220)

            sq = "SELECT * FROM Applications WHERE Client LIKE ?"
            self.res = c.execute(sq,(self.rid, ))
            for r in self.res:
                self.box.insert(END,"№"+str(r[0])+ " Apply date: " + str(r[1])+" Apply status: "+str(r[3])+"\n********************************************\n")



    def back(self):
        subprocess.Popen([sys.executable, "./main.py"])
        root.destroy()



root = Tk()
b=Application(root)
root.title("History")
root.geometry("1000x820+300+0")
root.resizable(False, False)
root.mainloop()
