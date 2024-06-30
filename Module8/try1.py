class InvalidDataException(Exception):
  """Исключение вызывается, когда переданные данные некорректны."""
  pass


class ProcessingException(Exception):
  """Исключение вызывается, когда возникает ошибка при обработке данных."""
  pass


def process_data(data):
  if not isinstance(data, int):
    raise InvalidDataException("Данные должны быть целым числом.")
  if data < 0:
    raise ProcessingException("Число не может быть отрицательным.")
  return data * 2


def handle_data(data):
  try:
    result = process_data(data)
    print(f"Результат обработки данных: {result}")
  except InvalidDataException as e:
    print(f"Ошибка: {e}")
    raise
  except ProcessingException as e:
    print(f"Ошибка: {e}")
    raise


def main():
  try:
    handle_data("not an int")
  except Exception as e:
    print(f"Исключение было передано дальше: {e}")

  try:
    handle_data(-5)
  except Exception as e:
    print(f"Исключение было передано дальше: {e}")

  try:
    handle_data(10)
  except Exception as e:
    print(f"Исключение было передано дальше: {e}")


if __name__ == "__main__":
  main()
