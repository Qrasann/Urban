import requests
import pandas as pd
import matplotlib.pyplot as plt

# --------------------- Библиотека Requests ---------------------

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
  print("Первые три записи с сайта JSONPlaceholder:\n")
  for post in response.json()[:3]:
    print(f"ID: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}\n")
else:
  print("Не удалось получить данные.")

new_post = {
  'title': 'New Post',
  'body': 'This is a new post created using the Requests library.',
  'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)

if response.status_code == 201:
  print("Успешно создана новая запись:")
  print(response.json())
else:
  print("Не удалось создать новую запись.")

# --------------------- Библиотека Pandas ---------------------

df = pd.read_csv('data/iris.csv')

print("\nПервые пять строк данных:\n", df.head(), "\n")

print("Описание данных:\n", df.describe(), "\n")

filtered_data = df[df['species'] == 'setosa']
print("Фильтрованные данные (только setosa):\n", filtered_data.head(), "\n")

grouped_data = df.groupby('species').mean()
print("Средние значения по видам:\n", grouped_data, "\n")

df['sepal_ratio'] = df['sepal_length'] / df['sepal_width']
print("Данные с новым столбцом:\n", df.head(), "\n")

# --------------------- Библиотека Matplotlib ---------------------

# 8. Линейный график
plt.figure(figsize=(10, 6))
plt.plot(df['sepal_length'], label='Длина чашелистика', color='b')
plt.plot(df['sepal_width'], label='Ширина чашелистика', color='r')
plt.title('Длина и ширина чашелистика')
plt.xlabel('Индекс')
plt.ylabel('Сантиметры')
plt.legend()
plt.grid(True)
plt.show()

# 9. Гистограмма
plt.figure(figsize=(10, 6))
plt.hist(df['petal_length'], bins=30, color='g', alpha=0.7)
plt.title('Гистограмма длины лепестков')
plt.xlabel('Длина лепестков (см)')
plt.ylabel('Количество')
plt.show()

# 10. Круговая диаграмма
species_counts = df['species'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
  species_counts,
  labels=species_counts.index,
  autopct='%1.1f%%',
  startangle=140,
  colors=['#ff9999', '#66b3ff', '#99ff99']
)
plt.title('Соотношение видов ирисов')
plt.axis('equal')
plt.show()
