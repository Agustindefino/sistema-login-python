from shoppinglib.users import user_exists, create_user, get_user_password
from shoppinglib.shopping_list import ShoppingListManager

class App:
<<<<<<< HEAD

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
=======
    #def __init__(self): pass
    def validate_login(self, email_digitado):
        if user_exists(email_digitado): 
            return True
        else:
            return False

    def register(self):
        print("--- CADASTRO ---")
        email: str = ""
        while not email:
            email = input("Digite seu email: ")
            
        if user_exists(email):
            print("Erro: Este email já está cadastrado!")
            email = ""
        else:
            senha = input("Crie uma senha: ")
            create_user(email, senha)
            print("Cadastro feito com sucesso!")

    def get_login(self):
        print("--- LOGIN ---")
        email = input("Digite seu email: ")
        senha_digitada = input("Digite sua senha: ")

        if user_exists(email): 
            senha_correta = get_user_password(email)
            if senha_digitada == senha_correta:
                print("Login feito com sucesso! Bem-vindo(a).")
            else:
                print("Erro: Senha incorreta.")
        else:
            print("Erro: Email não encontrado. Por favor, cadastre-se primeiro.")

    def start(self):
        while True:
            print("\n=== SISTEMA DE ACESSO ===")
            print("1. Cadastrar novo usuário")
            print("2. Fazer Login")
            print("3. Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.register()
            elif opcao == "2":
                self.get_login()
            elif opcao == "3":
                print("Indo embora...tchauu :D")
                break
            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    app = App()
    app.start()
>>>>>>> 7d3efd4caa81061990185776ad908204f20b3c72
