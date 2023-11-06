from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

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

class TransacaoCompra:
    def __init__(self, fornecedor, tinta, quantidade, data):
        self.fornecedor = fornecedor
        self.tinta = tinta
        self.quantidade = quantidade
        self.data = data

estoque = Estoque()
clientes = []
funcionarios = []
fornecedores = []

class TintaIn(BaseModel):
    cor: str
    marca: str
    preco: float
    quantidade: int

class ClienteIn(BaseModel):
    nome: str
    endereco: str
    email: str
    telefone: str

@app.post("/tintas/")
def criar_tinta(tinta: TintaIn):
    nova_tinta = Tinta(**tinta.dict())
    estoque.tintas.append(nova_tinta)
    return nova_tinta

@app.get("/tintas/{cor}")
def obter_tinta(cor: str):
    for tinta in estoque.tintas:
        if tinta.cor == cor:
            return tinta
    return {"erro": "Tinta não encontrada"}

@app.post("/clientes/")
def criar_cliente(cliente: ClienteIn):
    novo_cliente = Cliente(**cliente.dict())
    clientes.append(novo_cliente)
    return novo_cliente

@app.get("/clientes/{nome}")
def obter_cliente(nome: str):
    for cliente in clientes:
        if cliente.nome == nome:
            return cliente
    return {"erro": "Cliente não encontrado"}

@app.post("/vendas/")
def criar_venda(venda: Venda):
    # Implemente a lógica para processar uma venda aqui
    return venda

@app.get("/funcionarios/")
def listar_funcionarios():
    return funcionarios

@app.post("/funcionarios/")
def criar_funcionario(funcionario: Funcionario):
    funcionarios.append(funcionario)
    return funcionario

@app.get("/fornecedores/")
def listar_fornecedores():
    return fornecedores

@app.post("/fornecedores/")
def criar_fornecedor(fornecedor: Fornecedor):
    fornecedores.append(fornecedor)
    return fornecedor

@app.post("/realizar-compra/")
def realizar_compra(fornecedor, tinta, quantidade, data):  # (transacao: TransacaoCompra)
    transacao = TransacaoCompra(fornecedor, tinta, quantidade, data)
    
    # Verificar se a tinta está no estoque
    for t in estoque.tintas:
        if t.cor == tinta.cor:
            t.quantidade += quantidade
            break
    else:
        # Se a tinta não estiver no estoque, adicioná-la
        tinta.quantidade = quantidade
        estoque.tintas.append(tinta)
    
    return transacao