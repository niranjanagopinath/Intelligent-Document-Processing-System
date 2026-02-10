from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(Text)
    summary = Column(Text, nullable=True)
    category = Column(String, nullable=True)
    upload_date = Column(DateTime, default=datetime.utcnow)