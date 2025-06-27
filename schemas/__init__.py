"""Manage apps schemas"""

from .user import UserIn, UserOut, UserUpdate
from .inference import InferenceIn, InferenceOut

__all__ = [
    "UserIn",
    "UserOut",
    "InferenceIn",
    "UserUpdate",
    "InferenceOut",
]
