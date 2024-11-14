from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship

from app.db.models import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    created_at = Column(DATETIME)

    # Relationships
    devices = relationship('Device', back_populates='user')
    locations = relationship('Location', back_populates='user')
    messages = relationship('Message', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"