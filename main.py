from shoppinglib.users import user_exists, create_user, get_user_password
from shoppinglib.shopping_list import ShoppingListManager


class App:

    def __init__(self):

        self.shopping = ShoppingListManager()

    def validate_login(self, login, password):

        if not user_exists(login):
            return False

        saved_password = get_user_password(login)

        return saved_password == password

    def register_user(self, username, password):

        if user_exists(username):
            return False

        create_user(username, password)

        return True

    def create_list(self, name, market):

        return self.shopping.create_list(name, market)

    def add_item(self, name, barcode, price, quantity):

        return self.shopping.add_item(name, barcode, price, quantity)

    def get_items(self):

        return self.shopping.get_items()

    def get_item_by_barcode(self, barcode):
        items = self.get_items()
        for item in items:
            if item["barcode"] == barcode:
                return item
        return None

