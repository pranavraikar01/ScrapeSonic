import tkinter as tk
from tkinter import ttk
from tkinter import *
from overview import Scraper1
from tkinter.ttk import *
from PIL import ImageTk, Image

description_view_window = tk.Tk()

# Here we are adjusting the size of the window
description_view_window.geometry("1000x1000")

# Add image file
bg = ImageTk.PhotoImage(Image.open("Backgrounds2.jpg"))

# Show image using label
label1 = Label(description_view_window, image=bg)
label1.place(x=1, y=1)

# Create Frame
frame1 = Frame(description_view_window

               )
frame1.pack(pady=40)
# frame1.place(x=250,y=70)  #place function also does the same work as pack function does but pady is more convienent

def back_to_mainpage():
    description_view_window.destroy()
    import mainpagegui

class functions:

    

    def submit(self):

        catname = category.get()  # gets the category from strvar
        pages = page.get()
        print(type(pages))
        print("The name of Product is : " + catname)

        self.k = Scraper1().flipkart_scraper(catname, pages)  # k is a list

        self.Take_input(self.k)
        category.set("")  # sets the category again to blank

    def Take_input(self, k):
        print(k)
        Output.insert(END, k)


arr = []

bg3 = ImageTk.PhotoImage(Image.open("back.png"))
# below is used to show text on the frame
Output = Text(frame1, height=20,
              width=120,
              bg="light yellow")
Output.grid(column=0, row=2000, columnspan=7, rowspan=10)


ttk.Label(frame1, text="Scrape Sonic",
          background='light blue', foreground="black",
          font=("Arial", 21)).grid(row=0, column=1)

ttk.Label(frame1, text="Enter the Product :",
          font=("Arial", 12)).grid(column=0,
                                   row=5, padx=10, pady=25, columnspan=1)


ttk.Label(frame1, text="Pages :",
          font=("Arial", 12)).grid(column=2,
                                   row=5, padx=10, pady=25, columnspan=1)


# category  Combobox creation
category = tk.StringVar()
categorychoosen = ttk.Combobox(frame1, width=27, textvariable=category)

# Adding combobox drop for choosing the category
categorychoosen['values'] = ('Books')

categorychoosen.grid(column=1, row=5)
categorychoosen.current()


# no.of pages Combobox creation
page = tk.IntVar()
pagechoosen = ttk.Combobox(frame1, width=7, textvariable=page)

# adding Combobox drop down for choosing the number of pages
pagechoosen['values'] = (1)

pagechoosen.grid(column=3, row=5)
pagechoosen.current()

submit_button = Button(frame1, text='Submit',
                       command=functions().submit).grid(column=4, row=5)

backtobacktomainpagesignin = Button(description_view_window, text='back',
                     width=15, command=back_to_mainpage,image=bg3)
backtobacktomainpagesignin.place(x=900, y=550)


# back = Button(description_view_window, text='Back',
#               width=15, command=functions.back)
# back.place(x=20, y=50)

description_view_window.title("Scrape Sonic")

description_view_window.wm_minsize(600, 500)
description_view_window.resizable(200, 200)
description_view_window.wm_maxsize(1000, 600)
description_view_window.mainloop()
