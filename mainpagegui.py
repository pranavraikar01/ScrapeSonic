import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


def description():
    mainpage_view_window.destroy()
    import overviewgui


def tabulardata():
    mainpage_view_window.destroy()
    import tabulardatagui

def back_to_signin():
    mainpage_view_window.destroy()
    import signin


mainpage_view_window = tk.Tk()
mainpage_view_window.geometry("1020x1000")
# Add image file
bg = ImageTk.PhotoImage(Image.open("Backgrounds.png"))

bg1 = ImageTk.PhotoImage(Image.open("DESCRIPTION.png"))

bg2 = ImageTk.PhotoImage(Image.open("TABULARDATA.png"))
bg3 = ImageTk.PhotoImage(Image.open("back.png"))
mainpage_view_window.title("Scrape Sonic")

# Show image using label
label1 = Label(mainpage_view_window, image=bg)
label1.place(x=1, y=1)

# Create Frame
frame1 = Frame(mainpage_view_window

               )
frame1.pack(pady=40)


description = Button(mainpage_view_window, text='Description',
                     width=15, command=description, image=bg1)


description.place(x=180, y=350)

tabulardata = Button(mainpage_view_window, text='tabulardata',
                     width=15, command=tabulardata, image=bg2)
tabulardata.place(x=550, y=350)

backtosignin = Button(mainpage_view_window, text='back',
                     width=15, command=back_to_signin,image=bg3)
backtosignin.place(x=900, y=550)

mainpage_view_window.wm_minsize(600, 500)
mainpage_view_window.resizable(200, 200)
mainpage_view_window.wm_maxsize(1000, 600)
mainpage_view_window.mainloop()
