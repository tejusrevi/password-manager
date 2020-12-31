from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser, requests
from io import BytesIO
from Model.User import User
from Controller.UserController import UserController


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
    #root.resizable(False, False)
    Root.root.iconbitmap('assets/images/logo.ico')
    Root.root.title('Password Manager')
    Root.root.configure(background='#32425B')
    Root.root.geometry("800x450")
    render = ImageTk.PhotoImage(Image.open('assets/images/bg.png'))
    leftDecoration = Label(Root.loginScreen, image=render, borderwidth=0)
    leftDecoration.image = render
    LoginForm().createWindow(Root.loginForm)
    credit = Label(Root.form, bg='#32425B', fg='white', font=('Roboto',8), text="Made by Tejus Revi", borderwidth=0, cursor="hand2")
    credit.place(relx=0.5, rely=0.98, anchor=CENTER)
    credit.bind("<Button-1>",lambda e:webbrowser.open_new('https://tejus-dev.web.app/'))
    Root.loginForm.pack()
    Root.form.pack(side='right')
    leftDecoration.pack(side='left')
    Root.loginScreen.pack()
    
    #Root.loginScreen.pack_forget()
    #Dashboard().createWindow(Root.dashboard)
    #Root.dashboard.pack()

    return Root.root

  def handleRegisterButton(self, username, password, confirmPassword, errorLabel):
    if not Root.userController.isUsernameAvailable(username.get()):
      errorLabel.config(text="Sorry. That username is taken")
    else:
      if password.get() == confirmPassword.get():
        Root.userController.createUser(User(username.get(), password.get()))
        #errorLabel.config(text="")
        self.handleGoToLogin()
      else:
        errorLabel.config(text="Passwords don't match")

  def handleLogin(self,username, password):
    if Root.userController.authenticateUser(username.get(), password.get()):
      Root.loginScreen.pack_forget()
      Dashboard().createWindow(Root.dashboard)
      Root.dashboard.pack()

  def handleGoToRegister(self):
    Root.loginForm.pack_forget()
    RegisterForm().createWindow(Root.registerForm)
    Root.registerForm.pack()

  def handleGoToLogin(self):
    Root.registerForm.pack_forget()
    LoginForm().createWindow(Root.loginForm)
    Root.loginForm.pack()

  def handleLogout(self):
    Root.root.quit()

class LoginForm(Root):
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
    loginButton = Button(parent, text = "LOGIN", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command = lambda: super(LoginForm, self).handleLogin(username=nameEntry, password=passwordEntry))
    loginButton.place(relx=0.1, rely=0.62, anchor=W, width=300, height=25)
    registerButton = Button(parent, text = "OR REGISTER TODAY", anchor = W, bg="#415575", fg="white", bd=0, padx=95, command = lambda: super(LoginForm, self).handleGoToRegister())
    registerButton.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)

class RegisterForm(Root):
  def __init__(self):
    pass
  def createWindow(self, parent):
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
    registerButton = Button(parent, text = "REGISTER", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=125, command = lambda: super(RegisterForm, self).handleRegisterButton(nameEntry, passwordEntry, confirmPasswordEntry, errorLabel))
    registerButton.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)
    loginButton = Button(parent, text = "LOGIN INSTEAD", anchor = W, bg="#415575", fg="white", bd=0, padx=105, highlightbackground='red', command = lambda: super(RegisterForm, self).handleGoToLogin())
    loginButton.place(relx=0.1, rely=0.78, anchor=W, width=300, height=25)

