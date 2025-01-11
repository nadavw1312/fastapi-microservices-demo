# declarative base from previous example
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from sqlalchemy.orm import mapped_column


STR50 = Annotated[str, 50]
# expected to be used in multiple places
INTPK = Annotated[int, mapped_column(primary_key=True)]

class Base(DeclarativeBase):
    type_annotation_map = {
        STR50: String(50),
    }

