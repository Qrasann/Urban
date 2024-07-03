class EvenNumbers:
  def __init__(self, start=0, end=1):
    if start >= end:
      raise ValueError("Значение start должно быть меньше end")
    self.start = start
    self.end = end
    self.current = start

  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.end:
      raise StopIteration

    current = self.current
    self.current += 2
    return current

en = EvenNumbers(10, 25)
for i in en:
    print(i)
