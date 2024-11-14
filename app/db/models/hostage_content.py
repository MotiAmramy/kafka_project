from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class HostageContent(Base):
    __tablename__ = 'suspicious_hostage_content'

    id = Column(Integer, primary_key=True)
    sentence = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="hostage_content")


    def __repr__(self):
        return f"<HostageContent(id={self.id}, sentence={self.sentence}, user_id={self.user_id})>"