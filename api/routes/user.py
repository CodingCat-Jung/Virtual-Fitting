from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.database import get_db
from api.models.user import User
from api.schemas.user import UserCreate
from api.utils.jwt import get_current_user
from api.utils.hashing import get_password_hash

router = APIRouter(
    prefix="/users",  # URL 구조 정리
    tags=["users"]  # API 문서에서 users 그룹으로 정리
)

@router.post("/register", status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    회원가입 API  
    - 중복 이메일 체크  
    - 비밀번호 해싱 후 저장  
    - 회원가입 성공 시 `user_id` 및 `username` 반환  
    """
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

    return {
        "message": "회원가입 성공!",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }

#  로그인한 사용자만 접근 가능한 API
@router.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return {"email": current_user.useremail, "username": current_user.username}
