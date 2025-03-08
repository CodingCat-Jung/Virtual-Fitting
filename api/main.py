from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.database.database import engine, Base, get_db
from api.models.user_entity import User
from api.schemas.user_schema import UserCreate, UserResponse
from api.utils.utils import hash_password

app = FastAPI()

# MySQL 테이블 생성 (서버 시작 시 실행)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    # 이메일 중복 체크
    result = await db.execute(select(User).filter(User.email == user_data.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 비밀번호 해싱 후 저장
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user
