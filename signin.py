import tkinter as tk

from tkinter import ttk
from tkinter import *
from tkinter import messagebox


from pandas.core.frame import DataFrame
from functionalities import Scraper
from tkinter.ttk import *


from pandastable import Table, TableModel

from PIL import ImageTk, Image


def gui_page():
    if Input_loginid.get()=="" or Input_password.get()=="":
        messagebox.showerror('Error','All fields are required') 
    else:




        
        pass #hey pass kadhun taak ithe dbms cha code yenar ahe
        login_window.destroy()
        import gui

login_window = tk.Tk()

# Here we are adjusting the size of the window
login_window.geometry("1000x1000")
bg = ImageTk.PhotoImage(Image.open("Backgrounds.png"))

# Show image using label
label1 = Label(login_window, image=bg)
label1.place(x=1, y=1)


# Create Frame
frame1 = Frame(login_window)
frame1.pack(pady=100) 


titlelabel=Label(frame1, text="Scrape Sonic",
          background='light blue', foreground="black",
          font=("Arial", 15)).place(x=180,y=10)

loginidlabel=Label(frame1, text="Login id",
          font=("Arial", 12)).grid(column=0,
                                             row=15, padx=20, pady=55)

Input_loginid = Entry(frame1, 
             width = 35,
             )
Input_loginid.grid(column=1,row=15,padx=40,pady=45)




Passwordlabel=Label(frame1, text="Password",
          font=("Arial", 12)).grid(column=0,
                                             row=25, padx=20, pady=45)
Input_password = Entry(frame1, 
             width = 35,
            )
Input_password.grid(column=1,row=25,padx=40)

login_button = Button(frame1, text='Login',
             command=gui_page).grid(column=1, row=35,pady=10,padx=40)
login_window.title("Scrape Sonic")

login_window.wm_minsize(600, 500)
login_window.resizable(200, 200)
login_window.wm_maxsize(1000, 600)
login_window.mainloop()
