from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Define the database URL (SQLite in this case)
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database tables
def init_db():
    Base.metadata.create_all(bind=engine)