'''1 - 

Crie um programa que lê um arquivo CSV de logs de treinamento com a biblioteca pandas, calcule e exiba a média e o desvio padrão da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 

'''

import pandas as pd

def ler_e_calcular_estatisticas(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv)
        
        if 'tempo_execucao' not in df.columns:
            print("A coluna 'tempo_execucao' não foi encontrada no arquivo.")
            return
        
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()
        
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

arquivo = 'logs_treinamento.csv'  
ler_e_calcular_estatisticas(arquivo)
