import pandas as pd

def load_and_inspect_data(filepath):
    print("--- INICIANDO INSPEÇÃO DE DADOS ---")
    df = pd.read_csv(filepath)
    
    print(f"Total de Linhas: {len(df)}")
    print(f"Total de Colunas: {len(df.columns)}")
    
    print("\n--- PERCENTUAL DE VALORES NULOS (%) ---")
    null_percent = (df.isnull().sum() / len(df)) * 100
    print(null_percent[null_percent > 0].round(2))
    
    return df

def transform_data(df):
    print("\n--- INICIANDO TRANSFORMAÇÃO (ENCODING) ---")
    df_encoded = df.copy()
    
    # Ordinal Encoding (Para categorias com hierarquia)
    print("Aplicando Ordinal Encoding...")
    ordinal_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    ordinal_cols = ['Exercise Habits', 'Alcohol Consumption', 'Stress Level', 'Sugar Consumption']
    
    for col in ordinal_cols:
        if col in df_encoded.columns:
            df_encoded[col] = df_encoded[col].map(ordinal_mapping)
            
    # Transformar a variável alvo (Doença Cardíaca) em 0 e 1
    if 'Heart Disease Status' in df_encoded.columns:
        df_encoded['Heart Disease Status'] = df_encoded['Heart Disease Status'].map({'No': 0, 'Yes': 1})
        
    print("Ordinal Encoding concluído!")
    return df_encoded

if __name__ == "__main__":
    caminho_arquivo = "data/heart_disease.csv"
    
    # 1. Inspeção 
    df_bruto = load_and_inspect_data(caminho_arquivo)
    
    # 2. Transformação (Apenas Ordinal por enquanto)
    df_transformado = transform_data(df_bruto)
    
    print("\nExemplo após Ordinal Encoding (Stress Level e Target):")
    print(df_transformado[['Stress Level', 'Heart Disease Status']].head())