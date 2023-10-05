lista_alunos = [
    {
        'id': 1,
        'nome': 'Renato'
    },
    {
        'id': 2,
        'nome': 'Luciana'
    },
]

# CRUD

# post
# criar uma função que coloca a aluna joana(letra minúscula) na lista
aluna = 'joana'
def post_aluno(aluno: str):
    new_id = len(lista_alunos) + 1
    lista_alunos.append({
        'id': new_id,
        'nome': aluno
    })
    return lista_alunos

# print(post_aluno(aluna))
#  [{'id': 1, 'nome': 'Renato'}, {'id': 2, 'nome': 'Luciana'}, {'id': 3, 'nome': 'joana'}]

# read/get
# criar uma função que leia todos os alunos e imprima
def get_alunos(lista):
    return lista

# print(get_alunos(lista_alunos))
#  [{'id': 1, 'nome': 'Renato'}, {'id': 2, 'nome': 'Luciana'}, {'id': 3, 'nome': 'joana'}]

# read/get
# criar uma função que leia por id o aluno e imprima
def get_by_id(id: str):
    id_int = int(id) - 1
    return lista_alunos[id_int]

# print(get_by_id(3))

# put
# criar uma função que atualiza o nome joana na lista com a primeira letra maiúscula
def update_aluno(id: str, nome: str):
    id_int = int(id) -1
    aluno_update = lista_alunos[id_int]
    aluno_update['nome'] = nome
    return lista_alunos

print(update_aluno(3, 'Joana'))

# delete
# criar uma função que delete usando o id 
def delete_by_id(id: str):
    id_int = int(id)
    lista_alunos.pop(id_int-1)
    news_ids = 0

    # atualizar id
    for aluno in lista_alunos:
        news_ids += 1
        aluno['id'] = news_ids

    return lista_alunos
# print(lista_alunos)
# print(delete_by_id(2))
# [{'id': 1, 'nome': 'Renato'}, {'id': 3, 'nome': 'Joana'}]
