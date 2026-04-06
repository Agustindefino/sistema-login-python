from shoppinglib.users import *


class App:

    def __init__(self):
        self.user = None

    def validate_login(self, login, password):
        self.user = user_exists(login)
        if self.user and get_user_password(login) == password:
            return True
        self.user = None
        return False

    def register(self):
        while True:
            login = input('Digite o nome do Usuário:\t')
            if user_exists(login):
                print(f'Usuário {login} já existe')
                continue
            password = input('Digite o password:\t')
            self.user = create_user(login, password)
            break

    def get_login(self):
        while True:
            login = input('Digite o nome do Usuário:\t')
            password = input('Digite o password:\t')
            if self.validate_login(login, password):
                print(f'{self.user.username} logado com sucesso!')
            print(f'Usuário ou Senha Inválidos')

    def start(self):
        exit_app = False
        while not exit_app:
            if not self.user:
                response = input('Cadastrar digite C\nLogin digite L\nSair digite S')
                if response.lower() == 'c':
                    self.register()
                elif response.lower() == 'l':
                    self.get_login()
                elif response.lower() == 's':
                    exit_app = True
                else:
                    print(f'Você digitou {response}, digite uma das letras possíveis\n')
            else:
                response = input('Deslogar digite d\nSair digite S')
                if response.lower() == 'd':
                    self.user = None
                elif response.lower() == 's':
                    exit_app = True


app = App()
app.start()



