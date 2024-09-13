from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/post_qrdata/", response_model=schemas.Data)
def create_qr_data(data: schemas.QRDataCreate, db: Session = Depends(get_db)):
    return crud.create_QR_data(db=db, data=data)


@app.get("/get_qrdata/{id}", response_model=schemas.Data)
def read_qr_data(id: int, db: Session = Depends(get_db)):
    db_data = crud.get_data(db=db, id=id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="QRData not found")
    return db_data


@app.get("/getall_qrdata/", response_model=list[schemas.Data])
def read_all_qr_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_data(db=db, skip=skip, limit=limit)


@app.delete("/delete_qrdata/{id}", response_model=schemas.Data)
def delete_qr_data(id: int, db: Session = Depends(get_db)):
    db_data = crud.delete_data(db=db, id=id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="QRData not found")
    return db_data