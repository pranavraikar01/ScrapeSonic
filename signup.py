import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import mysql.connector

def clear():
    Input_loginid.delete(0,END)
    Input_password.delete(0,END)
    Inputname.delete(0,END)
    Inputemail.delete(0,END)
    

# create connection

def input():
    if not validate_email():
        return
    
    if Input_loginid.get()=='' or Input_password.get()==''or Inputname.get() == '' or Inputemail.get() == '':
        messagebox.showerror('Error','All fields are Required')
    else:
        try:
            db = mysql.connector.connect(host="localhost",user="root",password="Pranav@01",database="scrapelogin")
            mycursor = db.cursor()

        except:
            messagebox.showerror('Error', 'Database not connected')
            return
        try:
            query = 'create database scrapelogin'
            mycursor.execute(query)
            query = 'use scrapelogin'
            mycursor.execute(query)
            query = 'create table scrapeuser(loginid varchar(255) primary key not null, password varchar(255) not null, name varchar(255) not null, email varchar(255) not null )'
            mycursor.execute(query)

        except:
            mycursor.execute('use scrapelogin')
            query = 'select * from scrapeuser where loginid =%s'
            

            row = mycursor.fetchone()
            if row !=None:
                messagebox.showerror('Error', 'Loginid already exists')
            
            else:
                query = "INSERT INTO scrapeuser (loginid, password, name, email) VALUES (%s, %s,%s,%s)"
                mycursor.execute(query, (Input_loginid.get(), Input_password.get(), Inputname.get(), Inputemail.get()))
                db.commit()
                db.close()
                messagebox.showinfo('Success', 'Registration is Successful')
                clear()
                login_window.destroy()
                import signin
    
def gui_page():

    login_window.destroy()
    import signin

login_window = tk.Tk()

# Here we are adjusting the size of the window
login_window.geometry("1000x1000")
bg = ImageTk.PhotoImage(Image.open("Backgrounds1.png"))


# Show image using label
label1 = Label(login_window, image=bg)
label1.place(x=1, y=1)

#validating email
def validate_email():
    email = Inputemail.get()
    if email.endswith("@gmail.com"):
        return True
    else :
        messagebox.showerror("Error","Email must be in format of 'Example@gmail.com")
        clear()


# Create Frame
frame1 = Frame(login_window,relief='sunken')
frame1.pack(pady=150) 


loginidlabel=Label(frame1, text="Login id",
          font=("Arial", 12)).grid(column=0,
                                             row=15, padx=20, pady=20)

Input_loginid = Entry(frame1,
             width = 35,
             )
Input_loginid.grid(column=1,row=15,padx=40)



Passwordlabel=Label(frame1, text="Password",
          font=("Arial", 12)).grid(column=0,
                                             row=17, padx=20, pady=20)

Input_password = Entry(frame1,
             width = 35,
             )
Input_password.grid(column=1,row=17,padx=40)



emailLabel=Label(frame1,text='Email',font=('Microsoft Yahei UI Light',10,'bold'))
emailLabel.grid(row=35,column=0,padx=25,)

Inputemail= Entry(frame1,
             width = 35
             )
Inputemail.grid(row=35,column=1,padx=25,pady=20)



namelabel=Label(frame1,text='Name',font=('Microsoft Yahei UI Light',10,'bold'))
namelabel.grid(row=45,column=0,padx=25)

Inputname= Entry(frame1, 
             width = 35,
             )
Inputname.grid(row=45,column=1,padx=25,pady=20)





login_button = Button(frame1, text='Login',
             command=input).grid(column=1, row=50,pady=0,padx=40)

login_window.title("Scrape Sonic")


login_window.wm_minsize(600, 500)
login_window.resizable(200, 200)
login_window.wm_maxsize(1000, 600)
login_window.mainloop()