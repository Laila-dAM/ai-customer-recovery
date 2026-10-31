from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.config import settings


password_hash = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(
    user_id: int,
    company_id: int,
    role: str,
) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {
        "sub": str(user_id),
        "company_id": company_id,
        "role": role,
        "iat": now,
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )
