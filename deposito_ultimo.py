'''Este programa é uma simulação de um sistema de depósito de tintas com algumas classes e seus métodos executados por funções.'''
# Uma ideia é sincronizar o programa com o banco de dados "TinyDB". Vou procurar fazer depois.

class Tinta:
    def __init__(self, codigo, nome:str, cor:str, quantidade_peso:float, quantidade_estoque:int, preco:float, observacao=None):
        self.codigo = codigo
        self.nome = nome
        self.cor = cor
        self.quantidade_peso = quantidade_peso
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        self.observacao = observacao # A observacao é um atributo opcional, quando quiser basta passá-la como argumento ao criar uma instância da classe.

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}, Nome: {self.nome}, Cor: {self.cor}, Quantidade em litros: {self.quantidade_peso}, Quantidade no estoque: {self.quantidade_estoque}, Preço: {self.preco}")
        if self.observacao: # O método exibir_informacoes verifica se há uma observação antes de tentar imprimi-la.
            print(f"Observação: {self.observacao}")
    
    def listar_tintas(self):             # O método "listar tintas" é aqui dentro da classe Tinta?
        for tinta in self.tintas:
            print(f"Código: {tinta.codigo}, Nome: {tinta.nome}, Cor: {tinta.cor}, Quantidade: {tinta.quantidade}, Preço: {tinta.preco}")

class LojaDeTintas:
    def __init__(self):
        self.tintas = []

    def adicionar_tinta(self, tinta):
        self.tintas.append(tinta)

    def listar_tintas(self):             # Ou dentro da classe LojaDeTintas?
        for tinta in self.tintas:
            print(f"Código: {tinta.codigo}, Nome: {tinta.nome}, Cor: {tinta.cor}, Quantidade: {tinta.quantidade}, Preço: {tinta.preco}")

    def buscar_tinta_by_id(self, codigo):
        for tinta in self.tintas:
            if tinta.codigo == codigo:
                return tinta
        return None

    def atualizar_tinta_by_id(self, codigo, novo_nome, nova_cor, nova_quantidade, novo_preco):
        tinta = self.buscar_tinta_by_id(codigo)
        if tinta:
            tinta.nome = novo_nome
            tinta.cor = nova_cor
            tinta.quantidade = nova_quantidade
            tinta.preco = novo_preco
            print("Tinta atualizada com sucesso!")
        else:
            print("Tinta não encontrada.")

    def excluir_tinta_by_id(self, codigo):
        tinta = self.buscar_tinta_by_id(codigo)
        if tinta:
            self.tintas.remove(tinta)
            print("Tinta excluída com sucesso!")
        else:
            print("Tinta não encontrada.")

'''class CategoriaTinta:
    def __init__(self, categoria):
        self.categoria = categoria
        self.tintas = []

    def adicionar_tinta_categoria():
        ...'''

'''class Estoque:
    def __init__(self):
        self.tintas = []

    def exibir_estoque(self): ##
        print(f'Os produtos do estoque são: {self.tintas()}')

    def alterar_estoque_por_ID(self): ##
        self.codigo
        ...'''

class Cliente:
    def __init__(self, cpf:int, nome:str, endereco:str, email:str, telefone:float):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone


    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def listar_clientes(self):             # Ou dentro da classe LojaDeTintas?
        for cliente in self.clientes:
            print(f"Os clientes são: {cliente.cpf}, Nome: {cliente.nome}, Endereço: {cliente.endereco}, E-mail: {cliente.email}, Telefone: {cliente.telefone}")

    def buscar_cliente_by_id(self, cpf):
        for cliente in self.cliente:
            if cliente.cpf == cpf:
                return cliente
        return None

    def atualizar_cliente_by_id(self, codigo, novo_nome, nova_cor, nova_quantidade, novo_preco):
        tinta = self.buscar_tinta(codigo)
        if tinta:
            cli.nome = novo_nome
            cli.cor = nova_cor
            cli.quantidade = nova_quantidade
            cli.preco = novo_preco
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def excluir_cliente_by_id(self, cpf):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")

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
    
    def pesquisar_by_cargo():
        ...

class Fornecedor:
    def __init__(self, nome, contato, produtos_fornecidos):
        self.nome = nome
        self.contato = contato
        self.produtos_fornecidos = produtos_fornecidos

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedor.append(fornecedor)

class TransacaoCompra:
    def __init__(self, fornecedor, tinta, quantidade, data):
        self.fornecedor = fornecedor
        self.tinta = tinta
        self.quantidade = quantidade
        self.data = data

class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, tinta, quantidade): # Código?
        self.itens.append((tinta, quantidade))   # Coloca no "append" só o código ou todas as caracteríscticas?

class CupomDesconto:
    def __init__(self, codigo, desconto_percentual, data_validade):
        self.codigo = codigo
        self.desconto_percentual = desconto_percentual
        self.data_validade = data_validade

    '''def lancar_desconto():
        ...'''

loja = LojaDeTintas()
cli = Cliente()

# Exemplo de uso:
tinta_1 = Tinta(1, "Tinta Suvinil", "Azul", 5, 50, 10.99, "Essa tinta é resistente à água.")
tinta_2 = Tinta(2, "Tinta Aquanil", "Vermelho", 5, 30, 8.99)
tinta_3 = Tinta(3, "Tinta Coral", "Verde", 10, 50, 18.99)

cliente_1 = Cliente(42125452634, "Joao", "rua Estoril", "jonas@tmail.com", 1146798678967)
cliente_2 = Cliente(52125452634, "Maria", "rua dos Otoni", "marrie@umail.com", 5546798678967)
cliente_3 = Cliente(62125452634, "Serena", "rua Estoril", "serenity@kmail.com", 2146798678967)

loja.adicionar_tinta(tinta_1)
loja.adicionar_tinta(tinta_2)
loja.adicionar_tinta(tinta_3)

cli.adicionar_cliente(cliente_1)
cli.adicionar_cliente(cliente_2)
cli.adicionar_cliente(cliente_3)

loja.listar_tintas()
loja.atualizar_tinta_by_id(1, "Tinta C", "Yellow", 20, 20, 15.99)
loja.listar_tintas()
loja.excluir_tinta_by_id(2)
loja.listar_tintas()

cli.listar_clientes()
cli.atualizar_cliente_by_id(1, "Tinta C", "Yellow", 20, 20, 15.99)
cli.listar_clientes()
cli.excluir_cliente_by_id(2)
cli.listar_clientes()

class DepositoTintas:
    def __init__(self):
        # Inicializa o depósito com um dicionário vazio para armazenar as tintas e seus estoques
        self.estoque_tintas = {}

    def vender_tinta(self, nome_tinta, quantidade):
        # Vende uma quantidade específica de uma tinta do estoque
        if nome_tinta in self.estoque_tintas and quantidade <= self.estoque_tintas[nome_tinta]:
            self.estoque_tintas[nome_tinta] -= quantidade
            print(f'{quantidade} litros de {nome_tinta} vendidos.')
        elif nome_tinta not in self.estoque_tintas:
            print(f'Erro: A tinta {nome_tinta} não está no estoque.')
        else:
            print(f'Erro: Estoque insuficiente para vender {quantidade} litros de {nome_tinta}.')
    
    def verificar_estoque(self):
        # Retorna o estoque atual de todas as tintas
        return self.estoque_tintas

# Exemplo de uso
deposito_tintas = DepositoTintas()
print(deposito_tintas.verificar_estoque())
deposito_tintas.vender_tinta('Tinta Azul', 50)
print(deposito_tintas.verificar_estoque())
