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
        self.heading = Label(master, text="View, update or delete an account", font=('arial 40 bold'), fg='black')
        self.heading.place(x=50, y=30)

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
        self.backbtn.place(x=80, y=570)
    def search_db(self):
        self.input = self.namenet.get()
        self.input2 = self.passnet.get()
        sql = "SELECT * FROM Clients WHERE phone LIKE ? and password Like ?"
        self.res = c.execute(sql, (self.input, self.input2,))
        self.n=0
        for self.row in self.res:
            self.rid=self.row[0]
            self.rname= self.row[1]
            self.rage=self.row[2]
            self.rgender=self.row[3]
            self.rlocation=self.row[4]
            self.rphone=self.row[5]
            self.rweigh=self.row[6]
            self.rblood=self.row[7]
            self.rpassword=self.row[8]
            self.n=1
        if (self.n==1):
            self.name = Label(self.master, text="Name", font=('arial 18 bold'), fg='black')
            self.name.place(x=200, y=230)

            self.age = Label(self.master, text="Birth Year", font=('arial 18 bold'), fg='black' )
            self.age.place(x=200, y=270)

            self.gender = Label(self.master, text="Gender", font=('arial 18 bold'), fg='black' )
            self.gender.place(x=200, y=310)

            self.location = Label(self.master, text="Location", font=('arial 18 bold'), fg='black' )
            self.location.place(x=200, y=350)

            self.phone = Label(self.master, text="Phone", font=('arial 18 bold'), fg='black' )
            self.phone.place(x=200, y=390)

            self.weigh = Label(self.master, text="Weigh", font=('arial 18 bold'), fg='black' )
            self.weigh.place(x=200, y=430)

            self.blood = Label(self.master, text="Blood type", font=('arial 18 bold'), fg='black' )
            self.blood.place(x=200, y=470)

            self.password = Label(self.master, text="Password", font=('arial 18 bold'), fg='black' )
            self.password.place(x=200, y=510)

            self.name_ent = Entry(self.master, width=30)
            self.name_ent.insert(END, str(self.rname))
            self.name_ent.place(x=530, y=230)

            self.age_ent = ttk.Combobox(self.master, values=age, width=6)
            self.age_ent.set(str(self.rage))
            self.age_ent.place(x=530, y=270)

            self.varge = StringVar()
            self.gender_ent1= Radiobutton(self.master, text="Male", variable=self.varge, value="Male" )
            self.gender_ent2= Radiobutton(self.master, text="Female", variable=self.varge, value="Female" )
            if self.rgender == "Male":
                self.gender_ent1.select()
            else:
                self.gender_ent2.select()


            self.gender_ent1.place(x=530, y=310)
            self.gender_ent2.place(x=600, y=310)

            self.location_ent = Entry(self.master, width=30)
            self.location_ent.insert(END, str(self.rlocation))
            self.location_ent.place(x=530, y=350)

            self.phone_ent = Entry(self.master, width=30)
            self.phone_ent.insert(END, str(self.rphone))
            self.phone_ent.place(x=530, y=390)

            self.weigh_ent = ttk.Combobox(self.master, values=weight_list, width=6)
            self.weigh_ent.set(str(self.rweigh))
            self.weigh_ent.place(x=530, y=430)

            sqlq1 = "SELECT title FROM bloodtype Where id LIKE ?"
            self.result = c.execute(sqlq1, (str(self.rblood),))
            self.res=[]
            for self.row in self.result:
                self.res.append(self.row[0])
            self.blood_ent = ttk.Combobox(self.master, values=self.res, width=6)
            self.blood_ent.set(self.res[0])
            self.blood_ent.place(x=530, y=470)

            self.password_ent = Entry(self.master, width=30)
            self.password_ent.insert(END, str(self.rpassword))
            self.password_ent.place(x=530, y=510)

            self.update = Button(self.master, text="Update", width=20, height=2, bg='green', command=self.update_db)
            self.update.place(x=390, y=570)

            self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
            self.delete.place(x=740, y=570)


    def back(self):
        subprocess.Popen([sys.executable, "./main.py"])
        root.destroy()

    def update_db(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.varge.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.phone_ent.get()
        self.val6 = self.weigh_ent.get()
        self.val7 = self.blood_ent.get()
        self.val8 = self.password_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 =='' or self.val8 == '':
            messagebox.showinfo("Warning", "Please fill up all boxes")
        elif int(self.val2) not in age:
            messagebox.showinfo("Warning", "Please check your birthyear")
        elif int(self.val6) not in weight_list:
            messagebox.showinfo("Warning", "Please check your weigh")
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
                sql = "UPDATE Clients SET Name=?, birthYear=?, gender=?, location=?, phone=?, weigh=?, blood=?, password=? WHERE phone like ?"
                c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7, self.val8, self.namenet.get(),))
                conn.commit()
                messagebox.showinfo("Success", "Account for " + str(self.val1) + " was updated")
                self.name_ent.destroy()
                self.age_ent.destroy()
                self.gender_ent1.destroy()
                self.gender_ent2.destroy()
                self.location_ent.destroy()
                self.phone_ent.destroy()
                self.weigh_ent.destroy()
                self.blood_ent.destroy()
                self.password_ent.destroy()
                self.name.destroy()
                self.age.destroy()
                self.gender.destroy()
                self.location.destroy()
                self.phone.destroy()
                self.weigh.destroy()
                self.blood.destroy()
                self.password.destroy()
                self.update.destroy()
                self.delete.destroy()
                self.namenet.delete(0, 'end')

    def delete_db(self):
        MsgBox = messagebox.askquestion ('delete action','Are you sure you want to delete an account with all blood donation history',icon = 'warning')
        if MsgBox == 'yes':
            querydel = "DELETE from Applications WHERE Client like ?"
            self.run = c.execute(querydel, (self.rid,))
            conn.commit()
            query2 = "DELETE from Clients WHERE phone like ?"
            self.run = c.execute(query2, ( self.namenet.get(),))
            conn.commit()
            messagebox.showinfo("Updated", "Successfully Deleted")
            self.name_ent.destroy()
            self.age_ent.destroy()
            self.gender_ent1.destroy()
            self.gender_ent2.destroy()
            self.location_ent.destroy()
            self.phone_ent.destroy()
            self.weigh_ent.destroy()
            self.blood_ent.destroy()
            self.password_ent.destroy()
            self.name.destroy()
            self.age.destroy()
            self.gender.destroy()
            self.location.destroy()
            self.phone.destroy()
            self.weigh.destroy()
            self.blood.destroy()
            self.password.destroy()
            self.update.destroy()
            self.delete.destroy()
            self.namenet.delete(0, 'end')

root = Tk()
b=Application(root)
root.title("Update")
root.geometry("1000x650+300+150")
root.resizable(False, False)
root.mainloop()
