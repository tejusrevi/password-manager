from tkinter import *
from View.PasswordList import PasswordList
from tkinter import messagebox

from View.EditPassword import EditPassword

class Dashboard:
  def __init__(self, userController):
    self.userController = userController
  def createWindow(self, parent, handleLogout):
    
    profileMenu = Frame(parent, bg='#3a4d6b', width = 200, height=450)
    rightTab = Frame(parent, bg='#32425B', width = 600, height=450, borderwidth=0)
    profileMenu.place(relx=0, rely=0.5, anchor=W, width=200, height=450)
    Label(profileMenu, bg='#3a4d6b', fg='white', font=('Roboto',8), text="Welcome", borderwidth=0).pack( anchor = W , pady=3, padx=10)
    Label(profileMenu, bg='#3a4d6b', fg='white', font=('Roboto',12), text=self.userController.user.getUsername(), borderwidth=0).pack( anchor = W , pady=5, padx=10)
    var = IntVar()
    R1 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#415575', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Passwords", font=('Roboto',10), variable=var, value=1, command= lambda: self.handleRadioButton(var,rightTab))
    R1.pack( anchor = W , pady=1)
    R2 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#415575', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Credit Cards", font=('Roboto',10), variable=var, value=2, command= lambda: self.handleRadioButton(var, rightTab))
    R2.pack( anchor = W, pady=1)
    R3 = Radiobutton(profileMenu, indicatoron = 0, width = 30, height=2, cursor="hand2",bg='#415575', fg='white', activebackground='#198a78', activeforeground='white', selectcolor='#198a78', padx = 20, borderwidth=0, text="Secure Notes", font=('Roboto',10), variable=var, value=3, command= lambda: self.handleRadioButton(var,rightTab))
    R3.pack( anchor = W, pady=1)
    
    rightTab.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
    PasswordList(self.userController.user.passwords).createWindow(rightTab,self.handleSavePassword, self.copyPasswordToClipboard, self.handleEditPassword, self.deletePassword, self.getDecryptedPassword)

    logoutButton = Button(profileMenu, text = "LOGOUT", bg="#415575", fg="white", bd=0, highlightbackground='red', command = lambda: handleLogout())
    logoutButton.place(relx=0, rely=0.97, anchor=W, width=200, height=25)
    
    parent.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
    parent.pack()

  def handleRadioButton(self, var, parent):
    for child in parent.winfo_children():
      child.destroy()
    if var.get() == 1:
      parent.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
      PasswordList(self.userController.user.passwords).createWindow(parent,self.handleSavePassword, self.copyPasswordToClipboard, self.handleEditPassword, self.deletePassword, self.getDecryptedPassword)
    elif var.get() == 2:
      #h1.configure(text="Credit Cards")
      #addNew.configure(command=lambda: self.handleAddNewCreditCard(h1, addNew))
      parent.place(relx=1, rely=0.5, anchor=E, width=600, height=450)
    elif var.get() == 3:
      #h1.configure(text="Secure Notes")
      #addNew.configure(command=lambda: self.handleAddNewNote(h1, addNew))
      parent.place(relx=1, rely=0.5, anchor=E, width=600, height=450)

  def deletePassword(self, parent, password):
    confirmation = messagebox.askquestion("Delete", "Are you sure you want to delete this password?", icon='warning')
    if confirmation == 'yes':
      self.userController.deletePassword(password)
      PasswordList(self.userController.user.passwords).createWindow(parent,self.handleSavePassword, self.copyPasswordToClipboard, self.handleEditPassword, self.deletePassword, self.getDecryptedPassword)
    

  def copyPasswordToClipboard(self, password):
    tk = Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(self.getDecryptedPassword(password))
    tk.update() 

  def handleEditPassword(self, parent, password):
    EditPassword(password).createWindow(parent, self.editPassword, self.getDecryptedPassword)
  
  
  def handleSavePassword(self, parent, websiteEntry, loginEntry, passwordEntry, notesEntry, logo):
    self.userController.addPassword(websiteEntry.get(), loginEntry.get(), passwordEntry.get(), notesEntry.get(), logo)
    PasswordList(self.userController.user.passwords).createWindow(parent,self.handleSavePassword, self.copyPasswordToClipboard, self.handleEditPassword, self.deletePassword, self.getDecryptedPassword)

  def editPassword(self, parent, oldPassword, loginEntry, passwordEntry, notesEntry, logo):
    self.userController.editPassword(oldPassword, loginEntry.get(), passwordEntry.get(), notesEntry.get(), logo)
    PasswordList(self.userController.user.passwords).createWindow(parent,self.handleSavePassword, self.copyPasswordToClipboard, self.handleEditPassword, self.deletePassword, self.getDecryptedPassword)
  
  def getDecryptedPassword(self, password):
    return self.userController.getDecryptedPassword(password)
  