class Dashboard(Root):
  rightTab = Frame(Root.dashboard, bg='#32425B', width = 600, height=450, borderwidth=0)
  addPasswordFrame = Frame(Root.dashboard, bg='red', width = 600, height=450, borderwidth=0)
  def __init__(self):
    pass
  def createWindow(self, parent):
    profileMenu = Frame(parent, bg='#3a4d6b', width = 200, height=450)
    profileMenu.place(relx=0, rely=0.5, anchor=W, width=200, height=450)
    Label(profileMenu, bg='#3a4d6b', fg='white', font=('Roboto',8), text="Welcome", borderwidth=0).pack( anchor = W , pady=3, padx=10)
    Label(profileMenu, bg='#3a4d6b', fg='white', font=('Roboto',12), text=Dashboard.userController.user.getUsername(), borderwidth=0).pack( anchor = W , pady=5, padx=10)
    var = IntVar()
    R1 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#415575', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Passwords", font=('Roboto',10), variable=var, value=1, command= lambda: self.handleRadioButton(var,Dashboard.rightTab))
    R1.pack( anchor = W , pady=1)
    R2 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#415575', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Credit Cards", font=('Roboto',10), variable=var, value=2, command= lambda: self.handleRadioButton(var, Dashboard.rightTab))
    R2.pack( anchor = W, pady=1)
    #R3 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#415575', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Secure Notes", font=('Roboto',10), variable=var, value=3, command= lambda: self.handleRadioButton(var,Dashboard.rightTab))
    #R3.pack( anchor = W, pady=1)
    logoutButton = Button(profileMenu, text = "LOGOUT", bg="#415575", fg="white", bd=0, highlightbackground='red', command = lambda: super(Dashboard, self).handleLogout())
    logoutButton.place(relx=0, rely=0.97, anchor=W, width=200, height=25)

    Dashboard.rightTab.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
    parent.pack()

  def handleRadioButton(self, var, parent):
    for child in parent.winfo_children():
      child.destroy()
    if var.get() == 1:

      Dashboard.rightTab.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
      PasswordList().createWindow(parent)
    elif var.get() == 2:
      #h1.configure(text="Credit Cards")
      #addNew.configure(command=lambda: self.handleAddNewCreditCard(h1, addNew))
      Dashboard.rightTab.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
    elif var.get() == 3:
      #h1.configure(text="Secure Notes")
      #addNew.configure(command=lambda: self.handleAddNewNote(h1, addNew))
      Dashboard.rightTab.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
  

class AddNewPassword(Dashboard):
  logo = None
  def __init__(self):
    self.sv = StringVar()
  def createWindow(self, parent):
    for child in parent.winfo_children():
      child.destroy()
    h1 = Label(parent, bg='#32425B', fg='white', font=('Roboto',14), borderwidth=0, text='Add New Password')
    h1.place(relx=0.1, rely=0.1, anchor=W)

    websiteLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="WEBSITE", borderwidth=0)
    websiteLabel.place(relx=0.1, rely=0.2, anchor=W)

    logoLabel = Label(parent, borderwidth=0, bg='#32425B')
    self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv, logoLabel))

    websiteEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT, textvariable=self.sv)
    websiteEntry.place(relx=0.1, rely=0.25, anchor=W, width=300, height=25)

    loginLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="LOGIN ID", borderwidth=0)
    loginLabel.place(relx=0.1, rely=0.35, anchor=W)
    loginEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    loginEntry.place(relx=0.1, rely=0.4, anchor=W, width=300, height=25)
    passwordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
    passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
    passwordEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)

    passwordStrengthLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD STRENGTH: ", borderwidth=0)
    passwordStrengthLabel.place(relx=0.1, rely=0.55, anchor=W)

    notesLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="NOTES", borderwidth=0)
    notesLabel.place(relx=0.1, rely=0.65, anchor=W)
    notesEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    notesEntry.place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)

    logoLabel.place(relx=0.9, rely=0.5, anchor=E, width=100, height=100)
    saveButton = Button(parent, text = "SAVE", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command= lambda: self.handleSavePassword(parent, websiteEntry, loginEntry, passwordEntry, notesEntry, AddNewPassword.logo))
    saveButton.place(relx=0.1, rely=0.8, anchor=W, width=300, height=25)

    #PasswordList().createWindow(parent)

  def callback(self, sv, logoLabel):
    url = 'http://logo.clearbit.com/{}?size=80'.format(sv.get())
    response = requests.get(url)
    if(response.status_code == 200):
      logo = Image.open(BytesIO(response.content)).resize((100,100), Image.ANTIALIAS)
      logotk = ImageTk.PhotoImage(logo)
      logoLabel.configure(image = logotk)
      logoLabel.image = logotk
      AddNewPassword.logo = logo
  def handleSavePassword(self, parent, websiteEntry, loginEntry, passwordEntry, notesEntry, logo):
    Root.userController.addPassword(websiteEntry.get(), loginEntry.get(), passwordEntry.get(), notesEntry.get(), logo)
    PasswordList().createWindow(parent)

