#Importar o OpenAI mais recente:
from openai import OpenAI

#Importar o pandas para transformar o csv em leitura para o Python.
import pandas as pd

#Colocar a chave API do OpenAi (é necessário ter sua própria chave API, censuramos por motivos pessoais):
client = OpenAI(
    api_key="sua_chave_api"
)

#Ler o arquivo csv do meu computador, como ele estava dando erro inicialmente, tive que adicionar o enconding, pois não salvei como csv UTF-8.
df = pd.read_csv(r"C:\Users\natsu\Programação\Python\clientes_spa_antes.csv", encoding="latin1", sep=";")

#Utilizei a função para a OpenIA criar mensagens específicas com base na descrição e no tipo de cliente, depois especifiquei o que cada tipo de cliente significava.
#Foi utilizado o comando de return para retornar apenas o texto gerado pela IA.
def generate_message(cliente):
    response = client.responses.create(
        model="gpt-5-nano",
        input=f"""
Você trabalha em um hotel spa.

Crie uma mensagem personalizada para:
Nome: {cliente['nome']}
Preferência: {cliente['preferencia']}
Tipo de cliente: {cliente['tipo_cliente']}

Regras:
- VIP → oferecer benefício exclusivo
- Novo → dar boas-vindas
- Regular → convidar para retornar

Mensagem curta.
"""
    )

    return response.output_text


#Primeiro adicionamos um loop de lista vazia para armazenas as mensagens.
mensagens = []

#Para cada linha do excel, pegar os dados dos clientes, não deixar em forma de índice e sim separar as colunas por vírgula; e adicionar as mensagens para cada cliente.
for _, cliente in df.iterrows():
    mensagem = generate_message(cliente)
    mensagens.append(mensagem)

#Adicionar a nova coluna de "mensagens" no arquivo csv
df["mensagem"] = mensagens

#Para adicionar as novas informações no mesmo arquivo, porém o pandas cria automaticamente um index, como eu não queria isto, coloquei como false.
df.to_csv(r"C:\Users\natsu\Programação\Python\clientes_spa_depois.csv", index=False, encoding="latin1", sep=";")

#Caso o código seja bem sucedido e todas as operações sejam executadas com sucesso, aparecerá que as mensagens foram enviadas e teremos um novo arquivo com os dados anteriores e com as novas mensagens, ainda existindo o antigo arquivo csv.
print("Mensagens criadas!")
