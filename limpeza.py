import pandas as pd

def limpar_dados(input_path='Data/weatherHistory.csv', output_path='Data/weatherHistory_clean.csv'):
    df = pd.read_csv(input_path)

    cols_remover = ['Loud Cover', 'Daily Summary']
    df.drop(columns=[c for c in cols_remover if c in df.columns], inplace=True)

    if 'Precip Type' in df.columns:
        df['Precip Type'] = df['Precip Type'].fillna('none')  # corrigido aqui

    df.drop_duplicates(inplace=True)

    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], errors='coerce', utc=True)
    df.dropna(subset=['Formatted Date'], inplace=True)

    df.to_csv(output_path, index=False)
    print(f"✅ Dados limpos salvos em: {output_path}")

if __name__ == "__main__":
    limpar_dados()