class PasswordList(Dashboard):
  def __init__(self):
    pass
  def createWindow(self, parent):
    for child in parent.winfo_children():
      child.destroy()
    h1 = Label(parent, bg='#32425B', fg='white', font=('Roboto',14), borderwidth=0, text="Passwords")
    h1.place(relx=0.1, rely=0.1, anchor=W)
    addNew = Button(parent, bg='#198a78', fg='white', font=('Roboto',10), text="Add new", borderwidth=0, command=lambda:self.handleAddNewPassword())
    addNew.place(relx=0.95, rely=0.1, anchor=E)
    canvas = Canvas(parent, height=380, bg='#32425B', bd=0, highlightthickness=0, relief='ridge')
    scroll_y = Scrollbar(parent, orient="vertical", command=canvas.yview, bg='#32425B')

    listOfButtons = Frame(canvas, height=380, borderwidth=0, bg='#32425B')
    row = column = 0
    for password in Dashboard.userController.user.getPasswords():
      card = Label(listOfButtons, borderwidth=0, bg='#32425B', width=100)
      if password.getLogo() == None:
        '''
        cardLogotk = ImageTk.PhotoImage(password.getLogo())
        cardLogo = Label(card, borderwidth=0, bg='#32425B', image=cardLogotk)
        cardLogo.image = cardLogotk
        cardButton = Button(card, text=password.getWebsite(), bg='#32425B', fg='white', borderwidth=0, compound=TOP, width=100, padx=20, pady=20, wraplength=100, command=lambda password=password: PasswordTab().createWindow(password))
        '''
        cardButton = Button(card, text=password.getWebsite(), bg='#32425B', fg='white', borderwidth=0, width=10, padx=20, pady=20, command=lambda password=password: PasswordTab().createWindow(parent, password))
      else:
        cardLogotk = ImageTk.PhotoImage(password.getLogo().resize((50,50), Image.ANTIALIAS))
        cardLogo = Label(card, borderwidth=0, bg='#32425B', image=cardLogotk)
        cardLogo.image = cardLogotk
        cardButton = Button(card, text=password.getWebsite(), bg='#32425B', fg='white', borderwidth=0, image =cardLogotk, compound=TOP, width=100, padx=20, pady=20, wraplength=100, command=lambda password=password: PasswordTab().createWindow(parent, password))
      cardButton.pack()
      card.grid(row=int(row), column=column%4)
      row=row+0.25
      column=column+1
    canvas.create_window(0, 0, anchor='nw', window=listOfButtons)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                    
    canvas.place(relx=0, rely=1, anchor=SW, width=600)
    scroll_y.place(relx=1, rely=1, anchor=SE, height=380)
  def handleAddNewPassword(self):
    AddNewPassword().createWindow(Dashboard.rightTab)
  def handleAddNewCreditCard(self, h1, addNew):
    h1.configure(text="Add New Password")
    addNew.destroy()
  def handleAddNewNote(self, h1, addNew):
    h1.configure(text="Add New Password")
    addNew.destroy()
