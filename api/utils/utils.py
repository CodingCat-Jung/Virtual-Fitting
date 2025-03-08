from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """비밀번호를 해싱하여 반환"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """입력한 비밀번호가 저장된 해시값과 일치하는지 확인"""
    return pwd_context.verify(plain_password, hashed_password)
