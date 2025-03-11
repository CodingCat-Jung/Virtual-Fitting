from fastapi import FastAPI
from api.routes import auth, user

app = FastAPI(title="User API")

# 사용자 라우터 등록
app.include_router(user.router)
app.include_router(auth.router)


# 기본 루트 추가 (테스트용
@app.get("/")
def root():
    return {"message": "FastAPI 서버가 정상적으로 실행 중입니다!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, debug=True)
