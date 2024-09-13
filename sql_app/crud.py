from sqlalchemy.orm import Session
from . import models, schemas

def get_data(db: Session, id: int):
    return db.query(models.QRData).filter(models.QRData.id == id).first()

def get_all_data(db: Session, skip: int, limit: int = 100):
    return db.query(models.QRData).offset(skip).limit(limit).all()

def create_QR_data(db: Session, data: schemas.Data):
    db_user = models.QRData(client_id = data.client_id, data = data.data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_data(db: Session, id: int):
    db_data = db.query(models.QRData).filter(models.QRData.id == id).first()
    if db_data:
        db.delete(db_data)
        db.commit()
        return db_data
    return None

