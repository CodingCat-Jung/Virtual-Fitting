# 로그인 엔드포인트
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.database import get_db
from api.models.user import User
from api.schemas.auth import LoginRequest, TokenResponse
from api.utils.hashing import verify_password
from api.utils.jwt import create_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    # 1. 데이터베이스에서 사용자를 조회
    user = db.query(User).filter(User.useremail == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # 2. 비밀번호 검증
    if not verify_password(request.password, user.userpassword):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # 3. JWT 토큰 생성
    access_token = create_access_token({"sub": user.useremail})

    # 4. 토큰 반환
    return {"access_token": access_token, "token_type": "bearer"}
