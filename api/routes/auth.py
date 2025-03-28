# 로그인 엔드포인트
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.database import get_db
from api.models.user import User
from api.schemas.auth import LoginRequest, TokenResponse
from api.utils.hashing import verify_password
from api.utils.jwt import create_access_token
import logging

router = APIRouter()

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    logger.debug(f"📢 로그인 요청 데이터: {request.dict()}")  # 요청 데이터 확인
    
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        logger.warning(f"사용자 없음: {request.email}")
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(request.password, user.password):
        logger.warning(f"비밀번호 불일치: {request.email}")
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = create_access_token({"sub": user.email})
    logger.info(f"✅ 로그인 성공: {request.email}")
    return {"access_token": access_token, "token_type": "bearer"}