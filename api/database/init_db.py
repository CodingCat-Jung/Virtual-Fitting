import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from api.database.database import engine, Base
from api.models.user_entity import UserEntity

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("✅ User 테이블 생성 완료!")
