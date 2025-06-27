"""User schemas."""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base schema for user data."""

    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    """Base schema for user data."""

    password: str

class UserUpdate(UserBase):
    """Schema for updating user data."""

    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    full_name: str | None = None    


class UserOut(UserBase):
    """Schema for user output data."""

    id: int
