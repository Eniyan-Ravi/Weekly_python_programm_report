from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select


def require_exists(db: Session, model, id: int, name: str = "Resource"):

    stmt = select(model).where(model.id == id)
    obj = db.execute(stmt).scalar_one_or_none()
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{name} not found"
        )
    return obj