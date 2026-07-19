from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router
from routers.foods import router as foods_router
from routers.target import router as target_router
import uvicorn

app = FastAPI(title="NutriShe API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router)
app.include_router(foods_router)
app.include_router(target_router)



@app.get("/")
def read_root():
    return {"message": "Welcome to NutriShe API!"}