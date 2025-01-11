from typing_extensions import Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from users_service.db.model import INTPK, STR50, Base



# set up mapped_column() overrides, using whole column styles that are
user_fk = Annotated[int, mapped_column(ForeignKey("user_account.id"))]


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[INTPK]
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    newProp: Mapped[str]
    
    