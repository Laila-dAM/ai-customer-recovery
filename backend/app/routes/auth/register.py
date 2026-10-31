from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models import Company, User
from app.schemas.auth import (
    CurrentUserResponse,
    LoginRequest,
    RegisterRequest,
    RegisterResponse,
    TokenResponse,
)
from app.security import (
    create_access_token,
    get_password_hash,
    verify_password,
)


router = APIRouter()


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
            hashed_password=get_password_hash(payload.password),
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


@router.post("/login", response_model=TokenResponse)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
) -> TokenResponse:
    user = db.scalar(
        select(User).where(User.email == payload.email)
    )

    if user is None or not verify_password(
        payload.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    company = db.get(Company, user.company_id)

    if not user.is_active or company is None or not company.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is inactive",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        user_id=user.id,
        company_id=user.company_id,
        role=user.role,
    )

    return TokenResponse(access_token=access_token)


@router.get("/me", response_model=CurrentUserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
) -> CurrentUserResponse:
    return CurrentUserResponse(
        user_id=current_user.id,
        company_id=current_user.company_id,
        name=current_user.name,
        email=current_user.email,
        role=current_user.role,
    )
