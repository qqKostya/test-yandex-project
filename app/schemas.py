from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password_hash: str
    email: str


class RoleCreate(BaseModel):
    role_name: str


class PermissionCreate(BaseModel):
    permission_name: str
