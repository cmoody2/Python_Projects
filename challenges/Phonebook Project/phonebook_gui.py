from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import phonebook_main
import phonebook_func

def load_gui(self):

    self.lbl_fname = tk.Label(self.master, text='First Name: ')
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text='Last Name: ')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master, text='Phone Number: ')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text='Email Address: ')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady(10,0), sticky=N+W)
    self.lbl_user = tk.Label(self.master, text='User: ')
    self.lbl_user.grid(row=0, column=2, padx=(0,0), pady(10,0), sticky=N+W)

    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

    # Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    
    
    
