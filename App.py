from tkinter import *
from PIL import Image, ImageTk
from DTOs.User import User
from DTOs.Password import Password
import base64, pickle
from CaesarCipher import encrypt


users = []

with open("data.pkl", "rb") as input_file:
  e = pickle.load(input_file)
  print(e)
  for j in e:
    print(j.getUsername())

def registerUser(username, password):
  user = User(username.get(), password.get())
  users.append(user)
  print(users)
  with open('data.pkl', 'wb') as output:
    pickle.dump(users, output, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
  root = Tk()
  #root.resizable(False, False)
  root.title('Password Manager')
  root.configure(background='#32425B')
  root.geometry("800x450")

  loginScreen = Frame(root, bg='#32425B', width = 800, height=450)
  render = ImageTk.PhotoImage(Image.open('assets/images/bg.png'))

  leftDecoration = Label(loginScreen, image=render, borderwidth=0)
  loginForm = Frame(loginScreen, bg='#32425B', width = 400, height=450)
  
  h1 = Label(loginForm, bg='#32425B', fg='white', font=('Roboto',14), text="LOGIN", borderwidth=0).place(relx=0.5, rely=0.2, anchor=CENTER)

  nameLabel = Label(loginForm, bg='#32425B', fg='white', font=('Roboto',8), text="USERNAME", borderwidth=0)
  nameLabel.place(relx=0.1, rely=0.3, anchor=W)
  nameEntry = Entry(loginForm, bd=0, bg='#415575', fg='white', font=('Roboto',12), relief=FLAT)
  nameEntry.place(relx=0.1, rely=0.35, anchor=W, width=300, height=25)
  passwordLabel = Label(loginForm, bg='#32425B', fg='white', font=('Roboto',8), text="PASSWORD", borderwidth=0)
  passwordLabel.place(relx=0.1, rely=0.45, anchor=W)
  passwordEntry = Entry(loginForm, bd=0, bg='#415575', fg='white', show="·", font=('Roboto',30), relief=FLAT)
  passwordEntry.place(relx=0.1, rely=0.5, anchor=W, width=300, height=25)

  print(nameEntry)
  loginButton = Button(loginForm, text = "LOGIN", anchor = W, bg="#1ED5B9", fg="white", bd=0, padx=130, command = lambda: registerUser(username=nameEntry, password=passwordEntry)).place(relx=0.1, rely=0.62, anchor=W, width=300, height=25)
  registerButton = Button(loginForm, text = "REGISTER", anchor = W, bg="#415575", fg="white", bd=0, padx=125).place(relx=0.1, rely=0.7, anchor=W, width=300, height=25)

  loginForm.pack(side='right')
  leftDecoration.pack(side='left')
  loginScreen.pack()
  root.mainloop()