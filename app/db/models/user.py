from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship

from app.db.models import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    created_at = Column(String(255), unique=True, nullable=False)
    ip_address = Column(String(255), unique=True, nullable=False)


    location = relationship("Location", back_populates="user")
    device = relationship("Device", back_populates="user")


    explosive_content = relationship("ExplosiveContent", back_populates="user")
    hostage_content = relationship("HostageContent", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, created_at={self.created_at})>"
