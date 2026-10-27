import re

from pydantic import BaseModel, Field, field_validator


class RegisterRequest(BaseModel):
    company_name: str = Field(min_length=2, max_length=150)
    company_email: str = Field(min_length=5, max_length=255)
    company_phone: str | None = Field(default=None, max_length=30)
    name: str = Field(min_length=2, max_length=150)
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=8, max_length=128)

    @field_validator("company_email", "email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        value = value.strip().lower()

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value):
            raise ValueError("Invalid email address")

        return value

    @field_validator("company_name", "name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("This field cannot be empty")

        return value


class RegisterResponse(BaseModel):
    company_id: int
    company_name: str
    user_id: int
    name: str
    email: str
