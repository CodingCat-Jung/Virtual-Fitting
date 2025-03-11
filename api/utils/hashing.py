from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 비밀번호 검증 함수 추가
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)