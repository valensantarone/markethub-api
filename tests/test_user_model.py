import uuid

import pytest
from sqlalchemy.exc import IntegrityError

from app.models.user import User, UserRole


def test_create_user_successful(db_session):
    user = User(
        email="TestUser@Example.com",
        hashed_password="secure_hashed_password_123",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    
    assert isinstance(user.id, uuid.UUID)
    assert user.email == "testuser@example.com"
    assert user.role == UserRole.BUYER
    assert user.is_active is True
    assert user.created_at is not None
    assert user.updated_at is not None
    
def test_email_is_normalized_lowercase():
    user = User(
        email="  JOHN.DOE@GMAIL.COM   ",
        hashed_password="hash",
    )
    assert user.email == "john.doe@gmail.com"
    
def test_empty_email_raises_error():
    with pytest.raises(ValueError, match="El email no puede estar vacío."):
        User(email="", hashed_password="hash")
        
def test_duplicate_email_raises_integrity_error(db_session):
    user1 = User(email="unique@mail.com", hashed_password="hash1")
    db_session.add(user1)
    db_session.commit()
    
    user2 = User(email="UNIQUE@mail.com", hashed_password="hash2")
    db_session.add(user2)
    
    with pytest.raises(IntegrityError):
        db_session.commit()

def test_user_roles(db_session):
    admin = User(email="admin@mail.com", hashed_password="hash", role=UserRole.ADMIN)
    seller = User(email="seller@mail.com", hashed_password="hash", role=UserRole.SELLER)
    
    db_session.add_all([admin, seller])
    db_session.commit()
    
    assert admin.role == UserRole.ADMIN
    assert seller.role == UserRole.SELLER