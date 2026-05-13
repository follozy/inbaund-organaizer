from sqlalchemy import create_engine

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///base.db', echo=True)

class Base(DeclarativeBase):
    pass

class Servers(Base):
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(primary_key=True)
    IPv4: Mapped[str] = mapped_column(String(15))
    port: Mapped[int]
    pubKey: Mapped[str]
    mldsa65Verify: Mapped[str]
    shortIDs: Mapped[str]
    uTLS: Mapped[str]
    SNI: Mapped[str]
    Target: Mapped[str]
    security: Mapped[str]
    fingerprint: Mapped[str]

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tgid: Mapped[int]
    uuid: Mapped[str]
    flow: Mapped[str]
    email: Mapped[str]
    enable: Mapped[bool]
    created: Mapped[int]
    lustupdate: Mapped[int]
    tarif: Mapped[str] = "white"


Base.metadata.create_all(engine)

def take_engine():
    return engine