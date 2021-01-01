from tkinter import Label, Entry, Button, Frame, StringVar
from tkinter.constants import *

import requests
from io import BytesIO
from PIL import Image, ImageTk

from Controller.PasswordStrength import calculatePasswordStrength
class AddNewPasswordForm:
  logo = None
  def __init__(self):
    self.websiteSV = StringVar()
    self.passwordSV = StringVar()
  def createWindow(self, parent, handleSavePassword):
    for child in parent.winfo_children():
      child.destroy()
    h1 = Label(parent, bg='#32425B', fg='white', font=('Roboto',14), borderwidth=0, text='Add New Password')
    h1.place(relx=0.1, rely=0.1, anchor=W)

    websiteLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="WEBSITE", borderwidth=0)
    websiteLabel.place(relx=0.1, rely=0.2, anchor=W)

    logoLabel = Label(parent, borderwidth=0, bg='#32425B')
    passwordStrengthFrame = Frame(parent, width = 0, height=10)

    self.websiteSV.trace("w", lambda name, index, mode, sv=self.websiteSV: self.websiteCallback(self.websiteSV, logoLabel))
    self.passwordSV.trace("w", lambda name, index, mode, sv=self.passwordSV: self.passwordCallback(self.passwordSV, passwordStrengthFrame))

    websiteEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT, textvariable=self.websiteSV)
    websiteEntry.place(relx=0.1, rely=0.25, anchor=W, width=300, height=25)

    loginLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="LOGIN ID", borderwidth=0)
    loginLabel.place(relx=0.1, rely=0.35, anchor=W)
    loginEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    loginEntry.place(relx=0.1, rely=0.4, anchor=W, width=300, height=25)
    passwordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
    passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
    passwordEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT, textvariable=self.passwordSV)
    passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)

    passwordStrengthFrame.place(relx=0.1, rely=0.58, anchor=W)

    notesLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="NOTES", borderwidth=0)
    notesLabel.place(relx=0.1, rely=0.65, anchor=W)
    notesEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    notesEntry.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)

    logoLabel.place(relx=0.9, rely=0.5, anchor=E, width=100, height=100)
    saveButton = Button(parent, text = "SAVE", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command= lambda: handleSavePassword(parent, websiteEntry, loginEntry, passwordEntry, notesEntry, AddNewPasswordForm.logo))
    saveButton.place(relx=0.1, rely=0.8, anchor=W, width=300, height=25)

    #PasswordList().createWindow(parent)
  def websiteCallback(self, sv, logoLabel):
    url = 'http://logo.clearbit.com/{}?size=80'.format(sv.get())
    response = requests.get(url)
    if(response.status_code == 200):
      logo = Image.open(BytesIO(response.content)).resize((100,100), Image.ANTIALIAS)
      logotk = ImageTk.PhotoImage(logo)
      logoLabel.configure(image = logotk)
      logoLabel.image = logotk
      AddNewPasswordForm.logo = logo

  def passwordCallback(self, sv, passwordStrengthFrame):
    if calculatePasswordStrength(sv.get()) == 0:
      passwordStrengthFrame.configure(width=60, bg='#FF2C00')
    elif calculatePasswordStrength(sv.get()) == 1:
      passwordStrengthFrame.configure(width=120, bg='#FF6700')
    elif calculatePasswordStrength(sv.get()) == 2:
      passwordStrengthFrame.configure(width=180, bg='#FFA400')
    elif calculatePasswordStrength(sv.get()) == 3:
      passwordStrengthFrame.configure(width=240, bg='#D0C400')
    elif calculatePasswordStrength(sv.get()) == 4:
      passwordStrengthFrame.configure(width=300, bg='#7ADC05')
  
  
  