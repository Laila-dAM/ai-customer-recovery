from fastapi import APIRouter, Depends, HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import Company, User
from app.schemas.auth import RegisterRequest, RegisterResponse


router = APIRouter()
password_hash = PasswordHash.recommended()


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db),
) -> RegisterResponse:
    existing_company = db.scalar(
        select(Company).where(Company.email == payload.company_email)
    )

    if existing_company:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Company email is already registered",
        )

    existing_user = db.scalar(
        select(User).where(User.email == payload.email)
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User email is already registered",
        )

    company = Company(
        name=payload.company_name,
        email=payload.company_email,
        phone=payload.company_phone,
    )

    try:
        db.add(company)
        db.flush()

        user = User(
            company_id=company.id,
            name=payload.name,
            email=payload.email,
            hashed_password=password_hash.hash(payload.password),
            role="admin",
        )

        db.add(user)
        db.commit()
        db.refresh(company)
        db.refresh(user)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Company or user email is already registered",
        ) from None

    return RegisterResponse(
        company_id=company.id,
        company_name=company.name,
        user_id=user.id,
        name=user.name,
        email=user.email,
    )
