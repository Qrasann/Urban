class Vehicle:
  def __init__(self):
    self.vehicle_type = 'none'

class Car:
  def __init__(self):
    self.price = 1000000
  def horse_powers(self):
    return

class Nissan(Vehicle, Car):
  def __init__(self):
    super().__init__()
    self.price = 1200000
    self.vehicle_type = 'car'

  def horse_powers(self):
   return 322

nissan = Nissan()

print(nissan.vehicle_type)
print(nissan.price)
print(nissan.horse_powers())