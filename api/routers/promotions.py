from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..controllers import promotions as controller
from ..dependencies.database import get_db
from ..schemas import promotions as schema

router = APIRouter(
    prefix="/promotions",
    tags=["Promotions"],
)


@router.post("/", response_model=schema.Promotion, status_code=status.HTTP_201_CREATED)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.post("/generate", response_model=schema.Promotion, status_code=status.HTTP_201_CREATED)
def generate(request: schema.PromotionGenerate, db: Session = Depends(get_db)):
    return controller.generate(db=db, request=request)


@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Promotion)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Promotion)
def update(item_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    controller.delete(db=db, item_id=item_id)
