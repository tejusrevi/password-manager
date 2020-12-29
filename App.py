from tkinter import *
from PIL import Image, ImageTk
from DTOs.User import User
from DTOs.Password import Password
import base64, pickle, webbrowser
from CaesarCipher import encrypt

users = []
try:
  with open("data.pkl", "rb") as input_file:
    users = pickle.load(input_file)
except FileNotFoundError:
  pass

def handleGoToRegister():
  loginForm.pack_forget()
  getRegisterForm()
  registerForm.pack()

def handleGoToLogin():
  registerForm.pack_forget()
  getLoginForm()
  loginForm.pack()

def handleLogin(username, password):
  for user in users:
    if user.getUsername() == username.get():
      if user.getMasterPassword() == password.get():
        loginScreen.pack_forget()
        getDashboard(user)
        dashboard.pack()

def registerUser(username, password):
  users.append(User(username, password))
  with open('data.pkl', 'wb') as output:
    pickle.dump(users, output, pickle.HIGHEST_PROTOCOL)

def handleLogout():
  root.quit()

def handleRegisterButton(username, password, confirmPassword, errorLabel):
  userExists = False
  for user in users:
    if user.getUsername() == username.get():
      userExists = True
  if userExists:
    errorLabel.config(text="Sorry. That username is taken")
  else:
    if password.get() == confirmPassword.get():
      registerUser(username.get(), password.get())
      errorLabel.config(text="")
      handleGoToLogin()
    else:
      errorLabel.config(text="Passwords don't match")

