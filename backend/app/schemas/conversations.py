from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


ConversationChannel = Literal[
    "whatsapp",
    "email",
    "sms",
]

ConversationStatus = Literal[
    "open",
    "closed",
]

MessageDirection = Literal[
    "inbound",
    "outbound",
]


class ConversationCreate(BaseModel):
    lead_id: int = Field(gt=0)
    channel: ConversationChannel = "whatsapp"


class ConversationUpdate(BaseModel):
    status: ConversationStatus


class ConversationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    lead_id: int
    channel: ConversationChannel
    status: ConversationStatus
    created_at: datetime
    updated_at: datetime


class MessageCreate(BaseModel):
    sender: str = Field(min_length=1, max_length=30)
    direction: MessageDirection
    content: str = Field(min_length=1, max_length=10000)

    @field_validator("content")
    @classmethod
    def validate_content(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Message content cannot be empty")

        return value


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    conversation_id: int
    sender: str
    direction: MessageDirection
    content: str
    created_at: datetime
