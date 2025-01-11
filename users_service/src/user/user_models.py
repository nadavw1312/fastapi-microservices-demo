from src.db.model import INTPK, Base
from typing_extensions import Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column




# set up mapped_column() overrides, using whole column styles that are
USER_FK = Annotated[int, mapped_column(ForeignKey("user_account.id"))]


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[INTPK]
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    newProp: Mapped[str]
    
    