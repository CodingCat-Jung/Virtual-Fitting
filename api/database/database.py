from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 로컬 MySQL 접속 정보
DATABASE_URL = "mysql+pymysql://root:qkrwogus1205!@localhost:3306/virtual_fitting"

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 (모든 모델이 이 클래스를 상속받음)
Base = declarative_base()

# DB 연결을 위한 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
