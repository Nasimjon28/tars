from app.backand.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import CreateTable

class Task(Base):
    __tablename__='tasks'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str]
    contet: Mapped[str]
    priority: Mapped[int] = mapped_column(default=0)
    completed: Mapped[bool] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    user: Mapped['User'] = relationship(back_populates='tasks')

