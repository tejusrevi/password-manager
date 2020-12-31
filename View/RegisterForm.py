from tkinter import *

class RegisterForm():
  def __init__(self):
    pass
  def createWindow(self, parent, handleRegisterButton, handleGoToLogin):
    Label(parent, bg='#32425B', fg='white', font=('Roboto',14), text="REGISTER", borderwidth=0).place(relx=0.5, rely=0.2, anchor=CENTER)
    nameLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="USERNAME", borderwidth=0)
    nameLabel.place(relx=0.1, rely=0.3, anchor=W)
    nameEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    nameEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
    passwordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
    passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
    passwordEntry = Entry(parent, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',24), relief=FLAT)
    passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)
    confirmPasswordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="CONFIRM PASSWORD", borderwidth=0)
    confirmPasswordLabel.place(relx=0.1, rely=0.55, anchor=W)
    confirmPasswordEntry = Entry(parent, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',24), relief=FLAT)
    confirmPasswordEntry.place(relx=0.1, rely=0.6, anchor=W, width=300, height=25)
    errorLabel = Label(parent, bg='#32425B', fg='red', font=('Roboto',8), borderwidth=0)
    errorLabel.place(relx=0.1, rely=0.65, anchor=W)
    registerButton = Button(parent, text = "REGISTER", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=125, command = lambda: handleRegisterButton(nameEntry, passwordEntry, confirmPasswordEntry, errorLabel))
    registerButton.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)
    loginButton = Button(parent, text = "LOGIN INSTEAD", anchor = W, bg="#415575", fg="white", bd=0, padx=105, highlightbackground='red', command = lambda: handleGoToLogin())
    loginButton.place(relx=0.1, rely=0.78, anchor=W, width=300, height=25)
