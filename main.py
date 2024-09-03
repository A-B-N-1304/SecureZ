
from tkinter import *
from menufunctions import *
from credentials import *
from dangerhandler import dangerhandler
from loginpage import *


login()

top = Tk(className='SECUREZ')
top.geometry('540x567')
top.resizable(0, 0)
#menuBar = Menu(top)
bgm = PhotoImage(file="main_bgm.png")
danger = PhotoImage(file='dangersign.png')
logo = PhotoImage(file='SECUREZ (5).png')
background = Label(top, compound=CENTER, image=bgm)
background.place(x=0, y=0, relwidth=1, relheight=1)
mb = Menubutton(top, text="YOUR DATA", relief=RAISED, )
logodisp = Label(top, image=logo, bd=0)
logodisp.place(x=0, y=10)

mb.place(x=0, y=0)
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu


mb.menu.add_command(label="Show saved data", command=show_saved_data)
mb.menu.add_command(label="Edit Saved data", command=editbutton)

db = Button(top, image=danger, width=300, height=300, bd=0, relief=RAISED, command=dangerhandler)
db.place(x=120, y=120)


mb.place(x=0, y=100)


#top.config(menu = mb)

top.mainloop()





