from fastapi import FastAPI, HTTPException, status, Path
from apiTools import *
from data import lista_produtos

app = FastAPI(    
   title='Api Depósito de Tintas',
   version='0.0.1',
   description="Api com nome das tintas, suas respectivas características e outros itens do depósito.",
)

@app.get('/produtos',
        status_code=status.HTTP_200_OK,
        description='Retorna todos os produtos ou uma lista vazia.',
        summary='Retorna todos os clientes.'
        )
async def get_produtos():
    try:
        return lista_produtos
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Produtos não encontrados.'
    )

@app.get('/produto/{id}', status_code=status.HTTP_200_OK)
async def get_produto_id(id: int = Path(
    title='ID do produto',
    description=f'Deve ser de 1 a {len(lista_produtos)}',
    gt=1,
    lt=len(lista_produtos) + 1)
    ):
    try:
        resposta = get_by_id(id, lista_produtos)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Produto não encontrado.'
    )

@app.post('/produto-create', status_code=status.HTTP_201_CREATED)
async def create_produto(nome: str, cor: str, lavavel: bool):
    try:
        resposta = create_produto_new(nome, cor, lavavel, lista_produtos)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='Produto não criado.'
    )   

@app.put('/produto-update/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_produto(nome: str, cor: str, lavavel: bool, id: int):
    try:
        resposta = update_produto_by_id(nome, cor, lavavel, lista_produtos, id)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produto com o id:{id} não encontrado'
    )

@app.delete('/produto-delete/{id}', status_code=status.HTTP_200_OK)
async def delete_produto(id: int):
    try:        
        resposta = delete_produto_by_id(lista_produtos, id)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Produtos não encontrado com o id:{id}'
    )
