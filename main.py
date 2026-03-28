import pandas as pd
from limpeza import load_and_clean_data
from estatisticas import get_statistical_description
from analysis_univariate import perform_univariate_analysis

def main():
    path = "predict+students+dropout+and+academic+success/data.csv"
    
    # Carrega e limpa
    df = load_and_clean_data(path)
    
    if df is not None:
        # Mostra as colunas para conferência técnica
        print("Colunas prontas para análise:", df.columns.tolist())
        
        # Estatísticas
        get_statistical_description(df)
        
        # Análise Univariada
        perform_univariate_analysis(df)

if __name__ == "__main__":
    main()