from tkinter import *
from tkinter import messagebox
import mysql.connector
import sys



def loginpagefunc():
    global closebutton_isactivated
    closebutton_isactivated = False
    while not closebutton_isactivated:
        win = Tk(className='Login')
        win.geometry('480x700')
        win.resizable(0, 0)
        table = mysql.connector.connect(host='localhost', user='root', passwd='Anish_1319007', database='securez')
        if table.is_connected() == True:
            print("YAYYYYY")
        global cursorr
        cursorr = table.cursor()
        cursorr.execute('Select * from users')


        t = 'YOU ARE REQUESTED TO GIVE PHONE NUMBERS AND EMAIL ID OF 3 RELATIVES \n OF YOURS TO BE CONTACTED DURING EMERGENCY'

        pic = PhotoImage(file="login_bgm.png")
        background_label = Label(win, compound=CENTER, image=pic)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # User Phone Number
        query1 = Label(win, text='Enter your phone number:-', bd=4, bg='#0F52B9', fg='black')
        query1.place(x=10, y=80)

        entry1 = Entry(win, bd=2, bg='#00A5FF')
        entry1.place(x=250, y=80)
        # User Name
        query2 = Label(win, text='Your Name:-', bd=4, bg='#0F52B9', fg='black')
        query2.place(x=10, y=150)

        entry2 = Entry(win, bd=2, bg='#00A5FF')
        entry2.place(x=250, y=150)

        found = False
        def signupbutton():
            messagebox.showwarning('No Account available', "You haven't created a account in Securez")
            information = Label(win, compound=CENTER, text=t, bd=20, bg='#D3CCE3', fg='black')
            information.place(x=10, y=200)

            # Person 1 CREDENTIALS
            person1_phone = Label(win, text='PERSON 1 \n Phone number', bd=4, bg='#C685D6', fg='black')
            person1_phone.place(x=10, y=300)

            person1_phone_entry = Entry(win, bd=2, bg='#7B436A')
            person1_phone_entry.place(x=250, y=300)

            person1_mail = Label(win, text='PERSON 1 \n Email ID', bd=4, bg='#C685D6', fg='black')
            person1_mail.place(x=10, y=350)

            person1_mail_entry = Entry(win, bd=2, bg='#7B436A')
            person1_mail_entry.place(x=250, y=350)

            # PERSON 2 CREDENTIALS
            person2_phone = Label(win, text='PERSON 2 \n Phone number', bd=4, bg='#A03870', fg='black')
            person2_phone.place(x=10, y=400)

            person2_phone_entry = Entry(win, bd=2, bg='#AA5D83')
            person2_phone_entry.place(x=250, y=400)

            person2_mail = Label(win, text='PERSON 2 \n Email ID', bd=4, bg='#A03870', fg='black')
            person2_mail.place(x=10, y=450)

            person2_mail_entry = Entry(win, bd=2, bg='#AA5D83')
            person2_mail_entry.place(x=250, y=450)

            # PERSON 3 CREDENTIALS
            person3_phone = Label(win, text='PERSON 3 \n Phone number', bd=4, bg='#CDC2B7', fg='black')
            person3_phone.place(x=10, y=500)

            person3_phone_entry = Entry(win, bd=2, bg='#B8A899')
            person3_phone_entry.place(x=250, y=500)

            person3_mail = Label(win, text='PERSON 3 \n Email ID', bd=4, bg='#CDC2B7', fg='black')
            person3_mail.place(x=10, y=550)

            person3_mail_entry = Entry(win, bd=2, bg='#B8A899')
            person3_mail_entry.place(x=250, y=550)

            def submit():
                messagebox.askquestion("Confirmation", "Can the details be finalized ?")

                data = cursorr.fetchall()

                pn = entry1.get()
                global found, infolist
                found = False

                for row in data:
                    if row[0] == pn:
                        found = True
                        global infolist
                        infolist = list(row)
                        break
                if found == True:
                    messagebox.showinfo('You already Have a account in Securez')
                    file = open('userlog.txt', 'w+')
                    file.writelines(infolist)
                    file.close()
                    table.close()
                else:

                    userPhoneNumber = pn
                    print(userPhoneNumber)
                    try:
                        a = int(userPhoneNumber)
                    except:
                        messagebox.showwarning("Warning", "Check your phone number")
                        return None
                    if len(userPhoneNumber) != 10:
                        messagebox.showwarning("Warning", "Check your phone number")
                        return None
                    userName = entry2.get()
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
                    DBsubmission = "INSERT INTO users ( userphonenumber, username, phonenumber1 , phonenumber2, phonenumber3, email1, email2, email3)\
                                VALUES({},'{}',{},{},{},'{}','{}','{}')".format(userPhoneNumber, userName, person1Phone,
                                                                                person2Phone,
                                                                                person3Phone, person1Mail, person2Mail,
                                                                                person3Mail)
                    cursorr.execute(DBsubmission)
                    table.commit()
                    table.close()
                    infolist = [str(userPhoneNumber) + '\n', userName + '\n', str(person1Phone) + '\n',
                                str(person2Phone) + '\n', str(person3Phone) + '\n', person1Mail + '\n', person2Mail + '\n',
                                person3Mail + '\n']
                    file = open('userlog.txt', 'w+')
                    file.writelines(infolist)
                    file.close()
                    messagebox.showinfo("SUCCESS", "Your data is added successfully")
                    closebutton_isactivated = True
                    win.destroy()

            submitButton = Button(win, text="Submit", bd=5, command=submit)
            submitButton.place(x=200, y=620)





        def loginbuttonclick():
            userpn = entry1.get()
            try:
                a = int(userpn)
            except:
                messagebox.showwarning("Warning", "Check your phone number")
                return None
            if len(userpn) != 10:
                messagebox.showwarning("Warning", "Check your phone number")
                return None

            data = cursorr.fetchall()

            pn = entry1.get()
            print(pn)
            global found, infolist
            found = False

            for row in data:
                if row[0] == pn:
                    found = True
                    global infolist
                    infolist = list(row)
                    break
            if found == True:
                file = open('userlog.txt', 'w+')
                file.writelines(infolist)
                file.close()
                table.close()

            else:
                signupbutton()
        def closebutton():
            sys.exit()









        loginButton = Button(win, text="Submit", bd=5, command=loginbuttonclick)
        loginButton.place(x=200, y=200)

        signupButton = Button(win, text="Sign Up", bd=5, command=signupbutton)
        signupButton.place(x=400, y=200)

        closeButton = Button(win, text="Cancel", bd=5, command=closebutton)
        closeButton.place(x=100, y=200)



        win.mainloop()








#table name = users
#db name = securez