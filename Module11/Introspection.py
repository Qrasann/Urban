def introspection_info(obj):
  obj_type = type(obj).__name__

  attributes = dir(obj)

  methods = [attr for attr in attributes if callable(getattr(obj, attr)) and not attr.startswith('__')]

  module = getattr(obj, '__module__', 'builtin')

  info = {
    'Тип': obj_type,
    'Модуль': module,
    'Атрибуты': [attr for attr in attributes if not callable(getattr(obj, attr)) and not attr.startswith('__')],
    'Методы': methods
  }

  return info


number_info = introspection_info(322)
print("Информация о числе:")
print(number_info)

string_info = introspection_info("Панда")
print('Информация о строке:')
print(string_info)
