from fastapi import FastAPI, Request
from api.routes import auth, user
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import logging
import uvicorn

app = FastAPI(title="User API")

# 사용자 라우터 등록
app.include_router(user.router)
# 로그인 엔드포인트 라우터 등록
app.include_router(auth.router, prefix="/auth")

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 422 예외 처리 핸들러 추가
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"🚨 422 오류 발생! 요청 데이터: {await request.json()}")
    logger.error(f"📌 오류 상세: {exc.errors()}")  
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

# 기본 루트 추가 (테스트용)
@app.get("/")
def root():
    return {"message": "FastAPI 서버가 정상적으로 실행 중입니다!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, debug=True)

