def add_everything_up(a, b):
  try:
    return a + b
  except TypeError:
    return str(a) + str(b)


print(add_everything_up(322, 'Naruto'))
print(add_everything_up('Minecraft', 2408))
print(add_everything_up(123.456, 7))
print(add_everything_up('Саске', 'вернись'))
print(add_everything_up(8, 24))