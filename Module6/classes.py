class Car:
  price = 1000000
  def horse_powers(self):
    return

class Nissan(Car):
  price = 1200000
  def horse_powers(self):
    return 250

class Kia(Car):
  price = 800000
  def horse_powers(self):
    return 180


nissan = Nissan()
kia = Kia()
car = Car()

print("Car price:", Car.price)
print("Car horse powers:", car.horse_powers())
print("Nissan price:", Nissan.price)
print("Nissan horse powers:", nissan.horse_powers())
print("Kia price:", Kia.price)
print("Kia horse powers:", kia.horse_powers())
