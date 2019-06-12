from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import sqlite3
import os
import subprocess
from PIL import Image, ImageTk
import runpy
import datetime
#db connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

#list of ids from db
ids = []
Login_num=""
Password_num=""
class Application:
    def __init__(self, master):
        self.master = master
        self.header = Frame(master, width= 1360, height= 150, bg='#E4FFF9', borderwidth = 1, relief = SUNKEN)
        self.header.pack(side=TOP)

        image = Image.open("images/logo_ma.png")
        photo = ImageTk.PhotoImage(image)
        self.label = Label(self.header, image=photo,bg='#E4FFF9')
        self.label.image = photo
        self.label.place(x=500,y=0)

        image1 = Image.open("images/login.png")
        photo1 = ImageTk.PhotoImage(image1)
        self.sgnbtn = Button(self.header, image = photo1, command=self.func11, bg='#E4FFF9')
        self.sgnbtn.image = photo1
        self.sgnbtn.place(x=1150, y=10)

        self.left = Frame(master, width= 800, height= 670, bg='white')
        self.left.pack(side=LEFT)

        self.text = Label(self.left, text=("Contact details\n\nAddress:\t26 Margaret Street \n\tLondon\n\tW1W 8NB\nPhone:\t0300 123 23 23"),justify=LEFT, font=('arial 18'),fg='black', bg='white')
        self.text.place(x=10, y=20)

        image = Image.open("images/centre_pic.jpg")
        photo = ImageTk.PhotoImage(image)
        self.pic = Label(self.left, image=photo)
        self.pic.image = photo
        self.pic.place(x=420,y=3)

        self.text = Label(self.left, text=("Where to find us:"),justify=LEFT, font=('arial 25'),fg='black', bg='white')
        self.text.place(x=10, y=225)

        image = Image.open("images/map.png")
        photo = ImageTk.PhotoImage(image)
        self.pic = Label(self.left, image=photo)
        self.pic.image = photo
        self.pic.place(x=0,y=270)

        self.right = Frame(master, width=560, height= 670, bg='#F0F6F4')
        self.right.pack(side=RIGHT)

        self.mains = Frame(self.right, width=560, height= 670, bg='#C9FFBF')
        self.mains.place(x=0, y=0)


        self.login = Frame(self.mains, width=560, height= 167, bg='#C9FFBF')
        self.login.place(x=0, y=0)
        self.textreg = Label(self.login, text=("Register"), font=('arial 25 bold'),fg='black', bg='#C9FFBF')
        self.textreg.place(x=200, y=10)
        self.textreg2 = Label(self.login, text=("Become a blood donor"), font=('arial 18'),fg='black', bg='#C9FFBF')
        self.textreg2.place(x=150, y=50)
        self.change = Button(self.login, text="Register", font=('arial 12 bold'), height=2, command=self.func, fg='black', bg='Green')
        self.change.place(x=220, y=90)

        self.apply = Frame(self.mains, width=560, height= 168, bg='#FBCEB5')
        self.apply.place(x=0, y=167)
        self.textapp = Label(self.apply, text=("Getting an appointment"), font=('arial 25 bold'),fg='black', bg='#FBCEB5')
        self.textapp.place(x=90, y=10)
        self.textapp2 = Label(self.apply, text=("Don't wait - apply now"), font=('arial 18'),fg='black', bg='#FBCEB5')
        self.textapp2.place(x=140, y=50)
        self.change2 = Button(self.apply, text="Apply", font=('arial 12 bold'),height=2, command=self.func1, fg='black', bg='#FF756B')
        self.change2.place(x=230, y=90)

        self.check = Frame(self.mains, width=560, height= 167, bg='#FBE7B5')
        self.check.place(x=0, y=335)
        self.textcheck = Label(self.check, text=("Update your account"), font=('arial 25 bold'),fg='black', bg='#FBE7B5')
        self.textcheck.place(x=100, y=10)
        self.textcheck2 = Label(self.check, text=("View, update, delete account"), font=('arial 18'),fg='black', bg='#FBE7B5')
        self.textcheck2.place(x=120, y=50)
        self.change3 = Button(self.check, text="Apply", font=('arial 12 bold'),height=2, command=self.func2, fg='black', bg='#FFAD32')
        self.change3.place(x=230, y=90)

        self.tabloid = Frame(self.mains, width=560, height= 168, bg='#BBC9DD')
        self.tabloid.place(x=0, y=502)
        self.texttabloid = Label(self.tabloid, text=("History"), font=('arial 25 bold'),fg='black', bg='#BBC9DD')
        self.texttabloid.place(x=200, y=10)
        self.texttabloid2 = Label(self.tabloid, text=("View blood donation history "), font=('arial 18'),fg='black', bg='#BBC9DD')
        self.texttabloid2.place(x=130, y=50)
        self.change4 = Button(self.tabloid, text="Check", font=('arial 12 bold'),height=2, command=self.func3, fg='black', bg='#0043A4')
        self.change4.place(x=230, y=90)


    def func(self):
        subprocess.Popen([sys.executable, "./registration.py"])
        root.destroy()
    def func11(self):
        root1 = Tk()
        root1.title("AUTHORIZATION")
        root1.geometry("450x160+500+400")
        root1.resizable(False, False)
        self.login = Label(root1, text="Login", font=('arial 18 bold'), fg='black')
        self.login.place(x=10, y=10)

        self.password = Label(root1, text="Password", font=('arial 18 bold'), fg='black')
        self.password.place(x=10, y=50)

        self.login = Entry(root1, width=20)
        self.login.place(x=210, y=10)

        self.password = Entry(root1, width=20, show="*")
        self.password.place(x=210, y=50)

        self.submit = Button(root1, text="SIGN UP", width=20, height=2, bg='gold', command=self.func_signup)
        self.submit.place(x=200, y=90)

    def func_signup(self):
        self.val1 = self.login.get()
        self.val2 = self.password.get()
        squ = "SELECT id, name FROM Clients WHERE phone LIKE ? and password LIKE ?"
        self.res = c.execute(squ, (self.val1,self.val2,))
        self.pasres=[]
        for self.row in self.res:
            self.pasres.append(self.row[0])
            self.pasres.append(self.row[1])
        if (self.pasres == []):
            messagebox.showinfo("Warning", "Oops, something did not work out\nIncorrect phone/password combination.")
        else:
            self.sgnbtn.destroy()
            self.welcome= Frame(self.mains, width=560, height= 167, bg='#C9FFBF')
            self.welcome.place(x=0, y=0)
            self.textw = Label(self.welcome, text=("Hello, "+str(self.pasres[1])), font=('arial 25 bold'),fg='black', bg='#C9FFBF')
            self.textw.place(x=170, y=10)
            self.textw2 = Label(self.welcome, text=("Happy to see you in our centre!"), font=('arial 18'),fg='black', bg='#C9FFBF')
            self.textw2.place(x=100, y=50)
            self.bye = Button(self.welcome, text="Log out", font=('arial 12 bold'), height=2, command=self.logout, fg='black', bg='#C9FFBF')
            self.bye.place(x=240, y=90)

            self.changereg2 = Button(self.apply, text="Apply", font=('arial 12 bold'),height=2, command=self.funcappoint, fg='black', bg='#FF756B')
            self.changereg2.place(x=230, y=90)

            self.change3q = Button(self.check, text="Apply", font=('arial 12 bold'),height=2, command=self.funcupdatereg, fg='black', bg='#FFAD32')
            self.change3q.place(x=230, y=90)

            self.change4q = Button(self.tabloid, text="Check", font=('arial 12 bold'),height=2, command=self.funchistory, fg='black', bg='#0043A4')
            self.change4q.place(x=230, y=90)

    def funcappoint(self):
        squ = "SELECT Count(id) FROM Applications WHERE Client LIKE ? and Status NOT LIKE ?"
        self.res = c.execute(squ,(self.pasres[0], 'Processed', ))
        for self.r in self.res:
            self.countres=int(self.r[0])
            print(self.countres)
        if (self.countres !=0):
            messagebox.showinfo("Warning", "You're already in queue!")
        else:
            sql = "INSERT INTO Applications (time, Client, Status) VALUES(?,?,?)"
            c.execute(sql, (datetime.datetime.now(), self.pasres[0], 'Waiting'))
            conn.commit()
            sql3 = "SELECT id FROM Applications WHERE Client LIKE ? and Status LIKE ?"
            self.result1 = c.execute(sql3, (self.pasres[0], 'Waiting'))
            for self.row in self.result1:
                self.id1 = self.row[0]
            messagebox.showinfo("Success", "successfully created\n Your number is " + str(self.id1)+"\n.")
    def logout(self):
        self.welcome.destroy()
        self.changereg2.destroy()
        self.change3q.destroy()
        self.change4q.destroy()

        image1 = Image.open("images/login.png")
        photo1 = ImageTk.PhotoImage(image1)
        self.sgnbtn = Button(self.header, image = photo1, command=self.func11, bg='#E4FFF9')
        self.sgnbtn.image = photo1
        self.sgnbtn.place(x=1150, y=10)

    def funcupdatereg(self):
        subprocess.Popen([sys.executable, "./update.py"])
        root.destroy()
    def func1(self):
        subprocess.Popen([sys.executable, "./applying_process.py"])
        root.destroy()
    def func2(self):
        subprocess.Popen([sys.executable, "./update2.py"])
        root.destroy()
    def func3(self):
        subprocess.Popen([sys.executable, "./history.py"])
        root.destroy()
    def funchistory(self):
        subprocess.Popen([sys.executable, "./history2.py"])
        root.destroy()
root = Tk()
b = Application(root)
root.title("Menu")
root.geometry("1360x820+140+0")
imgicon = PhotoImage(file=os.path.join('./images/index.ico'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.resizable(False, False)
root.mainloop()
