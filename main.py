from fastapi import FastAPI
from routers.question_router import router as q_router
from routers.answer_router import router as a_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(q_router, prefix="/api/v1")
app.include_router(a_router, prefix="/api/v1")