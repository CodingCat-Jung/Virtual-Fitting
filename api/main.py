from fastapi import FastAPI
from api.Register import router as register_router  # Register.py에서 라우터 불러오기

app = FastAPI()

# Register 라우터 포함
app.include_router(register_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)