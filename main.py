#libraries
from dataclasses import dataclass, field
from datetime import datetime
from random import randint

#data
replacements = {'a': '@'
                , 'b': '8'
                , 'e': '3'
                , 'g': '9'
                , 'i': '!'
                , 'l': '1'
                , 'o': '0'
                , 's': '$'
                , 't': '7'
                , 'z': '2'}

#class def
@dataclass
class Password:
  site: str
  site_id: str
  site_pass: str
  last_update:str = (datetime.now())

  def update_pass(self, new_pass):
    self.site_pass = new_pass
    self.last_update = datetime.now()

@dataclass
class User:
  id: str
  email: str
  passwords: list[Password] = field(default_factory=list)

  def add_pass(self, password):
    self.passwords.append(password)

  def remove_pass(self, password):
    self.passwords.remove(password)

#func def
#password generator
def pw_generator(pw, keyword):
    pw = '' #reset password 
    for letter in keyword:
        replaced = 0 #reset tracker to start replacing if valid
        for key in replacements:
            if letter == key:
                pw += replacements[key]
                replaced = 1 #changed tracker to true if the letter is replaced using replacement dict
                continue
        if not replaced:
            #randomizer to change letter to upper case or lower case
            upper_or_lower = random.randint(1, 2)
            if upper_or_lower == 1:
                pw += letter.upper()
            else:
                pw += letter.lower()
            continue
                
    return pw


#test case

user = User('kuroro', 'kuro@gmail.com')
pw1 = Password("Twitch", 'kuroro@gmail.com', 'password123')

user.add_pass(pw1)

print(user.passwords[0].site)
