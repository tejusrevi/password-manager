from tkinter import Label, Button
from tkinter.constants import *

from PIL import Image, ImageTk

class SinglePassword:
  def __init__(self, password):
    self.password = password
  def createWindow(self, parent, copyPasswordToClipboard, handleEditPassword, deletePassword, getDecryptedPassword):
    for child in parent.winfo_children():
      child.destroy()
    Label(parent, bg='#32425B', fg='white', font=('Roboto',16), text="Password for "+self.password.getWebsite(), borderwidth=0).place(relx=0.1, rely=0.2, anchor=W)
    Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="LOGIN ID", borderwidth=0).place(relx=0.1, rely=0.3, anchor=W)
    Label(parent, bg='#32425B', fg='white', font=('Roboto',12), text=self.password.getLogin(), borderwidth=0).place(relx=0.1, rely=0.35, anchor=W)
    Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0).place(relx=0.1, rely=0.425, anchor=W)
    Label(parent, bg='#32425B', fg='white', font=('Roboto',12), text=getDecryptedPassword(self.password), borderwidth=0).place(relx=0.1, rely=0.475, anchor=W)
    Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="NOTES", borderwidth=0).place(relx=0.1, rely=0.55, anchor=W)
    Label(parent, bg='#32425B', fg='white', font=('Roboto',12), text=self.password.getNote(), borderwidth=0).place(relx=0.1, rely=0.6, anchor=W)
    
    copyPassword = Button(parent, text = "COPY PASSWORD TO CLIPBOARD", bg='#3a4d6b', fg="white", bd=0, command= lambda: copyPasswordToClipboard(self.password))
    copyPassword.place(relx=0.1, rely=0.7, anchor=W, width=330, height=25)

    editPassword = Button(parent, text = "EDIT", bg="#1ED5B9", fg="white", bd=0, command= lambda: handleEditPassword(parent, self.password))
    editPassword.place(relx=0.1, rely=0.8, anchor=W, width=150, height=25)

    deleteButton = Button(parent, text = "DELETE", bg="#BF4342", fg="white", bd=0, command= lambda: deletePassword(parent, self.password))
    deleteButton.place(relx=0.4, rely=0.8, anchor=W, width=150, height=25)
    if self.password.getLogo() != None:
      cardLogotk = ImageTk.PhotoImage(self.password.getLogo())
      cardLogo = Label(parent, borderwidth=0, bg='#32425B', image=cardLogotk)
      cardLogo.image = cardLogotk
      cardLogo.place(relx=0.9, rely=0.5, anchor=E, width=100, height=100)
  
