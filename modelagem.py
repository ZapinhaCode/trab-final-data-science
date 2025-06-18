from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score




# Seleciona colunas de entrada (X) e alvo (y) para o modelo
features = ['Temperature (C)', 'Humidity', 'Summary', 'Precip Type']
target = 'Apparent Temperature (C)'

# Aplicar One-Hot Encoding nas variáveis categóricas
df_model = df[features + [target]].copy()
df_model = df_model.fillna({'Precip Type': 'none'})  # garantir nenhum NaN em Precip Type
# Converte categorias em dummies
df_model = pd.get_dummies(df_model, columns=['Summary', 'Precip Type'], drop_first=True)

X = df_model.drop(target, axis=1)
y = df_model[target]

# Dividir em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Tamanho treino: {X_train.shape[0]} exemplos, teste: {X_test.shape[0]} exemplos")




# Modelo 1: Regressão Linear
linreg = LinearRegression()
linreg.fit(X_train, y_train)  # Treina o modelo nos dados de treino

# Predição no conjunto de teste
y_pred_lin = linreg.predict(X_test)

# Avaliação do modelo linear
mse_lin = mean_squared_error(y_test, y_pred_lin)
rmse_lin = mse_lin ** 0.5
r2_lin = r2_score(y_test, y_pred_lin)
print(f"Desempenho Regressão Linear - RMSE: {rmse_lin:.3f} °C, R²: {r2_lin:.3%}")

# Modelo 2: Random Forest Regressor (exemplo de modelo de árvore de decisão em conjunto)
rf = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
rf.fit(X_train, y_train)

# Predição no teste
y_pred_rf = rf.predict(X_test)

# Avaliação do Random Forest
mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = mse_rf ** 0.5
r2_rf = r2_score(y_test, y_pred_rf)
print(f"Desempenho Random Forest - RMSE: {rmse_rf:.3f} °C, R²: {r2_rf:.3%}")
