from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from app.db.models import Base






class ExplosiveContent(Base):
    __tablename__ = 'suspicious_explosive_content'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="explosive_content")


    def __repr__(self):
        return f"<ExplosiveContent(id={self.id}, message={self.sentence})>"
