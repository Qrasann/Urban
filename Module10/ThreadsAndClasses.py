import threading
import time


class Knight(threading.Thread):
  enemies = 100
  lock = threading.Lock()

  def __init__(self, name, power):
    super().__init__()
    self.name = name
    self.power = power

  def run(self):
    days = 0
    print(f"{self.name}, на нас напали!")
    while True:
      with Knight.lock:
        if Knight.enemies <= 0:
          break
        Knight.enemies -= self.power
        days += 1
        remaining_enemies = max(Knight.enemies, 0)
        print(f"{self.name}, сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")
      time.sleep(1)
    print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Naruto', 7)
second_knight = Knight('Sir Steve', 3)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
