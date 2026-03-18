
import peewee

db = peewee.SqliteDatabase('shopping.db')

class Usuario(peewee.Model):
    email = peewee.CharField(unique=True)
    senha = peewee.CharField()
    
    class Meta:
        database = db

db.connect()
db.create_tables([Usuario])


class App:

    def validate_login(self, login, password):
        try:
            usuario = Usuario.get(Usuario.email == login)
            return usuario.senha == password
        except Usuario.DoesNotExist:
            return False

    def register(self):
        print("Registrando novo usuário...")
        email = input("Digite seu email:")
        senha = input("Digite su senha:")
        
        if not email or not senha:
            print("Email e senha são obrigatórios.")
            return
        try:
            Usuario.create(email=email, senha=senha)
            print("Usuário registrado com sucesso!")
        except peewee.IntegrityError:
            print("Erro ao registrar usuário.")

    def get_login(self):
        print("faça login para acessar o sistema")
        email = input("Digite seu email:")
        senha = input("digite su senha:")
        if self.validate_login(email, senha):
            print("Login bem-sucedido!")
        else:
            print("Login falhou. Verifique suas credencias")


    def start(self):
         while True:
            print("\n=== SISTEMA ===")
            print("1. Cadastrar")
            print("2. Login")
            print("3. Sair")

            op = input("Escolha: ")

            if op == "1":
                self.register()
            elif op == "2":
                self.get_login()
            elif op == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")


app = App()
app.start()



