from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from db import SessionLocal, get_db
from schema import question_schema
from models import Question
from crud import question_crud

router = APIRouter(prefix="/q")


## schema => 출력 구조와 명세
@router.get("/list", response_model=question_schema.QuestionList)
async def question_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(
        db, skip=page * size, limit=size
    )
    return {
        "total": total,
        "question_list": _question_list,
    }


@router.get("detail/{question_id}", response_model=question_schema.Question)
async def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def question_create(
    _question_create: question_schema.QuestionCreate, db: Session = Depends(get_db)
):
    question_crud.create_question(db=db, question_create=_question_create)
