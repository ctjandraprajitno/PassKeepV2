import pickle
from dataclasses import dataclass

@dataclass
class Dog:
  sound: str = 'bark'

class Cat:
  def __init__(self):
    self.sound = 'meow'

# data = [Cat(), Dog()]

# with open('test.pkl', 'wb') as f:
#   pickle.dump(data, f)

with open('test.pkl', 'rb') as f:
  car = pickle.load(f)[0]
  dogi = pickle.load(f)[1]
  # data = pickle.load(f)

# print(data)

print(car.sound)
print(dogi.sound)
