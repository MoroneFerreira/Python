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
df.loc[df['age']<=0, 'age'] = media_idades
# %%
#Checando se os valores negativos foram ajustados
df[df['age']<=0]
#%%
#Checando valores NAN
df.isnull().sum()
# %%
#Filtrando valores null
df.loc[pd.isnull(df['age'])]
# %%
#Preenchendo os valores NAN com a média de idades
df['age'] = df['age'].fillna(df['age'].mean())
# %%
#Checando se ainda existem valores nulos:
df.isnull().sum()

#%%
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve


# %%
#dividindo registros de treino e teste
#Vamos desconsiderar o ID por ser irrelevante nesta análise
X = df.drop(columns=['default','clientid'])
y = df['default']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42, test_size=0.2)

# %%
#gerando um primeiro modelo apenas com o random_state
classificador = RandomForestClassifier(random_state=42)
classificador.fit(X_train, y_train)

# %%
#Gerando predição
classificador.predict(X_test)
# %%
#Entendendo as métricas
y_pred = classificador.predict(X_test)
print(classification_report(y_test, y_pred))
#Nota-se que o Recall (quantidade ponderada de acertos reais) pode ser melhorado para os clientes que não pagaram o emprestimo.

# %%
#Por se tratar de um modelo de crédito, talvez seja mais interessante ajustar o Threshold, onde teremos uma abordagem mais conservadora.
#Com o ajuste do Threshold, tendencio o modelo a acusar mais clientes que não pagariam e negar o crédito (mesmo errando alguns), do que ganhar em precisão e deixar alguns pováveis inadimplentes passarem.

#Pegando as probabilidades de inadimplência:

y_scores = classificador.predict_proba(X_test)[:, 1]

# %%
#Seprarando os dados de Precisão, Recall e Thresholds
precision, recall, thresholds = precision_recall_curve(y_test, y_scores)
#%%
#plotando um gráfico para entender melhor a curva
plt.figure(figsize=(10, 6))
plt.plot(thresholds, precision[:-1], label='Precisão', color='blue')
plt.plot(thresholds, recall[:-1], label='Recall', color='green')
plt.xlabel('Threshold')
plt.ylabel('Valor')
plt.title('Precisão e Recall em função do Threshold')
plt.legend()
plt.grid(True)
plt.show()

#Com essa análise, entendemos que o ponto em que a precisão e sensibilidade de cruzam é com um Threshold de 0.4
#Quero optar por sensibilizar o modelo, ou seja, abrir mão de algumas aprovações para evitar prejuízo por inadimplência, sem perder muita precisão.
#Dado o gráfico, vou seguir com um Threshold de 0.35, mantendo tanto a precisão como o recall acima de 80% e abaixo dos 100%*
# %%
#Ajustando a previsao com base no Threshold
threshold = 0.35
y_pred_threshold = (y_scores >= threshold).astype(int)

# %%
#Cria uma nova predição de y considerando as métricas do modelo de não pagamento
#A regra entre parênteses retorna uma classificão booleana de y_scores
#O astype(int) transforma True = 1 e False = 0, retornando os valores na escala de 0 e 1 conforme base de atributos
y_pred_threshold = (y_scores >= threshold).astype(int)

# %%
#obtendo métricas do modelo com Threshold aplicado
print(classification_report(y_test, y_pred_threshold))
