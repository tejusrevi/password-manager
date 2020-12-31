class User:
  def __init__(self, username, masterPassword, cipherKey):
    self.setUsername(username)
    self.setMasterPassword(masterPassword)
    self.setCipherKey(cipherKey)
    self.passwords = []

  def setCipherKey(self, cipherKey):
    self.cipherKey = cipherKey
  def getCipherKey(self):
    return self.cipherKey

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
    
  def deletePassword(self, password):
    self.passwords.remove(password)

  def getPasswords(self):
    return self.passwords
