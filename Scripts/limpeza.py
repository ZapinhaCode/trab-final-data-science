"""
limpeza.py
Funções para carregar, limpar e salvar o dataset de histórico do tempo.
"""
import os
import pandas as pd

# Carrega o dataset bruto, converte datas para UTC
def load_raw(path='../data/weatherHistory.csv') -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    df = pd.read_csv(path, parse_dates=['Formatted Date'])
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
    return df

# Limpa o DataFrame: remove colunas, duplicatas e trata valores ausentes
def clean(df: pd.DataFrame) -> pd.DataFrame:
    to_drop = ['Cloud Cover', 'Daily Summary']
    df = df.drop(columns=[c for c in to_drop if c in df], errors='ignore')
    df = df.drop_duplicates()
    df['Precip Type'] = df['Precip Type'].fillna('none')
    df = df.dropna(subset=['Formatted Date'])
    return df

# Salva o DataFrame limpo, garantindo que o diretório existe
def save(df: pd.DataFrame, path='data/weatherHistory_clean.csv') -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"✅ Dados limpos gravados em {path}")

if __name__ == "__main__":
    raw = load_raw()
    clean_df = clean(raw)
    save(clean_df)
    print(clean_df.head())  # Preview dos dados limpos