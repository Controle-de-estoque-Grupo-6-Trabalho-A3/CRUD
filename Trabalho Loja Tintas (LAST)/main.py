from database import Database
from models import Tinta, LojaDeTintas

db = Database('./banco.db')
loja = LojaDeTintas(db)
# cli = Cliente(db)

tinta_1 = Tinta(1, "Tinta Suvinil", "Azul")
tinta_2 = Tinta(2, "Tinta Aquanil", "Vermelho")
tinta_3 = Tinta(3, "Tinta Coral", "Verde")

# loja.adicionar_tinta(tinta_1)
# loja.adicionar_tinta(tinta_2)
# loja.adicionar_tinta(tinta_3)

tintas = loja.listar_tintas()
for tinta in tintas:
    print(tinta.codigo, tinta.nome, tinta.cor)

'''
loja = LojaDeTintas()
client = ListaClientes()

# Exemplo de uso:
tinta_1 = Tinta(1, "Tinta Suvinil", "Azul", 5, 50, 10.99, "Essa tinta é resistente à água.")
tinta_2 = Tinta(2, "Tinta Aquanil", "Vermelho", 5, 30, 8.99)
tinta_3 = Tinta(3, "Tinta Coral", "Verde", 10, 50, 18.99)
loja.adicionar_tinta(tinta_1)
loja.adicionar_tinta(tinta_2)
loja.adicionar_tinta(tinta_3)

cliente_1 = Cliente(42125452634, "Joao", "rua Estoril", "jonas@tmail.com", 1146798678967)
cliente_2 = Cliente(52125452634, "Maria", "rua dos Otoni", "marrie@umail.com", 5546798678967)
cliente_3 = Cliente(62125452634, "Serena", "rua Estoril", "serenity@kmail.com", 2146798678967)
client.adicionar_cliente(cliente_1)
client.adicionar_cliente(cliente_2)
client.adicionar_cliente(cliente_3)

loja.get_tinta_by_id(2)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
loja.listar_tintas()
loja.atualizar_tinta_by_id(1, "Tinta C", "Yellow", 20, 20, 15.99)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
loja.listar_tintas()
loja.excluir_tinta_by_id(2)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
loja.listar_tintas()

client.listar_clientes()
client.atualizar_cliente_by_cpf(1, "Bruno", "rua das Margaridas", "bru@imail.com", 20159971843)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
client.listar_clientes()
client.excluir_cliente_by_cpf(62125452634)
print('NOVA ATUALIZAÇÂO NO SISTEMA')
client.listar_clientes()

# Pendente
Venda.vender_tinta('Tinta Coral', 10)

'''