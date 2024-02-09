import atexit

import os

from sqlalchemy import Integer, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from dotenv import load_dotenv

load_dotenv()

PG_DSN = os.getenv('DSN')

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Subscrybers(Base):
    __tablename__ = 'subscrybers'

    id: Mapped[int] = mapped_column(primary_key=True)
    subscryber_number: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)

    @property
    def json(self):
        return {
            'id': self.id,
            'subscryber': self.subscryber_number,
        }


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

atexit.register(engine.dispose)
