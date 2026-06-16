from app.db.session import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

class Link(Base):

    __tablename__ = "links"

    id = Column(Integer, primary_key= True, index= True)

    original_url = Column(String)

    shorty_key = Column(String, index = True, unique = True)

    created_at = Column(
        DateTime, 
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )    

    clicks = relationship("Click", back_populates="link")