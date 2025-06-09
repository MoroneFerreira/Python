Autor: Morone Paula Ferreira
LinkedIn: https://www.linkedin.com/in/moroneferreira/

# 🧠 Classificador de Risco de Crédito com Ajuste de Threshold

Este projeto de ciência de dados tem como objetivo construir um modelo preditivo para **identificar clientes com risco de inadimplência**, usando uma base de dados fictícia de crédito. A abordagem inclui **tratamento de dados, análise exploratória, treinamento de modelo supervisionado, avaliação e ajuste de threshold** para obter um modelo mais conservador — ideal para cenários de concessão de crédito.

---

## 📊 Base de Dados

A base `credit_data.csv` contém informações sobre clientes, incluindo:

- `clientid`: Identificador do cliente
- `income`: Renda mensal
- `age`: Idade
- `loan`: Valor do empréstimo
- `default`: Variável alvo (0 = pagou, 1 = não pagou)

---

## 🧼 Etapas de Pré-processamento

1. **Análise de dados faltantes e inválidos** (ex: idades negativas)
2. **Tratamento de valores ausentes (NaN)**
3. **Visualização da distribuição das variáveis**
4. **Análise de balanceamento da variável alvo**

---

## 📈 Análise Exploratória

Foram utilizadas bibliotecas como `matplotlib`, `seaborn` e `plotly` para identificar padrões visuais entre as variáveis. Foi observada, por exemplo, uma maior inadimplência entre clientes mais jovens.

---

## 🧠 Modelo Preditivo

- **Modelo utilizado**: Random Forest (`RandomForestClassifier`)
- **Divisão da base**: 80% treino | 20% teste
- **Métrica foco**: `Recall` para classe de inadimplência, por ser mais relevante em análise de risco
- **Avaliação original**:
  - Ótimos resultados, mas o modelo tende a aprovar muitos clientes (foco na precisão)

---

## ⚖️ Ajuste de Threshold

Em vez de manter o threshold padrão de 0.5, foi feita uma análise da **curva Precisão x Recall** para encontrar o ponto mais conservador possível — ou seja, onde conseguimos **detectar mais inadimplentes mesmo com algum sacrifício em precisão**.

**Threshold escolhido**: `0.35`, pois manteve precisão e recall altos para ambas as classes.

---

## 📊 Resultados Finais

Com o threshold ajustado para 0.35:

```text
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       343
           1       0.93      0.95      0.94        57

    accuracy                           0.98       400
   macro avg       0.96      0.97      0.96       400
weighted avg       0.98      0.98      0.98       400
