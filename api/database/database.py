import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 환경 변수에서 DB URL 가져오기 (Docker 환경 지원)
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+aiomysql://root:qkrwogus1205!@localhost:3306/Virtual_Fitting")

# 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# 세션 설정
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# 베이스 모델 정의
Base = declarative_base()

# DB 세션을 가져오는 의존성 함수
async def get_db():
    async with SessionLocal() as session:
        yield session
