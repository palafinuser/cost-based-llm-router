from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated

from llm_router.db.session import engine, get_db
from llm_router.db.models.base import Base

app = FastAPI()
Base.metadata.create_all(bind=engine)
dbSession = Annotated[Session, Depends(get_db)]

@app.get("/")
def root():
    return {"message":"Cost-Based LLM Router [v0.0.1]"}

@app.get("/health")
def root():
    return {"status":"ok"}

@app.get("/test")
def test(db: dbSession):
    statement = select(1)
    return db.scalars(statement).all()