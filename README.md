# ETL de Usuários com Google Cloud BigQuery

Este projeto demonstra um processo de **ETL (Extract, Transform, Load)** utilizando o **Google Cloud BigQuery** para gerenciar dados de usuários. O objetivo é extrair dados de uma tabela de usuários no BigQuery, transformá-los (se necessário) e carregá-los em tabelas separadas para análise posterior.

## Funcionalidades

- **Extração de Dados**: O script extrai dados da tabela de usuários e da tabela de usuários ativos.
- **Transformação de Dados**: (Adicionar etapas de transformação, se necessário)
- **Carregamento de Dados**: Os dados extraídos são carregados em novas tabelas no BigQuery.

## Como funciona

O script possui as seguintes funcionalidades:

- **Extração de Dados de Todos os Usuários**: A função `extract_users()` extrai todos os dados da tabela de usuários no BigQuery.
- **Extração de Dados de Usuários Ativos**: A função `extract_active_users()` extrai apenas os usuários ativos, filtrando pela coluna `IsActive`.
- **Carregamento de Dados no BigQuery**: A função `load_data_to_table()` carrega os dados extraídos em novas tabelas no BigQuery, permitindo que esses dados sejam analisados separadamente.
- **Processo ETL**: Duas funções de ETL, `etl_all_users()` e `etl_active_users()`, executam o processo de extração e carregamento dos dados para as tabelas `TABLE_ALL_USERS_ETL` e `TABLE_ACTIVE_USERS_ETL`, respectivamente.

## Tecnologias Utilizadas

- **Google Cloud BigQuery**: Para armazenar e consultar os dados.
- **Pandas**: Para manipulação dos dados e conversão para o formato DataFrame.
- **python-dotenv**: Para carregar as variáveis de ambiente, como credenciais do Google Cloud e nomes das tabelas.

## Estrutura do Código

- **Carregamento de Credenciais**: O código carrega as credenciais do Google Cloud a partir de um arquivo JSON, utilizando a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`.
- **Consultas no BigQuery**: O código realiza consultas SQL para extrair dados da tabela `users` do BigQuery e filtrar usuários ativos.
- **Carregamento de Dados**: Os dados extraídos são carregados de volta no BigQuery em novas tabelas, o que pode ser útil para análises separadas.

## Requisitos

Este projeto requer Python 3.x. Para instalar as dependências, use o arquivo `requirements.txt` que lista todas as bibliotecas necessárias.

### Instalar Dependências

1. Clone o repositório:

```bash
git clone https://github.com/danilopinho75/etl-usuarios-bigquery.git
cd etl-usuarios-bigquery
```

2. Crie um ambiente virtual (opcional, mas recomendado)
```python
python3 -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

3. Instale as dependências do projeto:
```python
pip install -r requirements.txt
```
O arquivo requirements.txt contém as bibliotecas necessárias, como google-cloud, pandas e python-dotenv.

## Como Rodar o Projeto
### 1. Configuração inicial
Antes de rodar o script, você precisará configurar as credenciais do Google Cloud. Siga os passos abaixo:

- Crie um Service Account no Google Cloud e baixe o arquivo JSON com as credenciais.
- Defina a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS para o caminho do seu arquivo de credenciais:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
```
### 2. Variáveis de ambiente
O script utiliza algumas variáveis de ambiente que devem ser configuradas:

- BQ_TABLE_USERS: O nome da tabela de usuários no BigQuery.
- BQ_TABLE_ALL_USERS_ETL: O nome da tabela de destino para todos os usuários.
- BQ_TABLE_ACTIVE_USERS_ETL: O nome da tabela de destino para os usuários ativos.

Crie um arquivo <b>.env</b> na raiz do projeto e adicione as seguintes variáveis:

```
CREDENTIALS=/path/to/your/credentials.json
BQ_TABLE_USERS=your_project.your_dataset.users
BQ_TABLE_ALL_USERS_ETL=your_project.your_dataset.all_users_etl
BQ_TABLE_ACTIVE_USERS_ETL=your_project.your_dataset.active_users_etl
```

### 3. Executando o Script
Execute o script principal para rodar o processo de ETL:
```python
python main.py
```
O script irá extrair os dados dos usuários, transformá-los (se necessário) e carregar os dados nas tabelas de destino do BigQuery.
