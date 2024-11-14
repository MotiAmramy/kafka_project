from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class HostageContent(Base):
    __tablename__ = 'suspicious_hostage_content'

    id = Column(Integer, primary_key=True)
    sentence = Column(String, nullable=False)
    sentence = relationship('Message', back_populates='suspicious_hostage_content')

    def __repr__(self):
        return f"<SuspiciousHostageContent(id={self.id}, message_id={self.message_id})>"