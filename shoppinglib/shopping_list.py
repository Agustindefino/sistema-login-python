from shoppinglib.models import Item, ShoppingList, ShoppingListItem, PriceHistory


class ShoppingListManager:

    def create_list(self, name, market):

        return ShoppingList.create(
            name=name,
            market=market
        )

    def get_current_list(self):

        return (
            ShoppingList
            .select()
            .order_by(ShoppingList.created_at.desc())
            .first()
        )

    def add_item(self, name, barcode, price, quantity):

        current_list = self.get_current_list()

        if not current_list:
            raise Exception("Não foi criada lista de compras")

        item = Item.get_or_none(Item.bar_code == barcode)

        if not item:
            item = Item.create(
                name=name,
                bar_code=barcode
            )

        ShoppingListItem.create(
            shopping_list=current_list,
            item=item,
            quantity=quantity,
            price=price
        )

        PriceHistory.create(
            item=item,
            price=price,
            market=current_list.market
        )

    def get_items(self):

        current_list = self.get_current_list()

        if not current_list:
            return []

        items = []

        for entry in current_list.items:
        
            item = entry.item
            price = entry.price

            items.append({
                "name": item.name,
                "barcode": item.bar_code,
                "quantity": entry.quantity,
                "price": price,
                "total": price * entry.quantity
            })

        return items
    def get_item_by_barcode(self, barcode):

        current_list = self.get_current_list()

        if not current_list:
            return None

        for entry in current_list.items:

            if entry.item.bar_code == barcode:

                return {
                "name": entry.item.name,
                "barcode": entry.item.bar_code,
                "quantity": entry.quantity,
                "price": entry.price
            }

        return None
