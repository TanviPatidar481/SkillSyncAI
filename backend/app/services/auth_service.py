from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        request: RegisterRequest,
    ) -> User:
        stmt = select(User).where(User.email == request.email)
        existing_user = db.scalar(stmt)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        hashed_password = hash_password(request.password)

        user = User(
            email=request.email,
            password_hash=hashed_password,
            role=request.role,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def login_user(
        db: Session,
        request: LoginRequest,
    ) -> TokenResponse:
        stmt = select(User).where(User.email == request.email)
        user = db.scalar(stmt)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(request.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        access_token = create_access_token(
            user_id=str(user.id),
            role=user.role.value,
        )

        return TokenResponse(
            access_token=access_token,
        )