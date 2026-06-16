from app.db.session import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Click(Base):

    __tablename__ = "clicks"

    id = Column(Integer, primary_key=True, index= True)

    link_id = Column(Integer, ForeignKey("links.id"))

    created_at = Column(
        DateTime, 
        default=lambda: datetime.datetime.now(datetime.timezone.utc)
    )    

    user_agent = Column(String)

    ip_address = Column(String)    

    link = relationship("Link", back_populates="clicks")