import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set(style="whitegrid")

# === Leitura dos dados ===
try:
    df = pd.read_csv('Data/weatherHistory_clean.csv')
except FileNotFoundError:
    print("❌ Arquivo 'Data/weatherHistory.csv' não encontrado.")
    sys.exit(1)
except Exception as e:
    print("❌ Erro ao ler o CSV:", e)
    sys.exit(1)

# === Conversão segura da data com tratamento de fusos ===
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], errors='coerce', utc=True)
before_drop = len(df)
df.dropna(subset=['Formatted Date'], inplace=True)
after_drop = len(df)

if not pd.api.types.is_datetime64_any_dtype(df['Formatted Date']):
    print("❌ A coluna 'Formatted Date' ainda não está no formato datetime.")
    sys.exit(1)

if before_drop != after_drop:
    print(f"⚠️ {before_drop - after_drop} registros com datas inválidas foram removidos.")

# === Funções de análise ===

def estatisticas_descritivas(data):
    print("\n📊 Estatísticas Descritivas:")
    print(data.describe(include='all'))


def plot_distribuicao_temperatura(data):
    plt.figure(figsize=(10, 5))
    sns.histplot(data['Temperature (C)'], bins=30, kde=True)
    plt.title("Distribuição da Temperatura (°C)")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()


def plot_precip_type(data):
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Precip Type', data=data)
    plt.title("Frequência por Tipo de Precipitação")
    plt.xlabel("Tipo de Precipitação")
    plt.ylabel("Contagem")
    plt.tight_layout()
    plt.show()


def temperatura_media_por_mes(data):
    data['Mes'] = data['Formatted Date'].dt.month
    medias = data.groupby('Mes')['Temperature (C)'].mean()
    plt.figure(figsize=(10, 5))
    medias.plot(marker='o')
    plt.title("Temperatura Média por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Temperatura Média (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_matriz_correlacao(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matriz de Correlação")
    plt.tight_layout()
    plt.show()


# === Execução das análises ===

if __name__ == "__main__":
    print("✅ Análise iniciada com sucesso.")
    print(f"Total de registros: {len(df)}")
    print(f"Tipo da coluna 'Formatted Date': {df['Formatted Date'].dtype}")

    estatisticas_descritivas(df)
    plot_distribuicao_temperatura(df)
    plot_precip_type(df)
    temperatura_media_por_mes(df)
    plot_matriz_correlacao(df)
