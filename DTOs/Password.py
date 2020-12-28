class Password:
  def __init__(self, name, password, note):
    self.name = name
    self.password = password
    self.note = note
  
  def setName(self, name):
    self.name = name
  def getName(self):
    return self.name
  def setPassword(self, password):
    self.password = password
  def getPassword(self):
    return self.password
  def setNote(self, note):
    self.note = note
  def getNote(self):
    return self.note