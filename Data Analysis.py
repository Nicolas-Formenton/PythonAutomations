#Criar um roteiro
#Passo 1: Importar a base de dados
from numpy import column_stack
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.csv")

#Passo 2: Visualizar a base de dados
""" Entender as informaçoes que voce tem disponivel
Descobrir as cagadas da base de dados """
#informaçoes que não te ajudam, te atrapalham!

tabela = tabela.drop("Unnamed: 0", axis=1)
tabela = tabela.drop("Codigo", axis=1)
print(tabela)

#Passo 3: Tratamento de Dados (resolver os b.o's)
#Informaçoes do tipo CORRETO - Ajustar o TOTALGASTO(object to int/float)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = "coerce") #coerce = forçar p sobrescrever

#Procurar Informaçoes (VAZIAS, ERRADAS, ETC)
#COLUNA completamente vazia -> Excluir
tabela = tabela.dropna(how="all", axis=1)

#LINHA que tem alguma informaçao vazia -> Excluir
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

#Passo 4: Análise Inicial dos Dados

""" Como estão os cancelamentos? [26%(?)] | Coluna CHURN """
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))

#Passo 5: Descobrir motivos do cancelamento
print(tabela.columns)

for coluna in tabela.columns:
    #Etapa 1: criar o gráfico
    graph = px.histogram(tabela, x=coluna,color="Churn", text_auto=True)
    #Etapa 2: Exibe o gráfico
    graph.show()