import threading
import queue
import time


class Table:
  def __init__(self, number):
    self.number = number
    self.is_busy = False


class Customer(threading.Thread):
  def __init__(self, cafe, customer_id):
    threading.Thread.__init__(self)
    self.cafe = cafe
    self.customer_id = customer_id

  def run(self):
    print(f"Посетитель номер {self.customer_id} прибыл.")
    self.cafe.serve_customer(self)


class Cafe:
  def __init__(self, tables):
    self.queue = queue.Queue()
    self.tables = tables
    self.customer_counter = 0

  def customer_arrival(self):
    while True:
      self.customer_counter += 1
      customer = Customer(self, self.customer_counter)
      customer.start()
      time.sleep(1)

  def serve_customer(self, customer):
    for table in self.tables:
      if not table.is_busy:
        self._seat_customer(customer, table)
        return
    print(f"Посетитель номер {customer.customer_id} ожидает свободный стол.")
    self.queue.put(customer)

  def _seat_customer(self, customer, table):
    print(f"Посетитель номер {customer.customer_id} сел за стол {table.number}.")
    table.is_busy = True
    threading.Timer(5, self._finish_serving_customer, [customer, table]).start()

  def _finish_serving_customer(self, customer, table):
    print(f"Посетитель номер {customer.customer_id} покушал и ушёл.")
    table.is_busy = False
    if not self.queue.empty():
      next_customer = self.queue.get()
      self._seat_customer(next_customer, table)


if __name__ == "__main__":
  tables = [Table(i) for i in range(1, 4)]
  cafe = Cafe(tables)

  arrival_thread = threading.Thread(target=cafe.customer_arrival)
  arrival_thread.start()
  arrival_thread.join()
