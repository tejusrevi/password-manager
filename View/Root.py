from tkinter import *
from PIL import Image, ImageTk
import webbrowser

from Controller.UserController import UserController

from View.LoginForm import LoginForm
from View.RegisterForm import RegisterForm
from View.Dashboard import Dashboard

class Root:
  root = Tk()
  loginScreen = Frame(root, bg='#32425B', width = 800, height=450)
  form = Frame(loginScreen, bg='#32425B', width = 400, height=450)
  loginForm = Frame(form, bg='#32425B', width = 400, height=450)
  registerForm = Frame(form, bg='#32425B', width = 400, height=450)
  dashboard = Frame(root, bg='#32425B', width = 800, height=450)
  userController = UserController()

  def __init__(self):
    pass
  def createWindow(self):
    Root.root.resizable(False, False)
    Root.root.iconbitmap('assets/images/logo.ico')
    Root.root.title('Password Manager')
    Root.root.configure(background='#32425B')
    Root.root.geometry("800x450")

    render = ImageTk.PhotoImage(Image.open('assets/images/bg.png'))
    leftDecoration = Label(Root.loginScreen, image=render, borderwidth=0)
    leftDecoration.image = render

    LoginForm().createWindow(Root.loginForm, self.handleLogin, self.handleGoToRegister)

    credit = Label(Root.form, bg='#32425B', fg='white', font=('Roboto',8), text="Made by Tejus Revi", borderwidth=0, cursor="hand2")
    credit.place(relx=0.5, rely=0.98, anchor=CENTER)
    credit.bind("<Button-1>",lambda e:webbrowser.open_new('https://tejus-dev.web.app/'))

    Root.loginForm.pack()
    Root.form.pack(side='right')
    leftDecoration.pack(side='left')
    Root.loginScreen.pack()
    return Root.root

  def handleRegisterButton(self, username, password, confirmPassword, errorLabel):
    if username.get() == '' or password.get() == '':
      errorLabel.config(text="Username and password are required")
    else:
      if not Root.userController.isUsernameAvailable(username.get()):
        errorLabel.config(text="Sorry. That username is taken")
      else:
        if password.get() == confirmPassword.get():
          Root.userController.createUser(username.get(), password.get())
          self.handleGoToLogin()
        else:
          errorLabel.config(text="Passwords don't match")

  def handleLogin(self,username, password, errorLabel):
    if Root.userController.authenticateUser(username.get(), password.get()):
      Root.loginScreen.pack_forget()
      Dashboard(Root.userController).createWindow(Root.dashboard, self.handleLogout)
      Root.dashboard.pack()
    else:
      errorLabel.config(text="Incorrect credentials")

  def handleGoToRegister(self):
    Root.loginForm.pack_forget()
    RegisterForm().createWindow(Root.registerForm, self.handleRegisterButton, self.handleGoToLogin)
    Root.registerForm.pack()

  def handleGoToLogin(self):
    Root.registerForm.pack_forget()
    LoginForm().createWindow(Root.loginForm, self.handleLogin, self.handleGoToRegister)
    Root.loginForm.pack()

  def handleLogout(self):
    Root.root.quit()

