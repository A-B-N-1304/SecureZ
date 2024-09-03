from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
global table, cursorr

from loginpage import loginpagefunc


def getdata():
    userFile = open('userlog.txt', 'r')

    i = userFile.readlines()
    userFile.close()
    return i


def show_saved_data():
    i = getdata()
    global userPhoneNumber, userName


    userPhoneNumber, userName, person1Phone, person2Phone, person3Phone, person1Mail, person2Mail, person3Mail = i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]
    head = Toplevel()
    bckgnd = PhotoImage(file='save_bgm.png')
    head.geometry('540x700')
    head.resizable(0, 0)

    bckground = Label(head, compound=CENTER, image=bckgnd)
    bckground.place(x=0, y=0, relwidth=1, relheight=1)

    title=Label(head, text='YOUR DATA', font=('Arial', 20), bd=10, height=2, width=31, bg='#BB03FF', fg='black')
    title.place(x=10, y=10)

    query1 = Label(head, text='Your Phone Number', bd=7, bg='white', fg='black')
    query1.place(x=10, y=150)

    entry1 = Label(head, text=userPhoneNumber, bd=5, bg='pink', fg='black')
    entry1.place(x=250, y=150)
    # User Name
    query2 = Label(head, text='Your Name', bd=7, bg='white', fg='black')
    query2.place(x=10, y=200)

    entry2 = Label(head, text=userName, bd=5, bg='pink', fg='black')
    entry2.place(x=250, y=200)

    #PHONE NUMBER 1
    query3 = Label(head, text='PHONE NUMBER 1', bd=7, bg='white', fg='black')
    query3.place(x=10, y=300)

    entry3 = Label(head, text=person1Phone, bd=5, bg='pink', fg='black')
    entry3.place(x=250, y=300)


    #PHONE NUMBER 2
    query4 = Label(head, text='PHONE NUMBER 2', bd=7, bg='white', fg='black')
    query4.place(x=10, y=350)

    entry4 = Label(head, text=person2Phone, bd=5, bg='pink', fg='black')
    entry4.place(x=250, y=350)

    #PHONE NUMBER 3
    query5 = Label(head, text='PHONE NUMBER 3', bd=7, bg='white', fg='black')
    query5.place(x=10, y=400)

    entry5 = Label(head, text=person3Phone, bd=5, bg='pink', fg='black')
    entry5.place(x=250, y=400)

    #MAIL 1
    query6 = Label(head, text='PERSON 1 MAIL ID', bd=7, bg='white', fg='black')
    query6.place(x=10, y=450)

    entry6 = Label(head, text=person1Mail, bd=5, bg='pink', fg='black')
    entry6.place(x=250, y=450)

    #MAIL 2
    query7 = Label(head, text='PERSON 2 MAIL ID', bd=7, bg='white', fg='black')
    query7.place(x=10, y=550)

    entry7 = Label(head, text=person2Mail, bd=5, bg='pink', fg='black')
    entry7.place(x=250, y=550)

    #MAIL 3
    query8 = Label(head, text='PERSON 3 MAIL ID', bd=7, bg='white', fg='black')
    query8.place(x=10, y=600)

    entry8 = Label(head, text=person3Mail, bd=5, bg='pink', fg='black')
    entry8.place(x=250, y=600)
    head.mainloop()


    def deletemydata():
        table = mysql.connector.connect(host='localhost', user='root', passwd='QWERTY1234', database='securez')
        cursorr = table.cursor()
        q = 'DELETE FROM users where userphonenumber = {}'.format(userPhoneNumber)
        cursorr.execute(q)
        table.close()
        os.remove('userlog.txt')
        messagebox.showinfo("Your account have been successfully Deleted !")
        head.destroy()
        loginpagefunc()
        return None

    dele = Button(head, text='Delete My Data', bd=6, command=deletemydata)
    dele.place(x=50, y=610)



