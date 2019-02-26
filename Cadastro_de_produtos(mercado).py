class Produto:

    contador = 10000

    def __init__(self, nome, tipo, valor):

        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.id = Produto.contador + 1
        Produto.contador = self.id

produto = Produto(str(input("Nome:")), str(input('Tipo:')), str(input('Valor:')))

print(produto.__dict__)

x = str(input('Produto registrado , Deseja registrar outro?:'))

while x == 'sim' or x== 'Sim' or x== 's' or x == 'S':

    produto = Produto(str(input("Nome:")), str(input('Tipo:')), str(input('Valor:')))

    print(produto.__dict__)

    x = str(input('Produto registrado , Deseja registrar outro?:'))


