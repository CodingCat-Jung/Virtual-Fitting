# 1. Python 3.10 기반 이미지 사용
FROM python:3.10

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 패키지 설치
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

# 4. 애플리케이션 코드 복사
COPY . .

# 5. FastAPI 서버 실행
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
