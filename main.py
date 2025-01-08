import os
from google.cloud import bigquery
import pandas as pd
from dotenv import load_dotenv

# Carregar as variáveis de ambiente
load_dotenv()
credentials = os.getenv('CREDENTIALS')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials

# Configurar Tabelas
TABLE_USERS = os.getenv('BQ_TABLE_USERS')
TABLE_ALL_USERS_ETL = os.getenv('BQ_TABLE_ALL_USERS_ETL')
TABLE_ACTIVE_USERS_ETL = os.getenv('BQ_TABLE_ACTIVE_USERS_ETL')

# Cliente do Bigquery
client = bigquery.Client()


def extract_users():
    query_all_users = f"""
        SELECT *
        FROM {TABLE_USERS}
"""
    df_all_users = client.query(query_all_users).to_dataframe()
    return df_all_users

def extract_active_users():
    query_active_users = f"""
    SELECT
        *
    FROM {TABLE_USERS}
    WHERE IsActive = true
    """
    df_active_users = client.query(query_active_users).to_dataframe()
    print("Dados de usuários ativos extraídos com sucesso!")
    return df_active_users

def load_data_to_table(dataframe, table_name):
    job = client.load_table_from_dataframe(dataframe, table_name)
    job.result() #Aguarda a conclusão do job
    print(f"Dados carregados com sucesso na tabela `{table_name}`!")

def etl_all_users():
    print("Iniciando ETL de todos os usuários...")
    df_all_users = extract_users()
    load_data_to_table(df_all_users, TABLE_ALL_USERS_ETL)
    print("ETL de todos os usuários concluído...")

def etl_active_users():
    print("Iniciando ETL dos usuários ativos!")
    df_active_users = extract_active_users()
    load_data_to_table(df_active_users, TABLE_ACTIVE_USERS_ETL)
    print("ETL dos usuários ativos concluído!")

def main():
    etl_all_users()
    etl_active_users()

if __name__ == "__main__":
    main()
