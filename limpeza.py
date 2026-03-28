import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_clean_data(file_path):
    try:
        # Carregamento silencioso
        df = pd.read_csv(file_path, sep=';')
    except FileNotFoundError:
        return None

    # 1. Encoding da variável alvo
    if 'Target' in df.columns:
        le = LabelEncoder()
        df['Target_Encoded'] = le.fit_transform(df['Target'])

    # 2. Definição das 34 features conforme o README
    categorical_features = [
        'Marital Status', 'Nacionality', 'Gender', 'Displaced', 
        'Educational special needs', 'Debtor', 'Tuition fees up to date', 
        'Scholarship holder', 'International', "Mother's qualification", 
        "Father's qualification", "Mother's occupation", "Father's occupation",
        'Application mode', 'Course', 'Daytime/evening attendance', 
        'Previous qualification'
    ]

    # Conversão para categórico (otimização e semântica de dados)
    for col in categorical_features:
        if col in df.columns:
            df[col] = df[col].astype('category')

    # 3. Normalização das variáveis contínuas
    continuous_features = [
        'Previous qualification (grade)', 'Admission grade', 
        'Curricular units 1st sem (grade)', 'Curricular units 2nd sem (grade)',
        'Unemployment rate', 'Inflation rate', 'GDP'
    ]
    
    scaler = StandardScaler()
    existing_continuous = [col for col in continuous_features if col in df.columns]
    
    if existing_continuous:
        # Cria colunas escalonadas sem remover as originais para análise
        scaled_cols = [f"{col}_scaled" for col in existing_continuous]
        df[scaled_cols] = scaler.fit_transform(df[existing_continuous])

    # Retorna apenas uma confirmação técnica curta
    print(f"Dataset processado: {df.shape[0]} registros e {df.shape[1]} colunas.")
    return df


df_limpo = load_and_clean_data("predict+students+dropout+and+academic+success/data.csv")

df_limpo.head(print(df_limpo.columns))

