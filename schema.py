from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Integer)  # Adjust this based on your precision needs
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    category = relationship("ProductCategory", backref="products")

# Define the database connection
engine = create_engine('sqlite:///example.db')

# Create the tables
Base.metadata.create_all(engine)
