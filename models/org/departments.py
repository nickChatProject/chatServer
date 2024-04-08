from sqlalchemy import Column, Integer, String, ForeignKey

from models.db_connection.database import Base


class Department(Base):
    __tablename__ = 'organization_department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    company_id = Column(Integer, ForeignKey('organization_company.id'))
