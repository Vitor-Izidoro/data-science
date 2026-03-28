def get_statistical_description(df):
    """Gera o sumário estatístico para a seção do artigo."""
    total_instances = len(df)
    total_features = 34  # Valor fixo conforme documentação
    num_classes = df['Target'].nunique()
    
    class_counts = df['Target'].value_counts()
    class_pct = df['Target'].value_counts(normalize=True) * 100

    print("\n## Statistical Description")
    print(f"Number of instances: {total_instances}")
    print(f"Number of features: {total_features}")
    print(f"Number of classes: {num_classes}")
    print("Class distribution:")
    for cls in class_counts.index:
        print(f"  - {cls}: {class_counts[cls]} ({class_pct[cls]:.2f}%)")