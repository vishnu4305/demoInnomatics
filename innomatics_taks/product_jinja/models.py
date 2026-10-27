from sqlalchemy import Column, Integer, String, Numeric, Text
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(50))
    stock = Column(Integer, default=0)
    image_url = Column(String(255))