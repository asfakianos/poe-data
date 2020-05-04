from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items2'

    id = Column(Integer, primary_key=True)
    league = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    item_type = Column(String)
    base_name = Column(String)
    # Log implicits and explicits as strings, with each mod separated by a ||
    implicits = Column(String)
    explicits = Column(String)
    price = Column(String)

    def imp_list(self):
        return self.implicits.split("||")

    def exp_list(self):
        return self.explicits.split("||")

    def price_in_c(self):
        # Hook this up to the csv dataset in some way
        pass

    def __repr__(self):
        return self.base_name, self.implicits, self.explicits, self.price

print(Item.__table__, " loaded")
