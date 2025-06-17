import pickle
from dataclasses import dataclass

@dataclass
class Dog:
  self: str = 'bark'

class Cat:
  def __init__(self):
    self.sound = 'meow'

# data = Dog()

# with open('test.pkl', 'wb') as f:
#   pickle.dump(data, f)

with open('test.pkl', 'rb') as f:
  loaded_data = pickle.load(f)

print(loaded_data.sound)