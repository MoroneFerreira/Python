#%%
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# %%
#visualização inicial dos dados
df = pd.read_csv('credit_data.csv')
df
# %%
#Entendendo os tipos de dados da tabela
df.info()
# %%
#Breve resumo dos dados
df.describe()

# 3 registros sem idade preenchida e registro de idade com valor negativo
# %%
#Checando idades negativas
df[df['age']<=0]
# %%
#checando valores únicos da coluna "default"
np.unique(df['default'], return_counts=True)
# %%
#Plotando um gráfico para a coluna Default
sns.countplot(x=df['default'], palette='Greens_d')
#Se trata de uma base bem desbalanceada, o que pode tendenciar o modelo para definir o default em 0
# %%
plt.hist(x=df['age']);

# %%
