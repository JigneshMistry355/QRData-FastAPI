from pydantic import BaseModel

class QRBase(BaseModel):
    client_id : int
    data : str | None = None

class QRDataCreate(QRBase):
    client_id : int
    data : str

class Data(QRBase):
    id : int
    client_id : int
    data : str

    class Config:
        orm_mode = True
