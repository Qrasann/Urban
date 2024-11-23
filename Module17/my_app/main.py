from my_app.backend.db import engine, Base
from my_app.models.task import Task
from my_app.models.user import User

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    for table in [User.__table__, Task.__table__]:
        print(str(table))
