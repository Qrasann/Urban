calls = 0

def count_call():
  global calls
  calls += 1

def string_info(string):
  global z,x,y
  count_call()
  z = len(string)
  x = string.upper()
  y = string.lower()
  print(z,x,y)


def is_contains(string,list):
  count_call()
  string.lower()
  lowercase_list = [item.lower() for item in list]
  return string in lowercase_list


string_info('kek')
string_info('Pashilaya')
print(is_contains('lol',['loL','loShka','mEme']))
print(is_contains('key', ['clone','naruto','sasuke']))
print(calls)