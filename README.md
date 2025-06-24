# Previsão de Temperatura Aparente 🌡️

Repositório do Projeto de Data Science do curso CCC269 – UPF, orientado pelo Prof. Dr. Carlos Amaral Hölbig ([holbig@upf.br](mailto:holbig@upf.br)). Este projeto tem como objetivo prever a **Temperatura Aparente** (feels-like) utilizando dados climáticos históricos de Szeged, Hungria (2006–2016).

---

## 📂 Estrutura do Repositório

```
trab-final-data-science/
│
├─ Data/
│   ├─ weatherHistory.csv         # Dataset original
│   └─ weatherHistory_clean.csv   # Versão limpa após pré-processamento
│
├─ env/                           # Ambiente virtual (pasta local, opcional)
│
├─ Scripts/
│   ├─ limpeza.py                 # Carregamento e limpeza de dados
│   ├─ analize.py                 # Exploração de dados e visualizações
│   └─ modelagem.py               # Preparação de features, treino e avaliação de modelos
│
├─ README.md                      # Descrição do projeto e instruções
└─ WeatherHistoryNotebook.ipynb   # Notebook Jupyter autônomo com todo o pipeline
```

---

## 💾 Fonte do Dataset

* **Kaggle**: [muthuj7/weather-dataset](https://www.kaggle.com/datasets/muthuj7/weather-dataset?resource=download) – Historical Hourly Weather Data de Szeged, Hungria, abrangendo 2006–2016 (\~96.000 registros).

---

## 🔍 Descrição dos Arquivos

* **Data/weatherHistory.csv**
  Conjunto de dados original (.csv) com registros horários de variáveis climáticas.

* **Data/weatherHistory\_clean.csv**
  Arquivo gerado pelo script `limpeza.py`, após pré-processamento (datas em UTC, remoção de colunas e tratamento de nulos).

* **Scripts/limpeza.py**
  Funções para carregar o CSV bruto, parse de datas, remoção de colunas irrelevantes, tratamento de valores faltantes e duplicatas.

* **Scripts/analize.py**
  Rotinas de Análise Exploratória de Dados (EDA): estatísticas descritivas, histogramas de temperatura, countplots, séries temporais, boxplots sazonais e matriz de correlação.

* **Scripts/modelagem.py**
  Pipeline de modelagem: preparação de features (numéricas + one-hot encoding), split treino/teste, avaliação de Linear Regression (baseline) e Random Forest.

* **WeatherHistoryNotebook.ipynb**
  Notebook Jupyter standalone: percorre todas as etapas (limpeza, EDA, modelagem) diretamente no ambiente do notebook.


---

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/ZapinhaCode/trab-final-data-science.git
   ```
2. Acesse a pasta do projeto:

   ```bash
   cd trab-final-data-science
   ```
3. (Opcional) Configure o ambiente virtual:

   ```bash
   python -m venv env
   source env/bin/activate   # Linux/macOS
   .\\env\\Scripts\\activate  # Windows
   ```
4. Instale as dependências:

   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
5. Abra e execute o notebook:

   ```bash
   jupyter lab WeatherHistoryNotebook.ipynb
   ```

---

## 🏷️ Autores

* **Romeu Maia** (120206)
* **Bernardo Zaparoli** (189797)
* **Guilherme Di Domenico** (188997)

---

