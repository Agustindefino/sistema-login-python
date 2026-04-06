from peewee import *
from datetime import datetime
from .database import db


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


class Item(BaseModel):
    name = CharField(max_length=120)
    bar_code = CharField(max_length=15, unique=True)


class ShoppingList(BaseModel):
    name = CharField()
    market = CharField()


class ShoppingListItem(BaseModel):
    shopping_list = ForeignKeyField(ShoppingList, backref="items")
    item = ForeignKeyField(Item)
    quantity = IntegerField()
    price = FloatField()


class PriceHistory(BaseModel):
    item = ForeignKeyField(Item, backref="history")
    price = FloatField()
    market = CharField()


if __name__ == '__main__':
    db.create_tables([User, Item, ShoppingListItem, ShoppingList, PriceHistory])

