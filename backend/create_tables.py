from data.base import Base
from data.database import engine

# חשוב: הייבוא טוען את כל מחלקות המודלים.
import data.models  # noqa: F401


def create_tables() -> None:
    print("Tables SQLAlchemy knows about:")
    print(list(Base.metadata.tables.keys()))

    Base.metadata.create_all(bind=engine)

    print("Tables created successfully")


if __name__ == "__main__":
    create_tables()