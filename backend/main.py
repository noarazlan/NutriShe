from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.users import router as users_router
from routers.target import router as target_router
from routers.foods import router as foods_router  # 1. ייבוא הראוטר של המאכלים

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. חיבור הראוטרים לשרת
app.include_router(users_router)
app.include_router(target_router)
app.include_router(foods_router)  

@app.get("/")
def root():
    return {"message": "NutriShe backend is running"}