def get_by_id(id, lista_produtos):
    for produto in lista_produtos:
        if produto['id'] == id:
            return produto
        
def create_produto_new(nome, cor, lavavel, lista_produtos: list):
    new_produto = {
        'id': len(lista_produtos) + 1,
        'nome': nome,
        'cor': cor,
        'lavavel': lavavel,
    }
    lista_produtos.append(new_produto)
    return lista_produtos

def update_produto_by_id(nome, cor, lavavel, lista_produtos, id):
    for produto in lista_produtos:
        if produto['id'] == id:
            produto['nome']=  nome
            produto['cor']=  cor
            produto['lavavel']= lavavel
    
    return lista_produtos

def delete_produto_by_id(lista_produtos, id):
    lista_produtos.pop(id - 1)
    new_id = 0
    for produto in lista_produtos:
        new_id +=1
        produto['id'] = new_id
    
    return lista_produtos
