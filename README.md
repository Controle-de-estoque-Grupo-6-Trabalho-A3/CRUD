Baixar o arquivo “main”, “apiTools” e ‘data’.

Comandos do terminal:
python -m venv env
cd env
\Scripts\activate
Set-ExecutionPolicy Unrestricted -Force (caso de erro)
Set-ExecutionPolicy  -Scope CurrentUser  -ExecutionPolicy RemoteSigned
Caso o erro persista, ir até o power shell (azul claro) e executar os comandos acima.
.\\Scripts\activate
python -m pip install -U fastapi
python -m pip install uvicorn
uvicorn main:app --reload
OBS: os três arquivos após criados devem ser inseridos dentro da pasta "env" criada.

Após a execução dos códigos, colocar um “/docs” no final do seu endereço HTTP.
Ex: http://127.0.0.1:8000/docs

Para criar um novo botão em html (aula 4), crie um novo arquivo ‘html’ com o nome desejado mudando o meio 
({% for dado in ‘’organized_desc_deaths’’ %}).

Defina a sua função em ‘apiTools’.

Atualize o main com o “get/set/update/delete” desejado. Mudando o endereço da URL e dando referenciando.
