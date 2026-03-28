import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import skew, kurtosis

def perform_univariate_analysis(df):
    """
    Realiza análise univariada e salva os gráficos na pasta 'analysis univariate plot'.
    """
    # 1. Criação da pasta caso não exista
    output_dir = "analysis univariate plot"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Diretório '{output_dir}' criado.")

    # Configuração de Estilo
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({'font.size': 10})

    # Mapeamentos do README (Chaves como inteiros)
    course_map = {
        33: 'Biofuel Production Tech.', 171: 'Animation & Multimedia', 
        8014: 'Social Service (Eve)', 9003: 'Agronomy',
        9070: 'Communication Design', 9085: 'Veterinary Nursing', 
        9119: 'Informatics Engineering', 9130: 'Equinculture',
        9147: 'Management', 9238: 'Social Service', 
        9254: 'Tourism', 9500: 'Nursing',
        9556: 'Oral Hygiene', 9670: 'Advertising & Marketing', 
        9773: 'Journalism', 9853: 'Basic Education',
        9991: 'Management (Eve)'
    }

    marital_map = {1: 'Single', 2: 'Married', 3: 'Widower', 4: 'Divorced', 5: 'Facto union', 6: 'Legally separated'}
    binary_map = {1: 'Yes', 0: 'No'}
    gender_map = {1: 'Male', 0: 'Female'}
    attendance_map = {1: 'Daytime', 0: 'Evening'}
    
    # Mapeamento de Nacionalidade (Top 5 conforme README)
    nat_map = {1: 'Portuguese', 41: 'Brazilian', 2: 'German', 6: 'Spanish', 11: 'Italian'}

    variables = [
        ('Marital status', 'cat', marital_map),
        ('Gender', 'cat', gender_map),
        ('Displaced', 'cat', binary_map),
        ('Debtor', 'cat', binary_map),
        ('Tuition fees up to date', 'cat', binary_map),
        ('Scholarship holder', 'cat', binary_map),
        ('Course', 'cat', course_map),
        ('Daytime/evening attendance', 'cat', attendance_map),
        ('Nacionality', 'cat', nat_map),
        ('International', 'cat', binary_map),
        ('Age at enrollment', 'num', None),
        ('Previous qualification (grade)', 'num', None),
        ('Admission grade', 'num', None),
        ('Curricular units 1st sem (enrolled)', 'num', None),
        ('Curricular units 1st sem (approved)', 'num', None),
        ('Curricular units 1st sem (grade)', 'num', None),
        ('Curricular units 2nd sem (approved)', 'num', None),
        ('Curricular units 2nd sem (grade)', 'num', None),
        ('Unemployment rate', 'num', None),
        ('GDP', 'num', None)
    ]

    for var, vtype, mapping in variables:
        if var not in df.columns:
            continue

        print(f"Processando: {var}")
        plt.figure(figsize=(10, 6))
        
        # Nome do arquivo limpo (sem caracteres especiais)
        filename = var.replace("/", "_").replace(" ", "_").lower()

        if vtype == 'num':
            data = df[var].dropna()
            sns.histplot(data, kde=True, color='teal', bins=20)
            plt.title(f"Distribuição: {var}")
            plt.xlabel("Valor")
        else:
            # Garante que os dados sejam tratados como numéricos antes do map
            temp_series = pd.to_numeric(df[var], errors='coerce')
            if mapping:
                plot_data = temp_series.map(mapping).fillna(temp_series.astype(str))
            else:
                plot_data = temp_series.astype(str)
            
            counts = plot_data.value_counts()
            sns.countplot(y=plot_data, order=counts.index, palette='viridis', hue=plot_data, legend=False)
            plt.title(f"Frequência: {var}")
            plt.xlabel("Contagem")
            plt.ylabel("")

        plt.tight_layout()
        
        # SALVAR EM VEZ DE MOSTRAR
        save_path = os.path.join(output_dir, f"{filename}.png")
        plt.savefig(save_path)
        plt.close() # Fecha a figura para liberar memória

    print(f"\nSucesso: 20 gráficos foram salvos na pasta '{output_dir}'.")