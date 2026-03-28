import pandas as pd
from limpeza import load_and_clean_data
from estatisticas import get_statistical_description

def main():
    # Caminho do arquivo
    path = "predict+students+dropout+and+academic+success/data.csv"
    
    # Executa a limpeza
    df_limpo = load_and_clean_data(path)
    
    if df_limpo is not None:
        # Gera descrição para o artigo
        get_statistical_description(df_limpo)
        
        # Confirmação de colunas sem imprimir o dataframe completo
        print(f"\nTotal de colunas processadas: {len(df_limpo.columns)}")