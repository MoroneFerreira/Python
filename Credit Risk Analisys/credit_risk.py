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
#Verificando a distribuição de Idade
plt.hist(x=df['age']);

# %%
#Verificando a distribuição de Renda
plt.hist(x=df['income']);
# %%
#Verificando a distribuição de Divida
plt.hist(x=df['loan']);
# %%
#Gerando um gráfico dinâmico com plotly Express

grafico = px.scatter_matrix(df, dimensions=['age', 'income','loan'], color='default')
grafico.show()

#A partir deste plot, identifiquei que existe um padrão. Clientes mais jovens, até 35 anos tendem a não pagar os emprestimos
# %%
#Existem algumas formas de tratar os dados negativos:

#Pegando apenas os valores absolutos (removendo negativos) - Não garante que os dados estejam corretos.
#df['age'] = df['age'].abs()

#Neste caso, como seriam poucos registros, oderíamos também remover os dados com idades negativas da base com:
#df = df.drop(df[df['age']<=0].index)

#Por fim, acredito que a melhor forma seja substituir os valores negativos com a média das idades, tendenciando o modelo para o centro.
media_idades = df['age'][df['age']>=0].mean()
df.loc[df['age']<=0] = media_idades
# %%
#Checando se os valores negativos foram ajustados
df[df['age']<=0]
#%%
#teste
# %%
