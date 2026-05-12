from sqlalchemy import create_engine

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///base.db')

class Base(DeclarativeBase):
    pass

class Servers(Base):
    __tablename__ = "servers"
