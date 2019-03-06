from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:


    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'temos {cls.contador} usuario(s) no sistema ')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 200, salt_size = 10)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome__completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


nome = input('Nome:')
sobrenome = input('Sobrenome:')
email = input('email:')
senha = input('Senha:')
confirma_senha = input('Confirma a senha:')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha nao confere')
    exit()

print('Usuário criado com sucesso')

senha = input('Informe a senha para acesso:')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'senha user criptografada: {user._Usuario__senha}')

