from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=False, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    userRole = relationship("UserRole", back_populates="user")


class Role(Base):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), unique=True, nullable=False)

    userRole = relationship("UserRole", back_populates="role")
    rolePermission = relationship("RolePermission", back_populates="role")


class Permission(Base):
    __tablename__ = "permissions"
    permission_id = Column(Integer, primary_key=True, index=True)
    permission_name = Column(String(50), unique=True, nullable=False)

    userRole = relationship("UserRole", back_populates="permission")
    rolePermission = relationship("RolePermission",
                                  back_populates="permission")


class UserRole(Base):
    __tablename__ = 'user_roles'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.role_id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.permission_id'))

    user = relationship("User", back_populates="userRole")
    role = relationship("Role", back_populates="userRole")
    permission = relationship("Permission", back_populates="userRole")


class RolePermission(Base):
    __tablename__ = 'role_permissions'
    role_id = Column(Integer, ForeignKey('roles.role_id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.permission_id'),
                           primary_key=True)

    role = relationship("Role", back_populates="rolePermission")
    permission = relationship("Permission", back_populates="rolePermission")
