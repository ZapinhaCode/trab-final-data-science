# Tema do projeto 
Previsão de Temperatura Aparente a partir de Variáveis Climáticas (Análise de Dados Meteorológicos)

## URL do DataSet utilizado 
https://www.kaggle.com/datasets/muthuj7/weather-dataset?resource=download

## Dataset utilizado 
- **Origem:** Dataset de histórico do tempo para Szeged, Hungria (2006-2016), disponível no Kaggle.  
- **Descrição:** ~96 mil observações horárias com variáveis meteorológicas. Inclui colunas de data/hora, resumo do clima, tipo de precipitação (rain/snow/none), temperatura real (°C), temperatura aparente (°C), umidade (0-1), vento (km/h e direção), visibilidade (km), pressão (millibars), etc.  
- **Variáveis utilizadas no modelo:** Temperatura (C), Umidade, Resumo do tempo (Summary), Tipo de precipitação (Precip Type).  
- **Pré-processamento:** Remoção de colunas irrelevantes (ex: Loud Cover sempre zero), tratamento de missing values em Precip Type (substituídos por "none"), remoção de duplicatas, transformação de variáveis categóricas em dummies (one-hot encoding) e divisão treino/teste (80/20).

## Modelos utilizados/desenvolvidos 
- **Regressão Linear Múltipla:** Modelo linear para prever temperatura aparente a partir das variáveis selecionadas. Serviu como baseline pela simplicidade e interpretabilidade.  
- **Random Forest Regressor:** Modelo de ensemble de árvores de decisão, usado para capturar possíveis não-linearidades e interações complexas entre as variáveis.  
*(Obs.: Poderiam ser avaliados outros modelos de regressão como XGBoost, SVR, ou mesmo abordagens baseadas em fórmulas físicas, mas os dois acima foram suficientes neste projeto.)*

## Resultados obtidos 
- **Desempenho da Regressão Linear:** R² ≈ 0.987 no conjunto de teste (98.7% de variância explicada) e RMSE ≈ 1.2°C. O modelo praticamente reproduz a temperatura aparente com pequeno erro médio (~1°C).  
- **Desempenho do Random Forest:** R² ≈ 0.992 no teste (99.2% de variância explicada) e RMSE ≈ 0.98°C, mostrando leve melhoria.  
- **Análise:** Os resultados confirmam que a temperatura real é o fator dominante na sensação térmica. A inclusão de umidade e outras variáveis aprimora a previsão em casos extremos (calor úmido, frio ventoso). O modelo linear já alcança ótima performance, indicando relação quase linear entre as variáveis de entrada e o target.  
- **Validação:** O modelo foi validado em dados não vistos (20% teste) com excelente desempenho, indicando boa generalização. Uma validação cruzada k-fold também poderia ser conduzida para reforçar a confiabilidade.  
- **Conclusão:** É possível prever com alta acurácia a temperatura aparente usando aprendizado de máquina supervisionado neste dataset. O projeto demonstra todas as etapas de um workflow de Data Science, desde a exploração dos dados até a construção de um modelo preditivo confiável.
