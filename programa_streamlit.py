import streamlit as st
from datetime import datetime

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

estoque = Estoque()
clientes = []
funcionarios = []
fornecedores = []

def main():
    st.title("Loja de Tintas")

    menu = st.selectbox("Selecione uma opção:", ["Adicionar Tinta", "Adicionar Cliente", "Realizar Venda", "Listar Tintas", "Listar Clientes", "Listar Funcionários", "Listar Fornecedores"])
    
    if menu == "Adicionar Tinta":
        st.header("Adicionar Tinta")
        cor = st.text_input("Cor:")
        marca = st.text_input("Marca:")
        preco = st.number_input("Preço:")
        quantidade = st.number_input("Quantidade em estoque:")
        if st.button("Adicionar"):
            nova_tinta = Tinta(cor, marca, preco, quantidade)
            estoque.tintas.append(nova_tinta)
            st.success("Tinta adicionada com sucesso!")

    elif menu == "Adicionar Cliente":
        st.header("Adicionar Cliente")
        nome = st.text_input("Nome:")
        endereco = st.text_input("Endereço:")
        email = st.text_input("Email:")
        telefone = st.text_input("Telefone:")
        if st.button("Adicionar"):
            novo_cliente = Cliente(nome, endereco, email, telefone)
            clientes.append(novo_cliente)
            st.success("Cliente adicionado com sucesso!")

    elif menu == "Realizar Venda":
        st.header("Realizar Venda")
        cliente_nome = st.text_input("Nome do Cliente:")
        tinta_cor = st.text_input("Cor da Tinta:")
        quantidade = st.number_input("Quantidade:")
        if st.button("Registrar Venda"):
            cliente = next((c for c in clientes if c.nome == cliente_nome), None)
            tinta = next((t for t in estoque.tintas if t.cor == tinta_cor), None)
            if cliente and tinta:
                venda = Venda(cliente, [(tinta, quantidade)], datetime.now())
                st.success("Venda registrada com sucesso!")

    elif menu == "Listar Tintas":
        st.header("Tintas em Estoque")
        for tinta in estoque.tintas:
            st.write(f"Cor: {tinta.cor}, Marca: {tinta.marca}, Preço: {tinta.preco}, Quantidade em Estoque: {tinta.quantidade}")

    elif menu == "Listar Clientes":
        st.header("Clientes")
        for cliente in clientes:
            st.write(f"Nome: {cliente.nome}, Endereço: {cliente.endereco}, Email: {cliente.email}, Telefone: {cliente.telefone}")

    elif menu == "Listar Funcionários":
        st.header("Funcionários")
        for funcionario in funcionarios:
            st.write(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario}")

    elif menu == "Listar Fornecedores":
        st.header("Fornecedores")
        for fornecedor in fornecedores:
            st.write(f"Nome: {fornecedor.nome}, Contato: {fornecedor.contato}, Produtos Fornecidos: {', '.join(fornecedor.produtos_fornecidos)}")

if __name__ == "__main__":
    main()