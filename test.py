import pickle
from dataclasses import dataclass

@dataclass
class Dog:
  sound: str = 'bark'

  def speak(self):
    print(self.sound)

class Cat:
  def __init__(self):
    self.sound = 'meow'

@dataclass
class Frog:
  sound: str = 'ribbit'

# data = [Cat(), Dog(), Frog()]

# with open('test.pkl', 'wb') as f:
#   pickle.dump(data, f)

with open('test.pkl', 'rb') as f:
  data = pickle.load(f)

print(data)

car = data[0]
dogi = data[1]
fro = data[2]

print(car.sound)
print(dogi.sound)
print(fro.sound)

dogi.speak()