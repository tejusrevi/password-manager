class User:
  def __init__(self, username, masterPassword):
    self.username = username
    self.masterPassword = masterPassword
    self.passwords = []

  def setUsername(self, username):
    self.username = username
  def getUsername(self):
    return self.username

  def setMasterPassword(self, masterPassword):
    self.masterPassword = masterPassword
  def getMasterPassword(self):
    return self.masterPassword

  def setPasswords(self, passwords):
    self.passwords = passwords
  def addPassword(self, password):
    self.passwords.append(password)
  def getPasswords(self):
    return self.passwords