from database import Database

class Tinta:
    def __init__(self, codigo, nome:str, cor:str, quantidade_peso:float, quantidade_estoque:int, preco:float):
        self.codigo = codigo
        self.nome = nome
        self.cor = cor
        self.quantidade_peso = quantidade_peso
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco

class LojaDeTintas:
    def __init__(self, db: Database):
        self.db = db
        self.__criar_tabela_tinta()
    
    def __criar_tabela_tinta(self):
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS tintas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                cor VARCHAR(255) NOT NULL,
                quantidade_peso VARCHAR(255) NOT NULL,
                quantidade_estoque VARCHAR(255) NOT NULL,
                preco VARCHAR(255) NOT NULL
            ) ''')

    def adicionar_tinta(self, tinta:Tinta):
        self.db.execute('''
            INSERT INTO tintas (nome, cor, quantidade_peso, quantidade_estoque, preco)
            VALUES (?, ?, ?, ?, ?)
        ''', tinta.nome, tinta.cor, tinta.quantidade_peso, tinta.quantidade_estoque, tinta.preco)

    def listar_tintas(self) -> list[Tinta]:
        tintas_tuplas = self.db.get_all('SELECT * FROM tintas')

        tintas = []
        for tinta in tintas_tuplas:
            tintas.append(Tinta(tinta[0], tinta[1], tinta[2], tinta[3], tinta[4], tinta[5]))
        return tintas

    def atualizar_tinta_by_id(self, id, nome, cor, quantidade_peso, quantidade_estoque, preco):
        self.db.execute('''
            UPDATE tintas 
            SET nome = ?, cor = ? , quantidade_peso = ?, quantidade_estoque = ?, preco = ?
            WHERE id = ?"
        ''', id, nome, cor, quantidade_peso, quantidade_estoque, preco)

    def excluir_tinta_by_id(self, codigo):
        '''tinta = self.buscar_tinta_by_id(codigo)
        if tinta:
            self.tintas.remove(tinta)
            print("Tinta excluída com sucesso!")
        else:
            print("Tinta não encontrada.")'''