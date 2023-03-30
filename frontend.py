import tkinter as tk
import threading
from tkinter import ttk
from tkinter import *
from numpy.lib.polynomial import roots

from pandas.core.frame import DataFrame
from backend import Scraper
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

from pandastable import Table, TableModel

from PIL import ImageTk, Image



root = tk.Tk()

# Adjust size
root.geometry("1000x1000")

# Add image file
bg = ImageTk.PhotoImage(Image.open("Backgrounds_Triangles.png"))

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=1, y=1)

# Create Frame
frame1 = Frame(root
              # , style='My.TFrame'
               )
frame1.pack(pady=20)   
# frame1.place(x=250,y=70)  #place function also does the same work as pack function does but pady is more convienent 


class functions1:
    def submit(self):

        catname = n.get()
        pages = n3.get()
        print(type(pages))
        print("The name of Product is : " + catname)
        # t1 = threading.Thread(target=functions1().Bar(pages))
        # # t2 = threading.Thread(target=Scraper().dataframe_and_scrap(catname,pages))
        # t1.start()
        self.k = Scraper().dataframe_and_scrap(catname, pages)
        # self.k = t2.start()
        # t1.join()
        # t2.join()
        self.Take_input(self.k)
        # these two lines below are of no use dont knoow why these are here
        arr.append(self.k)
        n.set("")

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

# 1 st Combobox creation
n = tk.StringVar()
categorychoosen = ttk.Combobox(frame1, width=27, textvariable=n)

# Adding combobox drop down list
categorychoosen['values'] = (' Skin Cream',
                             ' Perfume',
                             ' Skin Talc',
                             ' Soap',
                             'Books')

categorychoosen.grid(column=1, row=5)
categorychoosen.current()


# 3 st Combobox creation
n3 = tk.IntVar()
pagechoosen = ttk.Combobox(frame1, width=7, textvariable=n3)

# Adding combobox drop down list
pagechoosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

pagechoosen.grid(column=3, row=5)
pagechoosen.current()

btn = Button(frame1, text='Submit',
             command=functions1().submit).grid(column=4, row=5)

root.title("Scrape Sonic")
# root.iconbitmap("flipkart_icon-icons.com_62718.ico")
root.wm_minsize(600, 500)
root.resizable(200, 200)
root.wm_maxsize(1000, 600)
root.mainloop()