class PasswordTab(Dashboard):
  def __init__(self):
    pass
  def createWindow(self, parent, password):
    for child in parent.winfo_children():
      child.destroy()
    Label(parent, bg='#32425B', fg='white', font=('Roboto',16), text="Password for "+password.getWebsite(), borderwidth=0).place(relx=0.1, rely=0.2, anchor=W)
    Label(parent, bg='#32425B', fg='white', text="LOGIN", borderwidth=0).place(relx=0.1, rely=0.35, anchor=W)
    Label(parent, bg='#415575', fg='white', font=('Roboto',14), text=password.getLogin(), borderwidth=0).place(relx=0.1, rely=0.4, anchor=W)
    Label(parent, bg='#32425B', fg='white', text="PASSWORD", borderwidth=0).place(relx=0.1, rely=0.45, anchor=W)
    Label(parent, bg='#415575', fg='white', font=('Roboto',14), text=password.getPassword(), borderwidth=0).place(relx=0.1, rely=0.5, anchor=W)
    Label(parent, bg='#32425B', fg='white', text="NOTE", borderwidth=0).place(relx=0.1, rely=0.55, anchor=W)
    Label(parent, bg='#415575', fg='white', font=('Roboto',14), text=password.getNote(), borderwidth=0).place(relx=0.1, rely=0.6, anchor=W)
    
    copyPassword = Button(parent, text = "COPY PASSWORD TO CLIPBOARD", bg='#3a4d6b', fg="white", bd=0, command= lambda: self.copyPasswordToClipboard(password))
    copyPassword.place(relx=0.1, rely=0.7, anchor=W, width=330, height=25)

    editPassword = Button(parent, text = "EDIT", bg="#1ED5B9", fg="white", bd=0, command= lambda: self.handleEditPassword(parent, password))
    editPassword.place(relx=0.1, rely=0.8, anchor=W, width=150, height=25)

    deleteButton = Button(parent, text = "DELETE", bg="#BF4342", fg="white", bd=0, command= lambda: self.deletePassword(parent, Dashboard.userController.user, password))
    deleteButton.place(relx=0.4, rely=0.8, anchor=W, width=150, height=25)
    if password.getLogo() != None:
      cardLogotk = ImageTk.PhotoImage(password.getLogo())
      cardLogo = Label(parent, borderwidth=0, bg='#32425B', image=cardLogotk)
      cardLogo.image = cardLogotk
      cardLogo.place(relx=0.9, rely=0.5, anchor=E, width=100, height=100)
  
  def deletePassword(self, parent, user, password):
    confirmation = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
    if confirmation == 'yes':
      Dashboard.userController.deletePassword(user, password)
      PasswordList().createWindow(parent)
    

  def copyPasswordToClipboard(self, password):
    Root.root.clipboard_clear()
    Root.root.clipboard_append(password.getPassword())
    Root.root.update() 

  def handleEditPassword(self, parent, password):
    EditPassword().createWindow(parent, password)
class EditPassword(Dashboard):
  def __init__(self):
    pass 
  def createWindow(self, parent, password):
    for child in parent.winfo_children():
      child.destroy()
    h1 = Label(parent, bg='#32425B', fg='white', font=('Roboto',14), borderwidth=0, text='Edit credentials for '+password.getWebsite())
    h1.place(relx=0.1, rely=0.1, anchor=W)

    if password.getLogo()!= None:
      logotk = ImageTk.PhotoImage(password.getLogo())
      logoLabel = Label(parent, borderwidth=0, bg='#32425B', image=logotk)
      logoLabel.image = logotk
      logoLabel.place(relx=0.9, rely=0.5, anchor=E, width=100, height=100)

    loginLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="LOGIN ID", borderwidth=0)
    loginLabel.place(relx=0.1, rely=0.3, anchor=W)
    loginEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    loginEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
    loginEntry.insert(0, password.getLogin())

    passwordLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
    passwordLabel.place(relx=0.1, rely=0.4, anchor=W)
    passwordEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    passwordEntry.place(relx=0.1, rely=0.45, anchor=W, width=300, height=25)
    passwordEntry.insert(0, password.getPassword())

    passwordStrengthLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD STRENGTH: ", borderwidth=0)
    passwordStrengthLabel.place(relx=0.1, rely=0.5, anchor=W)

    notesLabel = Label(parent, bg='#32425B', fg='white', font=('Roboto',8), text="NOTES", borderwidth=0)
    notesLabel.place(relx=0.1, rely=0.6, anchor=W)
    notesEntry = Entry(parent, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
    notesEntry.place(relx=0.1, rely=0.65, anchor=W, width=300, height=25)
    notesEntry.insert(0, password.getNote())

    saveButton = Button(parent, text = "SAVE", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command= lambda: self.editPassword(parent, password, loginEntry, passwordEntry, notesEntry, password.getLogo()))
    saveButton.place(relx=0.1, rely=0.75, anchor=W, width=300, height=25)
  
  def editPassword(self, parent, oldPassword, loginEntry, passwordEntry, notesEntry, logo):
    Dashboard.userController.editPassword(oldPassword, loginEntry.get(), passwordEntry.get(), notesEntry.get(), logo)
    PasswordList().createWindow(parent)