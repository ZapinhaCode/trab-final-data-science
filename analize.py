import pandas as pd

# Leitura dos dados
df = pd.read_csv('weatherHistory.csv')



# Estatísticas descritivas das principais variáveis numéricas
print(df[['Temperature (C)', 'Apparent Temperature (C)', 'Humidity']].describe())

# Calcular correlação entre temperatura real, aparente, umidade e vento
corr_matrix = df[['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)']].corr()
print("Correlação entre variáveis selecionadas:")
print(corr_matrix)
