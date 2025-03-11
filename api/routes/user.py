from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.database import get_db
from api.models.user import User
from api.schemas.user import UserCreate
from api.utils.hashing import get_password_hash

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # 이메일 중복 체크
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")

    # 비밀번호 해싱 후 저장
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "회원가입 성공!", "user_id": new_user.id}
