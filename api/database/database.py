from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:qkrwogus1205!@127.0.0.1:3306/Virtual_Fitting"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    print("❌ Database connection failed:", e)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
