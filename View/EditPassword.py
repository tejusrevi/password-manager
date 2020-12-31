from tkinter import *
from PIL import Image, ImageTk

class EditPassword:
  def __init__(self, password):
    self.password = password
  def createWindow(self, parent, editPassword, getDecryptedPassword):
    for child in parent.winfo_children():
      child.destroy()
    h1 = Label(parent, bg='#32425B', fg='white', font=('Roboto',14), borderwidth=0, text='Edit credentials for '+self.password.getWebsite())
    h1.place(relx=0.1, rely=0.1, anchor=W)

    if self.password.getLogo()!= None:
      logotk = ImageTk.PhotoImage(self.password.getLogo())
      logoLabel = Label(parent, borderwidth=0, bg='#32425B', image=logotk)
      logoLabel.image = logotk
      logoLabel.place(relx=0.9, rely=0.5, anchor=E, width=100, height=100)

    loginLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="LOGIN ID", borderwidth=0)
    loginLabel.place(relx=0.1, rely=0.3, anchor=W)
    loginEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    loginEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
    loginEntry.insert(0, self.password.getLogin())

    passwordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
    passwordLabel.place(relx=0.1, rely=0.4, anchor=W)
    passwordEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    passwordEntry.place(relx=0.1, rely=0.45, anchor=W, width=300, height=25)
    passwordEntry.insert(0, getDecryptedPassword(self.password))

    passwordStrengthLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD STRENGTH: ", borderwidth=0)
    passwordStrengthLabel.place(relx=0.1, rely=0.5, anchor=W)

    notesLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="NOTES", borderwidth=0)
    notesLabel.place(relx=0.1, rely=0.6, anchor=W)
    notesEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    notesEntry.place(relx=0.1, rely=0.65, anchor=W, width=300, height=25)
    notesEntry.insert(0, self.password.getNote())

    saveButton = Button(parent, text = "SAVE", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command= lambda: editPassword(parent, self.password, loginEntry, passwordEntry, notesEntry, self.password.getLogo()))
    saveButton.place(relx=0.1, rely=0.75, anchor=W, width=300, height=25)