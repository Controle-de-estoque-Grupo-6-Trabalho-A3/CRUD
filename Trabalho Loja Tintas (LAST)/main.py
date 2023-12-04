from database import Database
from models import Tinta, LojaDeTintas

db = Database('./banco.db')
loja = LojaDeTintas(db)
# cli = Cliente(db)

tinta_1 = Tinta(1, "Tinta Suvinil", "Azul", 5, 30, 20.99)
tinta_2 = Tinta(2, "Tinta Aquanil", "Vermelho", 5, 50, 14.99)
tinta_3 = Tinta(3, "Tinta Coral", "Verde", 10, 40, 18.99)

loja.adicionar_tinta(tinta_1)
loja.adicionar_tinta(tinta_2)
loja.adicionar_tinta(tinta_3)

tintas = loja.listar_tintas()
for tinta in tintas:
    print(tinta.codigo, tinta.nome, tinta.cor, tinta.quantidade_peso, tinta.quantidade_estoque, tinta.preco)

loja.atualizar_tinta_by_id(2, "Tinta Whitening", "Branca", 10, 30, 42.99)