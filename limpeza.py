import pandas as pd

# Leitura dos dados
df = pd.read_csv('weatherHistory.csv')

# Visão geral das primeiras linhas (amostra dos dados)
print(df.head(5))  # Exibe as primeiras 5 linhas do dataset

# Remover coluna irrelevante (Loud Cover) e Daily Summary que não será usada
df.drop(['Loud Cover', 'Daily Summary'], axis=1, inplace=True)

# Tratar valores ausentes em 'Precip Type': substituir NaN por 'none'
df['Precip Type'].fillna('none', inplace=True)

# Remover linhas duplicadas completas, se houver
df.drop_duplicates(inplace=True)

# Conversão da coluna de data para datetime
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'])

# Conferir resultado da limpeza
print("Dados após limpeza:")
print(f"Total de registros: {len(df)}")
print("Valores nulos por coluna:")
print(df.isnull().sum())
