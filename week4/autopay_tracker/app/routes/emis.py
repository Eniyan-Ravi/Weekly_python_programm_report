from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schema import EMICreate, EMIOut, EMIUpdate
from app.services import emi_service

router = APIRouter(prefix="/emis", tags=["EMI"])

@router.post("/", response_model=EMIOut)
def create_emi(emi_request: EMICreate, db: Session = Depends(get_db)):
    return emi_service.create_emi(db, emi_request)

@router.get("/", response_model=List[EMIOut])
def get_emis(db: Session = Depends(get_db)):
    return emi_service.list_emis(db)

@router.get("/{emi_id}", response_model=EMIOut)
def get_emi(emi_id: int, db: Session = Depends(get_db)):
    return emi_service.get_emi(db, emi_id)

@router.put("/{emi_id}", response_model=EMIOut)
def update_emi(emi_id: int, emi_request: EMIUpdate, db: Session = Depends(get_db)):
    return emi_service.update_emi(db, emi_id, emi_request)

@router.delete("/{emi_id}")
def delete_emi(emi_id: int, db: Session = Depends(get_db)):
    emi_service.delete_emi(db, emi_id)
    return {"message": "EMI has been Deleted successfully"}