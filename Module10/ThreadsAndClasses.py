import threading
import time


class Knight(threading.Thread):
  def __init__(self, name, power):
    super().__init__()
    self.name = name
    self.power = power
    self.enemies = 100

  def run(self):
    days = 0
    print(f"{self.name}, на нас напали!")
    while self.enemies > 0:
      days += 1
      self.enemies -= self.power
      remaining_enemies = max(self.enemies, 0)
      print(f"{self.name} сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")
      time.sleep(1)
    print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Naruto', 7)
second_knight = Knight('Sir Steve', 10)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
