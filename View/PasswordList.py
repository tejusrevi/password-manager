from tkinter import *
from View.AddNewPassword import AddNewPassword
from PIL import Image, ImageTk

from View.PasswordTab import PasswordTab

class PasswordList:
  def __init__(self, passwords):
    self.passwords = passwords
  def createWindow(self, parent, handleSavePassword, copyPasswordToClipboard, handleEditPassword, deletePassword, getDecryptedPassword):
    for child in parent.winfo_children():
      child.destroy()
    h1 = Label(parent, bg='#32425B', fg='white', font=('Roboto',14), borderwidth=0, text="Passwords")
    h1.place(relx=0.1, rely=0.1, anchor=W)
    addNew = Button(parent, bg='#198a78', fg='white', font=('Roboto',10), text="Add new", borderwidth=0, command=lambda: self.handleAddNewPassword(parent, handleSavePassword))
    addNew.place(relx=0.95, rely=0.1, anchor=E)
    canvas = Canvas(parent, height=380, bg='#32425B', bd=0, highlightthickness=0, relief='ridge')
    scroll_y = Scrollbar(parent, orient="vertical", command=canvas.yview, bg='#32425B')

    listOfButtons = Frame(canvas, height=380, borderwidth=0, bg='#32425B')
    row = column = 0
    for password in self.passwords:
      card = Label(listOfButtons, borderwidth=0, bg='#32425B', width=100)
      if password.getLogo() == None:
        '''
        cardLogotk = ImageTk.PhotoImage(password.getLogo())
        cardLogo = Label(card, borderwidth=0, bg='#32425B', image=cardLogotk)
        cardLogo.image = cardLogotk
        cardButton = Button(card, text=password.getWebsite(), bg='#32425B', fg='white', borderwidth=0, compound=TOP, width=100, padx=20, pady=20, wraplength=100, command=lambda password=password: PasswordTab().createWindow(password))
        '''
        cardButton = Button(card, text=password.getWebsite(), bg='#32425B', fg='white', borderwidth=0, width=10, padx=20, pady=20, command=lambda password=password: PasswordTab(password).createWindow(parent, copyPasswordToClipboard, handleEditPassword, deletePassword, getDecryptedPassword))
      else:
        cardLogotk = ImageTk.PhotoImage(password.getLogo().resize((50,50), Image.ANTIALIAS))
        cardLogo = Label(card, borderwidth=0, bg='#32425B', image=cardLogotk)
        cardLogo.image = cardLogotk
        cardButton = Button(card, text=password.getWebsite(), bg='#32425B', fg='white', borderwidth=0, image =cardLogotk, compound=TOP, width=100, padx=20, pady=20, wraplength=100, command=lambda password=password: PasswordTab(password).createWindow(parent, copyPasswordToClipboard, handleEditPassword, deletePassword, getDecryptedPassword))
      cardButton.pack()
      card.grid(row=int(row), column=column%4)
      row=row+0.25
      column=column+1
    canvas.create_window(0, 0, anchor='nw', window=listOfButtons)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                    
    canvas.place(relx=0, rely=1, anchor=SW, width=600)
    scroll_y.place(relx=1, rely=1, anchor=SE, height=380)

  def handleAddNewPassword(self, parent, handleSavePassword):
    AddNewPassword().createWindow(parent, handleSavePassword)
  def handleAddNewCreditCard(self, h1, addNew):
    h1.configure(text="Add New Password")
    addNew.destroy()
  def handleAddNewNote(self, h1, addNew):
    h1.configure(text="Add New Password")
    addNew.destroy()