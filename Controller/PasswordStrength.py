import re

def calculatePasswordStrength(password):
  strength = 0
  if re.search("[A-Z]", password):
    strength += 1
  if re.search("[a-z]", password):
    strength += 1
  if re.search("[1-9]", password):
    strength += 1
  if not password.isalnum():
    strength += 1
  if (len(password) < 8):
    strength = strength/2

  return int(strength)
