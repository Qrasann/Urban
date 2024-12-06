from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Настройка базы данных
DATABASE_URL = "sqlite:///./taskmanager.db"

# Создание движка
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Настройка сессии
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базовый класс моделей
Base = declarative_base()
