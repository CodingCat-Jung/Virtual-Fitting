import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from api.database.database import get_db
from api.models.user import User
from datetime import datetime, timedelta
#  .env 파일 로드
load_dotenv()

#  환경 변수에서 SECRET_KEY 가져오기
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")  # 기본값은 보안상 위험하니 .env 설정 필수
ALGORITHM = "HS256"

# FastAPI의 OAuth2PasswordBearer를 사용하여 "Authorization: Bearer <token>" 방식 지원
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#  JWT 토큰 검증 함수
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.query(User).filter(User.useremail == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt