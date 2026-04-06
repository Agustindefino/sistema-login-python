from shoppinglib.users import user_exists, create_user, get_user_password

class App:
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
