from tkinter import *
from screens.Root import Root
class LoginForm():
  def __init__(self):
    pass
  def createWindow(self, parent):
    Label(parent, bg='#32425B', fg='white', font=('Roboto',14), text="LOGIN", borderwidth=0).place(relx=0.5, rely=0.2, anchor=CENTER)
    nameLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="USERNAME", borderwidth=0)
    nameLabel.place(relx=0.1, rely=0.3, anchor=W)
    nameEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    nameEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
    passwordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
    passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
    passwordEntry = Entry(parent, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',24), relief=FLAT)
    passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)

    loginButton = Button(parent, text = "LOGIN", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command = lambda: super.handleLogin(username=nameEntry, password=passwordEntry))
    loginButton.place(relx=0.1, rely=0.62, anchor=W, width=300, height=25)
    registerButton = Button(parent, text = "OR REGISTER TODAY", anchor = W, bg="#415575", fg="white", bd=0, padx=95, command = lambda: super.handleGoToRegister())
    registerButton.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)
  
  