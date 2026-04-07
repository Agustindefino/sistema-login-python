from shoppinglib.users import user_exists, create_user, get_user_password
from shoppinglib.shopping_list import ShoppingListManager

class App:

    def __init__(self):

        self.shopping = ShoppingListManager()

    def validate_login(self, login, password):

        if user_exists(login):

            senha_correta = get_user_password(login)

            if password == senha_correta:
                return True

        return False  # sempre retorna algo

    def register_user(self, username, password):

        if user_exists(username):
            print("Erro: usuário já existe.")
            return False

        if len(password) < 8:
            print("Erro: A senha deve ter pelo menos 8 caracteres.")
            return False

        if not any(letra.isupper() for letra in password):
            print("Erro: A senha deve conter pelo menos uma letra maiúscula.")
            return False

        if not any(caractere.isdigit() for caractere in password):
            print("Erro: A senha deve conter pelo menos um número.")
            return False

        # Se passou em todas as validações
        create_user(username, password)

        print("Usuário cadastrado com sucesso.")
        return True

    def create_list(self, name, market):

        self.shopping.create_list(name, market)

        print("Lista de comprar criada com sucesso.")

    def add_item(self, name, barcode, price, quantity):

        self.shopping.add_item(
            name=name,
            barcode=barcode,
            price=price,
            quantity=quantity
        )

        print("Item adicionado com sucesso.")

    def get_items(self):

        return self.shopping.get_items()

    def get_item_by_barcode(self, barcode):

        return self.shopping.get_item_by_barcode(barcode)
