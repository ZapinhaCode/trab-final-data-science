"""
modelagem.py
Treinamento e avaliação de modelos para previsão de temperatura aparente.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def load_data(path: str = '../data/weatherHistory_clean.csv') -> pd.DataFrame:
    """
    Carrega o dataset limpo, lança erro se não encontrar o arquivo
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    df = pd.read_csv(path, parse_dates=['Formatted Date'])
    return df


def prepare_features(df: pd.DataFrame):
    """
    Prepara features numéricas e categóricas (one-hot), retorna X e y
    """
    numeric_features = [
        'Temperature (C)', 'Humidity', 'Wind Speed (km/h)',
        'Visibility (km)', 'Pressure (millibars)'
    ]
    categorical_features = ['Summary', 'Precip Type']
    # Remove linhas com valores nulos nas colunas usadas
    df = df.dropna(subset=numeric_features + ['Apparent Temperature (C)'])
    df[categorical_features] = df[categorical_features].fillna('unknown')
    X_num = df[numeric_features]
    X_cat = pd.get_dummies(df[categorical_features], drop_first=True)
    X = pd.concat([X_num, X_cat], axis=1)
    y = df['Apparent Temperature (C)']
    print(f"Features shape: {X.shape}, Target shape: {y.shape}")
    return X, y


def split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42):
    """
    Separa X e y em conjuntos de treino e teste
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def evaluate_model(model, X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series):
    """
    Treina o modelo e imprime métricas de avaliação (RMSE e R2)
    """
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"{model.__class__.__name__} -> RMSE: {mse**0.5:.2f}, R2: {r2:.4f}")
    return mse, r2


def run_evaluation():
    """
    Executa todo o pipeline de modelagem e avaliação dos modelos
    """
    df = load_data()
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    print("\n--- Avaliação de Modelos ---")
    # Baseline Linear Regression
    lr = LinearRegression()
    evaluate_model(lr, X_train, X_test, y_train, y_test)

    # Random Forest leve para comparação
    rf = RandomForestRegressor(
        n_estimators=20,
        max_depth=10,
        random_state=42,
        n_jobs=1
    )
    evaluate_model(rf, X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    run_evaluation()