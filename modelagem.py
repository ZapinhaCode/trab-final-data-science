import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def carregar_dados(path='Data/weatherHistory_clean.csv'):
    df = pd.read_csv(path)
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
    return df

def preparar_dados(df):
    # Seleciona colunas que serão usadas como features
    # Exemplo simplificado: usar 'Humidity', 'Wind Speed (km/h)', 'Visibility (km)', 'Pressure (millibars)'
    features = ['Humidity', 'Wind Speed (km/h)', 'Visibility (km)', 'Pressure (millibars)']
    target = 'Temperature (C)'

    # Remove linhas com valores nulos nessas colunas
    df = df.dropna(subset=features + [target])

    X = df[features]
    y = df[target]
    return X, y

def treinar_modelo(X, y):
    # Divide em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instancia e treina regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Faz predições no teste
    y_pred = model.predict(X_test)

    # Avaliação
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"R^2 Score: {r2:.4f}")

    return model

if __name__ == "__main__":
    print("🔍 Carregando dados...")
    df = carregar_dados()

    print("⚙ Preparando dados para modelagem...")
    X, y = preparar_dados(df)

    print("📈 Treinando modelo...")
    model = treinar_modelo(X, y)
