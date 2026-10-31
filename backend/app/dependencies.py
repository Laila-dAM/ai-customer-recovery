from collections.abc import Generator
from typing import Callable

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.config import settings
from app.database import SessionLocal
from app.models import Company, User


bearer_scheme = HTTPBearer(auto_error=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired authentication token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if credentials is None:
        raise unauthorized

    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )

        user_id = int(payload["sub"])
        company_id = int(payload["company_id"])
        token_role = payload["role"]

    except (jwt.InvalidTokenError, KeyError, TypeError, ValueError):
        raise unauthorized from None

    user = db.get(User, user_id)

    if user is None or not user.is_active:
        raise unauthorized

    company = db.get(Company, user.company_id)

    if (
        company is None
        or not company.is_active
        or user.company_id != company_id
        or user.role != token_role
    ):
        raise unauthorized

    return user


def require_roles(*roles: str) -> Callable[..., User]:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )

        return current_user

    return role_checker
