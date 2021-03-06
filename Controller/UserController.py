import pickle
from Model.User import User
from Model.Password import Password
from Controller.EncryptDecrypt import encrypt, decrypt
import random

class UserController:
  def __init__(self):
    self.users = []
    self.user = None
    try:
      with open("data.pkl", "rb") as input_file:
        self.users = pickle.load(input_file)

    except FileNotFoundError:
      pass

  def getUsers(self):
    return self.users

  def createUser(self, username, password):
    cipherKey = random.randint(1,26)
    encryptedPassword = encrypt(password, cipherKey)
    newUser = User(username, encryptedPassword, cipherKey)
    self.getUsers().append(newUser)
    with open('data.pkl', 'wb') as output:
      pickle.dump(self.getUsers(), output, pickle.HIGHEST_PROTOCOL)

  def isUsernameAvailable(self, username):
    usernameAvailable = True
    for user in self.getUsers():
      if user.getUsername() == username:
        usernameAvailable = False
    return usernameAvailable
  
  def authenticateUser(self, username, password):
    for user in self.getUsers():
      if user.getUsername() == username:
        if decrypt(user.getMasterPassword(), user.getCipherKey()) == password:
          self.user = user
          return True
    return False

  def addPassword(self, website, login, password, notes, logo):
    cipherKey = random.randint(1,26)
    encryptedPassword = encrypt(password, cipherKey)
    password = Password(website, login, encryptedPassword, notes, logo, cipherKey)
    for user in self.getUsers():
      if user.getUsername() == self.user.getUsername():
        user.addPassword(password)
        self.user = user
    with open('data.pkl', 'wb') as output:
      pickle.dump(self.getUsers(), output, pickle.HIGHEST_PROTOCOL)

  def deletePassword(self, password):
    for user in self.getUsers():
      if user.getUsername() == self.user.getUsername():
        user.deletePassword(password)
        self.user = user
    with open('data.pkl', 'wb') as output:
      pickle.dump(self.getUsers(), output, pickle.HIGHEST_PROTOCOL)
  
  def editPassword(self, oldPassword, login, password, note, logo):
    encryptedPassword = encrypt(password, oldPassword.getCipherKey())
    for user in self.getUsers():
      if user.getUsername() == self.user.getUsername():
        passwordToEdit = [p for p in user.getPasswords() if p == oldPassword][0]
        passwordToEdit.setLogin(login)
        passwordToEdit.setPassword(encryptedPassword)
        passwordToEdit.setNote(note)
    with open('data.pkl', 'wb') as output:
      pickle.dump(self.getUsers(), output, pickle.HIGHEST_PROTOCOL)
  
  def getDecryptedPassword(self, password):
    return decrypt(password.getPassword(), password.getCipherKey())


  
