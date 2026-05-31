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

if __name__ == "__main__":
    caminho_arquivo = "data/heart_disease.csv"
    
    df_bruto = load_and_inspect_data(caminho_arquivo)