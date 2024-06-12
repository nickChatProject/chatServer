from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.models.db_connection.database import Base


class Company(Base):
    __tablename__ = 'organization_company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
