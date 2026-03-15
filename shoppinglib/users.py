from .models import User


def user_exists(username):
    '''

    Verifica se um Usuario existe a partir de seu username/login

    :param username: Nome de usuario/login criado pelo cliente
    :return: o usuario caso exista ou None (vazio) caso não exista
    '''
    user = User.get_or_none(User.username == username)
    return user is not None


def create_user(username, password):
    '''
    Cria um usuario a partir de um username/login e password, caso o ususername/login não exista
    :param username: Nome de usuario/login a ser criado
    :param password: senha do usuario a ser criado
    :return: Retorna o usuario criado ou None(vazio) caso não tenha conseguido criar um usuario
    '''
    if not user_exists(username):
        return User.create(username=username, password=password)
    return None


def get_user_password(username):
    '''
    Busca a senha do usuario correspondente ao username/login no banco de dados
    :param username: Nome do usuario/login a buscar a senha
    :return: Retorna o password correspondente ao username/login
    '''

    user = User.get_or_none(User.username == username)

    if user:
        return user.password

    return None

