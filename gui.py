import tkinter as tk
import threading
from tkinter import ttk
from tkinter import *
from numpy.lib.polynomial import roots

from pandas.core.frame import DataFrame
from functionalities import Scraper
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

from pandastable import Table, TableModel

from PIL import ImageTk, Image



table_view_window = tk.Tk()

# Here we are adjusting the size of the window
table_view_window.geometry("1000x1000")

# Add image file
bg = ImageTk.PhotoImage(Image.open("Backgrounds.png"))

# Show image using label
label1 = Label(table_view_window, image=bg)
label1.place(x=1, y=1)

# Create Frame
frame1 = Frame(table_view_window
              
               )
frame1.pack(pady=20)   
# frame1.place(x=250,y=70)  #place function also does the same work as pack function does but pady is more convienent 


class functions:
    def submit(self):

        catname = category.get()        #gets the category from strvar
        pages = page.get()
        print(type(pages))
        print("The name of Product is : " + catname)
        
        self.k = Scraper().dataframe_and_scrap(catname, pages)
    
        self.Take_input(self.k)
        # these two lines below are of no use dont knoow why these are here
        arr.append(self.k)
        category.set("")

    def Take_input(self, k):
        print(k)
        # Output.insert(END,k)
        self.table = pt = Table(frame1, dataframe=k,
                                showtoolbar=True, showstatusbar=True, )
        pt.show()

arr = []

#below is used to show text on the frame
# Output = Text(frame1, height = 20,
#              width = 120,
#              bg = "light yellow")
# Output.grid(column=0,row=2000,columnspan=7,rowspan=10)


ttk.Label(frame1, text="Scrape Sonic",
          background='light blue', foreground="black",
          font=("Arial", 21)).grid(row=0, column=1)

ttk.Label(frame1, text="Select the Product :",
          font=("Arial", 12)).grid(column=0,
                                             row=5, padx=10, pady=25, columnspan=1)


ttk.Label(frame1, text="Pages :",
          font=("Arial", 12)).grid(column=2,
                                             row=5, padx=10, pady=25, columnspan=1)

#category  Combobox creation
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
pagechoosen['values'] = (1, 2, 3, 4, 5)

pagechoosen.grid(column=3, row=5)
pagechoosen.current()

submit_button = Button(frame1, text='Submit',
             command=functions().submit).grid(column=4, row=5)

table_view_window.title("Scrape Sonic")

table_view_window.wm_minsize(600, 500)
table_view_window.resizable(200, 200)
table_view_window.wm_maxsize(1000, 600)
table_view_window.mainloop()
