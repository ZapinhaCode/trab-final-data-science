"""
analize.py
Análise exploratória e visualização de dados do histórico do tempo.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

PLOTS_DIR = "plots"

# Garante que o diretório de plots existe
def ensure_plots_dir():
    os.makedirs(PLOTS_DIR, exist_ok=True)

# Carrega o dataset limpo, lança erro se não encontrar o arquivo
def load_clean(path: str = "../data/weatherHistory_clean.csv") -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    df = pd.read_csv(path, parse_dates=["Formatted Date"])
    return df

# Imprime estatísticas descritivas numéricas e categóricas do DataFrame
def descriptive_stats(df: pd.DataFrame) -> None:
    print("\n--- Estatísticas Numéricas ---")
    print(df.describe())
    print("\n--- Estatísticas Categóricas ---")
    print(df.describe(include=["object"]))


# Plota histogramas das temperaturas real e aparente
def plot_temperature_distributions(df: pd.DataFrame) -> None:
    ensure_plots_dir()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(df['Temperature (C)'], bins=30, kde=True, ax=axes[0])
    axes[0].set(title="Distribuição: Temperature (°C)")
    sns.histplot(df['Apparent Temperature (C)'], bins=30, kde=True, ax=axes[1])
    axes[1].set(title="Distribuição: Apparent Temperature (°C)")
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTS_DIR, "dist_temperatures.png"))
    plt.close(fig)


# Plota histograma da diferença entre temperatura aparente e real
def plot_temp_delta(df: pd.DataFrame) -> None:
    df = df.copy()
    df['Temp Delta'] = df['Apparent Temperature (C)'] - df['Temperature (C)']
    ensure_plots_dir()
    plt.figure(figsize=(8,5))
    sns.histplot(df['Temp Delta'], bins=30, kde=True)
    plt.title("Distribuição da Diferença (Apparent - Real)")
    plt.xlabel("Temp Delta (°C)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "dist_temp_delta.png"))
    plt.close()


# Plota contagens das categorias de Precip Type e das 10 principais Summary
def plot_categorical_counts(df: pd.DataFrame) -> None:
    ensure_plots_dir()
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x='Precip Type', order=df['Precip Type'].value_counts().index)
    plt.title("Contagem por Precip Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "count_precip_type.png"))
    plt.close()

    top_summ = df['Summary'].value_counts().nlargest(10)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top_summ.values, y=top_summ.index)
    plt.title("Top 10 Summaries")
    plt.xlabel("Contagem")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "count_summary_top10.png"))
    plt.close()


# Plota série temporal da temperatura aparente agregada por frequência
def plot_time_series(df: pd.DataFrame, freq: str = 'D') -> None:
    ensure_plots_dir()
    freq_resample = 'ME' if freq == 'M' else freq
    ts = df.set_index('Formatted Date')['Apparent Temperature (C)'].resample(freq_resample).mean()
    plt.figure(figsize=(12,5))
    ts.plot()
    plt.title(f"Série Temporal: Temp Aparente ({freq} médio)")
    plt.xlabel("Data")
    plt.ylabel("Apparent Temperature (°C)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, f"timeseries_apparent_{freq}.png"))
    plt.close()


# Plota boxplots da temperatura aparente por mês e por hora do dia
def plot_seasonal_boxplots(df: pd.DataFrame) -> None:
    df = df.copy()
    if 'Month' not in df.columns:
        df['Month'] = df['Formatted Date'].dt.month
    if 'Hour' not in df.columns:
        df['Hour'] = df['Formatted Date'].dt.hour
    plt.figure(figsize=(10,5))
    sns.boxplot(x='Month', y='Apparent Temperature (C)', data=df)
    plt.title("Temp Aparente por Mês")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "boxplot_temp_by_month.png"))
    plt.close()
    plt.figure(figsize=(10,5))
    sns.boxplot(x='Hour', y='Apparent Temperature (C)', data=df)
    plt.title("Temp Aparente por Hora do Dia")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "boxplot_temp_by_hour.png"))
    plt.close()


# Plota mapa de calor da matriz de correlação das variáveis numéricas
def plot_correlation_matrix(df: pd.DataFrame) -> None:
    ensure_plots_dir()
    numeric_cols = ['Temperature (C)', 'Apparent Temperature (C)', 'Humidity',
                    'Wind Speed (km/h)', 'Visibility (km)', 'Pressure (millibars)']
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title("Matriz de Correlação")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "correlation_matrix.png"))
    plt.close()


# Executa todas as análises e gera os plots
def run_all():
    df = load_clean()
    descriptive_stats(df)
    plot_temperature_distributions(df)
    plot_temp_delta(df)
    plot_categorical_counts(df)
    plot_time_series(df, freq='D')
    plot_time_series(df, freq='M')
    plot_seasonal_boxplots(df)
    plot_correlation_matrix(df)


if __name__ == "__main__":
    ensure_plots_dir()
    run_all()