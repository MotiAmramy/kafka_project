from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from app.db.models import Base





class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(String(100), nullable=False)
    longitude = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='location')

    def __repr__(self):
        return f"<Location(id={self.id}, city={self.city}, country={self.country}, latitude={self.latitude}, longitude={self.longitude})>"