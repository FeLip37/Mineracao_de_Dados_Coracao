import pandas as pd
import os
import matplotlib.pyplot as plt 
import seaborn as sn 

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
        
    # One-Hot Encoding (Para categorias sem hierarquia)
    print("Aplicando One-Hot Encoding...")
    one_hot_cols = ['Gender', 'Smoking', 'Family Heart Disease', 'Diabetes', 'High Blood Pressure', 'Low HDL Cholesterol', 'High LDL Cholesterol']
    
    # Filtra apenas as colunas que realmente existem no dataset
    colunas_presentes = [col for col in one_hot_cols if col in df_encoded.columns]
    if colunas_presentes:
        df_encoded = pd.get_dummies(df_encoded, columns=colunas_presentes, drop_first=True)
        
    print("Transformação 100% concluída!")
    return df_encoded

if __name__ == "__main__":
    caminho_arquivo = "data/heart_disease.csv"
    
    # Inspeção 
    df_bruto = load_and_inspect_data(caminho_arquivo)
    
    # Transformação (Agora com Ordinal + One-Hot)
    df_transformado = transform_data(df_bruto)
    
    # Imprime as colunas para provar que o One-Hot Encoding funcionou
    print("\nLista de Colunas após o One-Hot Encoding:")
    print(list(df_transformado.columns))

def visualize_data(df):
    print("\n--- GERANDO VISUALIZAÇÕES ---")
    plot_dir = "plots"
    
    # Automação da criação do diretório de gráficos
    os.makedirs(plot_dir, exist_ok=True)

def visualize_data(df):
    print("\n--- GERANDO VISUALIZAÇÕES ---")
    plot_dir = "plots"
    os.makedirs(plot_dir, exist_ok=True)
    
    # Configuração do tamanho do gráfico
    plt.figure(figsize=(12, 10))
    
    # Seleção de colunas numéricas para o cálculo da correlação matemática
    cols_numericas = df.select_dtypes(include=['float64', 'int64', 'uint8', 'bool', 'int32'])
    corr = cols_numericas.corr()
    
    # Geração do Heatmap
    sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Heatmap de Correlação Matemática das Variáveis")
    plt.tight_layout()
    
    # Salvando o arquivo na pasta automatizada
    heatmap_path = os.path.join(plot_dir, "correlation_heatmap.png")
    plt.savefig(heatmap_path)
    plt.close()
    
    print(f"Heatmap de correlação matemático salvo com sucesso em: {heatmap_path}")

if __name__ == "__main__":
    caminho_arquivo = "heart_disease.csv" 
    
    # Inspeção 
    df_bruto = load_and_inspect_data(caminho_arquivo)
    
    # Tratamento de Nulos (Adicionado anteriormente)
    df_tratado = handle_missing_values(df_bruto)
    
    # Transformação (Ordinal + One-Hot)
    df_transformado = transform_data(df_tratado)
    
    # [NOVO] 4. Visualização de Dados (Geração do Heatmap)
    visualize_data(df_transformado)
    
    # Exportação do Dataset limpo
    output_file = "cleaned_heart_disease.csv"
    df_transformado.to_csv(output_file, index=False)
