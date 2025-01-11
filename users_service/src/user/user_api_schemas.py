from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Schema for creating a new user
class UserCreate(BaseModel):
    name: str = Field(..., title="Name of the user", min_length=2, max_length=100)
    email: EmailStr = Field(..., title="Email address of the user")
    password: str = Field(..., title="Password", min_length=6)
    newProp: str = Field(..., title="newProp of the user", min_length=2, max_length=100)
    

    class Config:
        json_schema_extra= {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "password": "securepassword123",
                "newProp": "bdika"
            }
        }


# Schema for returning user data
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    newProp: str

    class Config:
        from_attributes = True
        json_schema_extra= {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "newProp": "bdika"
            }
        }


# Schema for updating user information
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, title="Updated name of the user", min_length=2, max_length=100)
    email: Optional[EmailStr] = Field(None, title="Updated email address of the user")
    password: Optional[str] = Field(None, title="Updated password", min_length=6)
    newProp: str = Field(..., title="newProp of the user", min_length=2, max_length=100)
    

    class Config:
        json_schema_extra= {
            "example": {
                "name": "John Doe Jr.",
                "email": "john.jr@example.com",
                "password": "newsecurepassword123",
                "newProp": "bdika"
            }
        }
