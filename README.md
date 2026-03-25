# ETL - Hotel Spa com OpenAI

Pipeline ETL em Python que extrai dados de clientes de um arquivo CSV, gera mensagens personalizadas utilizando a API da OpenAI com base nas preferências e tipo de cliente, e carrega os resultados em um novo arquivo CSV. O projeto demonstra a automação de comunicação personalizada por meio das etapas de Extract, Transform e Load.

## Estrutura do projeto

data/
- clientes_spa_antes.csv
- clientes_spa_depois.csv

etl_spa.py

## Como funciona

1. Extract: lê clientes_spa_antes.csv
2. Transform: gera mensagens com OpenAI
3. Load: salva em clientes_spa_depois.csv

## Tecnologias utilizadas

- Python
- Pandas
- OpenAI API
- CSV

## Exemplo

Entrada:
nome | preferencia | tipo_cliente

Saída:
nome | preferencia | tipo_cliente | mensagem
