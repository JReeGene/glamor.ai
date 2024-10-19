from ...db.base_class import Base
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)      
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey("user.id"))  
    author = relationship("User", back_populates="blogs")