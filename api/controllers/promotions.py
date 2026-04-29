import random
import string
from datetime import date, timedelta

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ..models import promotions as model


def _handle_db_error(db: Session, error: SQLAlchemyError):
    db.rollback()
    detail = str(error.__dict__.get("orig", error))
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


def create(db: Session, request):
    existing_promotion = db.query(model.Promotion).filter(
        model.Promotion.code == request.code
    ).first()

    if existing_promotion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Promotion code already exists",
        )

    new_promotion = model.Promotion(
        code=request.code.upper(),
        expiry_date=request.expiry_date,
    )

    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
    except SQLAlchemyError as e:
        _handle_db_error(db, e)

    return new_promotion


def generate(db: Session, request):
    prefix = request.prefix.upper().replace(" ", "")
    code_length = request.code_length
    expiry_date = date.today() + timedelta(days=request.days_valid)

    for _ in range(10):
        random_code = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=code_length)
        )
        promo_code = f"{prefix}-{random_code}" if prefix else random_code

        existing_promotion = db.query(model.Promotion).filter(
            model.Promotion.code == promo_code
        ).first()

        if not existing_promotion:
            new_promotion = model.Promotion(
                code=promo_code,
                expiry_date=expiry_date,
            )

            try:
                db.add(new_promotion)
                db.commit()
                db.refresh(new_promotion)
            except SQLAlchemyError as e:
                _handle_db_error(db, e)

            return new_promotion

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Could not generate a unique promotion code. Please try again.",
    )


def read_all(db: Session):
    try:
        return db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        detail = str(e.__dict__.get("orig", e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


def read_one(db: Session, item_id: int):
    try:
        promotion = db.query(model.Promotion).filter(model.Promotion.id == item_id).first()
    except SQLAlchemyError as e:
        detail = str(e.__dict__.get("orig", e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found",
        )

    return promotion


def update(db: Session, item_id: int, request):
    promotion = db.query(model.Promotion).filter(model.Promotion.id == item_id).first()

    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found",
        )

    update_data = request.dict(exclude_unset=True)

    if "code" in update_data and update_data["code"]:
        update_data["code"] = update_data["code"].upper()
        existing_promotion = db.query(model.Promotion).filter(
            model.Promotion.code == update_data["code"],
            model.Promotion.id != item_id,
        ).first()

        if existing_promotion:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Promotion code already exists",
            )

    for key, value in update_data.items():
        setattr(promotion, key, value)

    try:
        db.commit()
        db.refresh(promotion)
    except SQLAlchemyError as e:
        _handle_db_error(db, e)

    return promotion


def delete(db: Session, item_id: int):
    promotion = db.query(model.Promotion).filter(model.Promotion.id == item_id).first()

    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found",
        )

    try:
        db.delete(promotion)
        db.commit()
    except SQLAlchemyError as e:
        _handle_db_error(db, e)
