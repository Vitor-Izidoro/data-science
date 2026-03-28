import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_clean_data(file_path):
    try:
        # O quotechar='"' trata as aspas que aparecem no seu CSV
        df = pd.read_csv(file_path, sep=';', quotechar='"')
        
        # Limpeza agressiva: remove espaços extras e aspas remanescentes
        df.columns = df.columns.str.replace('"', '').str.strip()
        
        print(f"Dataset processado: {df.shape[0]} registros e {df.shape[1]} colunas.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

    # 1. Encoding da variável alvo
    if 'Target' in df.columns:
        le = LabelEncoder()
        df['Target_Encoded'] = le.fit_transform(df['Target'])

    # 2. Tipagem de Categóricas
    # Usamos nomes simples aqui, pois a limpeza acima já padronizou
    categorical_features = [
        'Marital status', 'Nacionality', 'Gender', 'Displaced', 
        'Educational special needs', 'Debtor', 'Tuition fees up to date', 
        'Scholarship holder', 'International', 'Course', 
        'Daytime/evening attendance', 'Previous qualification'
    ]

    for col in categorical_features:
        if col in df.columns:
            df[col] = df[col].astype('category')

    # 3. Normalização
    continuous_features = [
        'Previous qualification (grade)', 'Admission grade', 
        'Curricular units 1st sem (grade)', 'Curricular units 2nd sem (grade)',
        'Unemployment rate', 'Inflation rate', 'GDP'
    ]
    
    scaler = StandardScaler()
    existing_continuous = [col for col in continuous_features if col in df.columns]
    if existing_continuous:
        scaled_cols = [f"{col}_scaled" for col in existing_continuous]
        df[scaled_cols] = scaler.fit_transform(df[existing_continuous])

    return df

