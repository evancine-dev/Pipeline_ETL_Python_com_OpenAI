# ETL - Hotel Spa com OpenAI

Este projeto implementa um pipeline ETL em Python que gera mensagens personalizadas para clientes de um hotel spa utilizando a API da OpenAI.

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

Saída:
nome | preferencia | tipo_cliente | mensagem
