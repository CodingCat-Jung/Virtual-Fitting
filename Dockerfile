# Python 3.10 기반 이미지 사용
FROM python:3.11-buster

ENV PYTHONUNBUFFERED = 1
# 작업 디렉토리 설정
WORKDIR /src

RUN pip install "poetry==1.6.1"

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi
# 애플리케이션 소스 복사
COPY . .

# FastAPI 서버 실행
CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
