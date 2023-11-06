class Tinta:
    def __init__(self, cor, marca, preco, quantidade):
        self.cor = cor
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade

class CategoriaTinta:
    def __init__(self, nome):
        self.nome = nome
        self.tintas = []

class Estoque:
    def __init__(self):
        self.tintas = []

class Cliente:
    def __init__(self, nome, endereco, email, telefone):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

class Venda:
    def __init__(self, cliente, tintas_vendidas, data):
        self.cliente = cliente
        self.tintas_vendidas = tintas_vendidas
        self.data = data

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Fornecedor:
    def __init__(self, nome, contato, produtos_fornecidos):
        self.nome = nome
        self.contato = contato
        self.produtos_fornecidos = produtos_fornecidos

class TransacaoCompra:
    def __init__(self, fornecedor, tinta, quantidade, data):
        self.fornecedor = fornecedor
        self.tinta = tinta
        self.quantidade = quantidade
        self.data = data

class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, tinta, quantidade):
        self.itens.append((tinta, quantidade))

class CupomDesconto:
    def __init__(self, codigo, desconto_percentual, data_validade):
        self.codigo = codigo
        self.desconto_percentual = desconto_percentual
        self.data_validade = data_validade