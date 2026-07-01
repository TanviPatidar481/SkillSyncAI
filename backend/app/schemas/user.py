from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.user import UserRole


class UserResponse(BaseModel):
    id: UUID
    email: str
    role: UserRole
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )