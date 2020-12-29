class Password:
  def __init__(self, website, login, password, note):
    self.website = website
    self.login = login
    self.password = password
    self.note = note
  
  def setWebsite(self, website):
    self.website = website
  def getWebsite(self):
    return self.website
  def setLogin(self, login):
    self.login = login
  def getLogin(self):
    return self.login
  def setPassword(self, password):
    self.password = password
  def getPassword(self):
    return self.password
  def setNote(self, note):
    self.note = note
  def getNote(self):
    return self.note