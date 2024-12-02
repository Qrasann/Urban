import sqlite3

def initiate_db():
    """Инициализация базы данных: создание таблицы Users."""
    try:
        with sqlite3.connect('not_telegram.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL DEFAULT 1000
                )
            ''')
            conn.commit()
            print("Таблица успешно создана или уже существует.")
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации базы данных: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

def add_user(username, email, age):
    """Добавление нового пользователя."""
    try:
        with sqlite3.connect('not_telegram.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                           (username, email, age, 1000))
            conn.commit()
            print(f"Пользователь {username} успешно добавлен.")
    except sqlite3.IntegrityError:
        print("Ошибка: этот пользователь уже существует в базе данных.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении пользователя: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

def is_included(username):
    """Проверка наличия пользователя."""
    try:
        with sqlite3.connect('not_telegram.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
            result = cursor.fetchone()
            return result is not None
    except sqlite3.Error as e:
        print(f"Ошибка при проверке наличия пользователя: {e}")
        return False
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return False