def getLoginForm():
  Label(loginForm, bg='#32425B', fg='white', font=('Roboto',14), text="LOGIN", borderwidth=0).place(relx=0.5, rely=0.2, anchor=CENTER)
  nameLabel = Label(loginForm, bg='#32425B', fg='white', font=('Roboto',8), text="USERNAME", borderwidth=0)
  nameLabel.place(relx=0.1, rely=0.3, anchor=W)
  nameEntry = Entry(loginForm, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
  nameEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
  passwordLabel = Label(loginForm, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
  passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
  passwordEntry = Entry(loginForm, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',24), relief=FLAT)
  passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)

  loginButton = Button(loginForm, text = "LOGIN", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command = lambda: handleLogin(username=nameEntry, password=passwordEntry))
  loginButton.place(relx=0.1, rely=0.62, anchor=W, width=300, height=25)
  registerButton = Button(loginForm, text = "OR REGISTER TODAY", anchor = W, bg="#415575", fg="white", bd=0, padx=95, command = lambda: handleGoToRegister())
  registerButton.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)

def getRegisterForm():
  Label(registerForm, bg='#32425B', fg='white', font=('Roboto',14), text="REGISTER", borderwidth=0).place(relx=0.5, rely=0.2, anchor=CENTER)
  nameLabel = Label(registerForm, bg='#32425B', fg='white', font=('Roboto',8), text="USERNAME", borderwidth=0)
  nameLabel.place(relx=0.1, rely=0.3, anchor=W)
  nameEntry = Entry(registerForm, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
  nameEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
  passwordLabel = Label(registerForm, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
  passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
  passwordEntry = Entry(registerForm, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',24), relief=FLAT)
  passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)
  confirmPasswordLabel = Label(registerForm, bg='#32425B', fg='white', font=('Roboto',8), text="CONFIRM PASSWORD", borderwidth=0)
  confirmPasswordLabel.place(relx=0.1, rely=0.55, anchor=W)
  confirmPasswordEntry = Entry(registerForm, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',24), relief=FLAT)
  confirmPasswordEntry.place(relx=0.1, rely=0.6, anchor=W, width=300, height=25)

  errorLabel = Label(registerForm, bg='#32425B', fg='red', font=('Roboto',8), borderwidth=0)
  errorLabel.place(relx=0.1, rely=0.65, anchor=W)

  registerButton = Button(registerForm, text = "REGISTER", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=125, command = lambda: handleRegisterButton(nameEntry, passwordEntry, confirmPasswordEntry, errorLabel))
  registerButton.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)
  loginButton = Button(registerForm, text = "LOGIN INSTEAD", anchor = W, bg="#415575", fg="white", bd=0, padx=105, highlightbackground='red', command = lambda: handleGoToLogin())
  loginButton.place(relx=0.1, rely=0.78, anchor=W, width=300, height=25)

def handleRadioButton(var, parent):
  for child in parent.winfo_children():
    child.destroy()
  if var.get() == 1:
    getPasswords(parent)
  elif var.get() == 2:
    getCreditCards(parent)
  elif var.get() == 3:
    getNotes(parent)


def getDashboard(user):
  profileMenu = Frame(dashboard, bg='#3a4d6b', width = 800, height=450)
  profileMenu.place(relx=0.12, rely=0.5, anchor=CENTER, width=200, height=450)
  utility = Frame(dashboard, bg='#32425B', width = 600, height=450)

  Label(profileMenu, bg='#3a4d6b', fg='white', font=('Roboto',8), text="Welcome", borderwidth=0).pack( anchor = W , pady=1, padx=10)
  Label(profileMenu, bg='#3a4d6b', fg='white', font=('Roboto',12), text='Tejus', borderwidth=0).pack( anchor = W , pady=1, padx=10)

  var = IntVar()
  R1 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#546f99', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Passwords", font=('Roboto',10), variable=var, value=1, command= lambda: handleRadioButton(var,utility))
  R1.pack( anchor = W , pady=1)
  R2 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#546f99', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Credit Cards", font=('Roboto',10), variable=var, value=2, command= lambda: handleRadioButton(var, utility))
  R2.pack( anchor = W, pady=1)
  R3 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#546f99', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Secure Notes", font=('Roboto',10), variable=var, value=3, command= lambda: handleRadioButton(var,utility))
  R3.pack( anchor = W, pady=1)

  logoutButton = Button(profileMenu, text = "LOGOUT", bg="#415575", fg="white", bd=0, highlightbackground='red', command = lambda: handleLogout())
  logoutButton.place(relx=0, rely=0.97, anchor=W, width=200, height=25)

  utility.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
  dashboard.pack() #remov

def getPasswords(window):
  Label(window, bg='#32425B', fg='white', font=('Roboto',14), text="Passwords", borderwidth=0).place(relx=0.05, rely=0.1, anchor=W)
  Button(window, bg='#198a78', fg='white', font=('Roboto',10), text="Add new", borderwidth=0).place(relx=0.95, rely=0.1, anchor=E)

def getCreditCards(window):
  Label(window, bg='#32425B', fg='white', font=('Roboto',14), text="Credit Cards", borderwidth=0).place(relx=0.05, rely=0.1, anchor=W)
  Button(window, bg='#198a78', fg='white', font=('Roboto',10), text="Add new", borderwidth=0).place(relx=0.95, rely=0.1, anchor=E)

def getNotes(window):
  Label(window, bg='#32425B', fg='white', font=('Roboto',14), text="Secure Notes", borderwidth=0).place(relx=0.05, rely=0.1, anchor=W)
  Button(window, bg='#198a78', fg='white', font=('Roboto',10), text="Add new", borderwidth=0).place(relx=0.95, rely=0.1, anchor=E)

if __name__ == '__main__':
  root = Tk()
  #root.resizable(False, False)
  root.title('Password Manager')
  root.configure(background='#32425B')
  root.geometry("800x450")
  '''
  loginScreen = Frame(root, bg='#32425B', width = 800, height=450)
  render = ImageTk.PhotoImage(Image.open('assets/images/bg.png'))

  leftDecoration = Label(loginScreen, image=render, borderwidth=0)
  form = Frame(loginScreen, bg='#32425B', width = 400, height=450)
  loginForm = Frame(form, bg='#32425B', width = 400, height=450)
  registerForm = Frame(form, bg='#32425B', width = 400, height=450)
  getLoginForm()

  credit = Label(form, bg='#32425B', fg='white', font=('Roboto',8), text="Made by Tejus Revi", borderwidth=0, cursor="hand2")
  credit.place(relx=0.5, rely=0.98, anchor=CENTER)
  credit.bind("<Button-1>",lambda e:webbrowser.open_new('https://tejus-dev.web.app/'))

  loginForm.pack()
  form.pack(side='right')
  leftDecoration.pack(side='left')
  loginScreen.pack()
  '''
  dashboard = Frame(root, bg='#32425B', width = 800, height=450)
  getDashboard()
  root.mainloop()