from shoppinglib.users import user_exists, create_user, get_user_password
from shoppinglib.shopping_list import ShoppingListManager


class App:

    def __init__(self):

        self.shopping = ShoppingListManager()

    def validate_login(self, login, password):

        pass

    def register_user(self, username, password):

        pass

    def create_list(self, name, market):

        pass

    def add_item(self, name, barcode, price, quantity):

        pass

    def get_items(self):

        pass

    def get_item_by_barcode(self, barcode):
        pass