def editbutton():

    edit = Toplevel()   #change the BG if you want..  and change to toplevel()
    bckgnd = PhotoImage(file='edit_bgm.png')
    edit.geometry('540x700')
    edit.resizable(0, 0)

    bckground = Label(edit, compound=CENTER, image=bckgnd)
    bckground.place(x=0, y=0, relwidth=1, relheight=1)

    person1_phone = Label(edit, text='PERSON 1 \n Phone number', bd=4, bg='#C685D6', fg='black')
    person1_phone.place(x=10, y=300)

    person1_phone_entry = Entry(edit, bd=2, bg='#7B436A')
    person1_phone_entry.place(x=250, y=300)

    person1_mail = Label(edit, text='PERSON 1 \n Email ID', bd=4, bg='#C685D6', fg='black')
    person1_mail.place(x=10, y=350)

    person1_mail_entry = Entry(edit, bd=2, bg='#7B436A')
    person1_mail_entry.place(x=250, y=350)

    # PERSON 2 CREDENTIALS
    person2_phone = Label(edit, text='PERSON 2 \n Phone number', bd=4, bg='#A03870', fg='black')
    person2_phone.place(x=10, y=400)

    person2_phone_entry = Entry(edit, bd=2, bg='#AA5D83')
    person2_phone_entry.place(x=250, y=400)

    person2_mail = Label(edit, text='PERSON 2 \n Email ID', bd=4, bg='#A03870', fg='black')
    person2_mail.place(x=10, y=450)

    person2_mail_entry = Entry(edit, bd=2, bg='#AA5D83')
    person2_mail_entry.place(x=250, y=450)

    # PERSON 3 CREDENTIALS
    person3_phone = Label(edit, text='PERSON 3 \n Phone number', bd=4, bg='#CDC2B7', fg='black')
    person3_phone.place(x=10, y=500)

    person3_phone_entry = Entry(edit, bd=2, bg='#B8A899')
    person3_phone_entry.place(x=250, y=500)

    person3_mail = Label(edit, text='PERSON 3 \n Email ID', bd=4, bg='#CDC2B7', fg='black')
    person3_mail.place(x=10, y=550)

    person3_mail_entry = Entry(edit, bd=2, bg='#B8A899')
    person3_mail_entry.place(x=250, y=550)

    def submitbutton():

        table = mysql.connector.connect(host='localhost', user='root', passwd='QWERTY1234', database='securez')
        cursorr = table.cursor()
        file = open('userlog.txt', 'w+')
        db = mysql.connector.connect(host='localhost', user='root', passwd='QWERTY1234', database='securez')
        person1Mail = person1_mail_entry.get()
        person1Phone = person1_phone_entry.get()
        try:
            a = int(person1Phone)
        except:
            messagebox.showwarning("Warning", "Check Person 1 phone number")
            return None
        if len(person1Phone) != 10:
            messagebox.showwarning("Warning", "Check Person 1 phone number")
            return None
        person2Mail = person2_mail_entry.get()
        person2Phone = person2_phone_entry.get()
        try:
            a = int(person2Phone)
        except:
            messagebox.showwarning("Warning", "Check Person 2 phone number")
            return None
        if len(person2Phone) != 10:
            messagebox.showwarning("Warning", "Check Person 2 phone number")
            return None
        person3Mail = person3_mail_entry.get()
        person3Phone = person3_phone_entry.get()
        try:
            a = int(person3Phone)
        except:
            messagebox.showwarning("Warning", "Check Person 3 phone number")
            return None
        if len(person3Phone) != 10:
            messagebox.showwarning("Warning", "Check Person 3 phone number")
            return None

        DBsubmission = "UPDATE users SET phonenumber1 = '{}', phonenumber2 = '{}', phonenumber3 = '{}', email1 = '{}', email2 = '{}', email3 = '{}' WHERE userphonenumber = '{}'".format(
            person1Phone, person2Phone, person3Phone, person1Mail, person2Mail, person3Mail, userPhoneNumber)
        cursorr.execute(DBsubmission)
        table.commit()
        table.close()

        infolist = [userPhoneNumber + '\n', userName + '\n', person1Phone + '\n', person2Phone + '\n',
                    person3Phone + '\n', person1Mail + '\n', person2Mail + '\n',
                    person3Mail + '\n']
        file.writelines(infolist)
        file.close()
        messagebox.showinfo("SUCCESS", "Your data was modified successfully . Saved data will be opened shortly ..")
        show_saved_data()
        edit.destroy()

    submitButton = Button(edit, text="Submit", bd=5, command=submitbutton)
    submitButton.place(x=200, y=620)

    edit.mainloop()









