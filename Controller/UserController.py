import pickle
from Model.User import User
from Model.Password import Password

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

  def createUser(self, newUser):
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
        if user.getMasterPassword() == password:
          self.user = user
          return True
    return False

  def addPassword(self, website, login, password, notes, logo):
    password = Password(website, login, password, notes, logo)
    for user in self.getUsers():
      if user.getUsername() == self.user.getUsername():
        user.addPassword(password)
        self.user = user
    print(self.users)
    with open('data.pkl', 'wb') as output:
      pickle.dump(self.getUsers(), output, pickle.HIGHEST_PROTOCOL)
  
