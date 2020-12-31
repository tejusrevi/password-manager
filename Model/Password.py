class Password:
  def __init__(self, website, login, password, note, logo, cipherKey):
    self.setWebsite(website)
    self.setLogin(login)
    self.setPassword(password)
    self.setNote(note)
    self.setLogo(logo)
    self.setCipherKey(cipherKey)
  def setCipherKey(self, cipherKey):
    self.cipherKey = cipherKey
  def getCipherKey(self):
    return self.cipherKey
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
  def setLogo(self, logo):
    self.logo = logo
  def getLogo(self):
    return self.logo