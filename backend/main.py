from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.users import router as users_router
from routers.target import router as target_router
from routers.recipes import router as recipes_router
from routers.favorites import router as favorites_router
from routers.tips import router as tips_router
from routers.foods import router as foods_router

app = FastAPI()


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router)
app.include_router(target_router)
app.include_router(recipes_router)
app.include_router(favorites_router)
app.include_router(tips_router)
app.include_router(foods_router)

@app.get("/")
def root():
    return {"message": "NutriShe backend is running"}