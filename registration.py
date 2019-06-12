#This frame consits the registration form for our centre

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import os
import sqlite3
import subprocess

#db connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

#list of limitation
age=[x for x in range(datetime.datetime.now().year-80, datetime.datetime.now().year-16)]
weight_list=[x for x in range(50,161)]
#main class
class Registration:
    def __init__(self, master):
        self.master = master

        self.left = Frame(master, width= 800, height= 600, bg='silver')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=600, bg="#4A586E")
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="REGISTRATION FORM", font=('arial 40 bold'), fg='black', bg='silver')
        self.heading.place(x=90, y=30)

        #form
        self.name = Label(self.left, text="Name", font=('arial 18 bold'), fg='black', bg='silver')
        self.name.place(x=140, y=130)

        self.age = Label(self.left, text="Birth Year", font=('arial 18 bold'), fg='black', bg='silver')
        self.age.place(x=140, y=170)

        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='silver')
        self.gender.place(x=140, y=210)

        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='silver')
        self.location.place(x=140, y=250)

        self.phone = Label(self.left, text="Phone", font=('arial 18 bold'), fg='black', bg='silver')
        self.phone.place(x=140, y=290)

        self.weigh = Label(self.left, text="Weigh", font=('arial 18 bold'), fg='black', bg='silver')
        self.weigh.place(x=140, y=330)

        self.blood = Label(self.left, text="Blood type", font=('arial 18 bold'), fg='black', bg='silver')
        self.blood.place(x=140, y=370)

        self.password = Label(self.left, text="Password", font=('arial 18 bold'), fg='black', bg='silver')
        self.password.place(x=140, y=410)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=390, y=130)

        self.age_ent = ttk.Combobox(self.left, state="choose", values=age, width=6)
        self.age_ent.set("Select")
        self.age_ent.place(x=390, y=170)

        self.varge = StringVar()
        self.gender_ent1= Radiobutton(self.left, text="Male", variable=self.varge, value="Male", bg='silver',anchor = W)
        self.gender_ent2= Radiobutton(self.left, text="Female", variable=self.varge, value="Female", bg='silver')

        self.gender_ent1.place(x=390, y=210)
        self.gender_ent2.place(x=460, y=210)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=390, y=250)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=390, y=290)

        self.weigh_ent = ttk.Combobox(self.left, state="choose", values=weight_list, width=6)
        self.weigh_ent.set("Select")
        self.weigh_ent.place(x=390, y=330)

        sqlq = "SELECT * FROM bloodtype"
        self.result = c.execute(sqlq)
        self.res=[]
        for self.row in self.result:
            self.res.append(self.row[1])
        self.blood_ent = ttk.Combobox(self.left, state="choose", values=self.res, width=6)
        self.blood_ent.set("Select")
        self.blood_ent.place(x=390, y=370)

        self.password_ent = Entry(self.left, width=30, show="*")
        self.password_ent.place(x=390, y=410)

        self.submit = Button(self.left, text="SUBMIT", width=20, height=2, bg='gold', command=self.add_appointment)
        self.submit.place(x=400, y=470)

        self.backbtn = Button(self.left, text="GO TO PREVIOUS PAGE", width=20, height=2, bg='silver', command=self.back)
        self.backbtn.place(x=150, y=470)

        sql2 = "SELECT COUNT(ID) FROM Clients"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
        self.logs = Label(self.right, text="INFO", font=('arial 28 bold'), fg='black', bg='#4A586E')
        self.logs.place(x=130, y=30)

        self.box = Text(self.right, width=44, height=27)
        self.box.insert(END, "Most people can give blood.\n\nYou can give blood if you:\n1)are fit and healthy \n2)weigh between 50kg and 160kg \n3)are aged between 17 and 80\n\nIf you have any questions then call us on \n0300 123 23 23.\n********************************************\n")
        self.box.insert(END, "There are " + str(self.id) + " clients. Join us.\n")

        self.box.place(x=20, y=90)


    #forms functions
    def add_appointment(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.varge.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.phone_ent.get()
        self.val6 = self.weigh_ent.get()
        self.val7 = self.blood_ent.get()
        self.val8 = self.password_ent.get()

        #checking for errors
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 =='' or self.val8 == '':
            messagebox.showinfo("Warning", "Please fill up all boxes")
        elif int(self.val2) not in age:
            messagebox.showinfo("Warning", "Please check your birthyear")
        elif int(self.val6) not in weight_list:
            messagebox.showinfo("Warning", "Please check your weigh")
        else:
            squ = "SELECT password FROM Clients WHERE phone LIKE ?"
            self.res = c.execute(squ, (self.val5,))
            self.pasres=[]
            for self.row in self.res:
                self.pasres.append(self.row[0])
            if (self.pasres != []):
                self.val8=self.pasres[0]
                messagebox.showinfo("Warning", "You have already an account.\n Your login and password are printed in info block.")
            else:
                squb = "SELECT id FROM bloodtype WHERE title LIKE ?"
                self.resb = c.execute(squb, (self.val7,))
                self.pasresb=[]
                for self.row in self.resb:
                    self.pasresb.append(self.row[0])
                if (self.pasresb == []):
                    messagebox.showinfo("Warning", "Check blood type!")
                else:
                    self.val7=self.pasresb[0]
                    sql = "INSERT INTO Clients (Name, birthYear, gender, location, phone, weigh, blood, password) VALUES(?,?,?,?,?,?,?,?)"
                    c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7, self.val8))
                    conn.commit()
                    messagebox.showinfo("Success", "Account for " + str(self.val1) + " has been created")
                    self.box.insert(END, 'Your login: ' + str(self.val5) + '\nYour password: ' + str(self.val8)+'\n\n')
                    self.name_ent.delete(0, 'end')
                    self.age_ent.set("Select")
                    self.gender_ent1.deselect()
                    self.gender_ent2.deselect()
                    self.location_ent.delete(0, 'end')
                    self.phone_ent.delete(0, 'end')
                    self.phone_ent.delete(0, 'end')
                    self.weigh_ent.set("Select")
                    self.blood_ent.set("Select")
                    self.password_ent.delete(0, 'end')
    def back(self):
        subprocess.Popen([sys.executable, "./main.py"])
        root.destroy()
root = Tk()
b = Registration(root)
root.title("Registration form")
root.geometry("1200x600+250+150")

imgicon = PhotoImage(file=os.path.join('./images/index3.png'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)
root.resizable(False, False)
root.mainloop()
