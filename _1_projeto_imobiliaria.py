# -*- coding: utf-8 -*-
"""#1 Projeto_imobiliaria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1okWOdDy2o_PqYHHjICcsPaxzP1VToXbt

# Conhecendo a base de dados

## Importando os dados
"""

import pandas as pd

url  = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)

url  = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url, sep=';') #,sep é utilização para separação de virgula

dados = pd.read_csv(url, sep=';')
dados

dados.head(10)

dados.tail()

type(dados) #type ajuda vê que tipo dado é

"""## Características gerais da base de dados"""

dados.shape

dados.columns

dados.info()

dados['Tipo']

dados[['Quartos','Valor']]

"""# Análise exploratória de dados

## Qual o valor médio de aluguel por tipo de imóvel?
"""

dados.head()

dados['Valor'].mean() #mean é a media

dados.groupby('Tipo').mean(numeric_only=True) #método groupby #numeric_only utiliza para ocorrer especificamente em dados númericos

dados.groupby('Tipo')['Valor'].mean()

dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
#transformamos em dataframe e ordemanos do menor para maior

df_preco_tipo = dados.groupby('Tipo').mean()[['Valor']].sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize=(14, 10), color ='purple');

"""## Removendo os imóveis comerciais"""

dados.Tipo.unique()

imoveis_comerciais = ['Conjunto Comercial/Sala',  # listas dados que queremos remover
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

dados.query('@imoveis_comerciais in Tipo') #query condição

dados.query('@imoveis_comerciais not in Tipo')

df = dados.query('@imoveis_comerciais not in Tipo')
df.head()

df.Tipo.unique()

df_preco_tipo = df.groupby("Tipo").mean()[["Valor"]].sort_values("Valor")

df_preco_tipo.plot(kind='barh', figsize=(14, 10), color ='purple');

"""## Qual o percentual de cada tipo de imóvel na nossa base de dados?"""

df.Tipo.unique()

df.Tipo.value_counts(normalize=True) #contar valores

df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color ='green', edgecolor='black',
                        xlabel = 'Tipos', ylabel = 'Percentual');

"""### **Selecionando apenas os imóveis do tipo apartamento**"""

df.query('Tipo == "Apartamento"')

df.query('Tipo == "Apartamento"')
df.head()

"""# Tratando e filtrando os dados

## Lidando com dados nulos
"""

df.isnull() #analisar dados  nulos ou não

df.isnull().sum()

df.fillna(0)

df = df.fillna(0)

df.isnull().sum()

"""## Removendo registros"""

df.query('Valor == 0 | Condominio == 0')

df.query('Valor == 0 | Condominio == 0').index

registros_a_remover = df.query('Valor == 0 | Condominio == 0').index

df.drop(registros_a_remover, axis=0, inplace=True)

df.query('Valor == 0 | Condominio == 0')

df.head()

df.Tipo.unique()

df.drop('Tipo', axis=1, inplace=True)

df.head()

"""## Filtros

### **1. Apartamentos que possuem `1 quarto` e `aluguel menor que 1200`**
"""

df['Quartos'] == 1

selecao1 = df['Quartos'] == 1
df[selecao1].head(5)

selecao2 = df['Valor'] <1200
df[selecao2]

selecao_final = (selecao1) & (selecao2)
df[selecao_final].head()

df_1 = df[selecao_final]

"""### **2. `Apartamentos` que possuem pelo menos `2 quartos`, `aluguel menor que 3000` e `area maior que 70`**"""

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
df[selecao]

df_2 = df[selecao]

"""## Salvando os dados"""

df.to_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index=False)

df.to_csv('dados_apartamentos.csv', index=False)

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index=False, sep=';')

pd.read_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv', sep=';')

"""# Manipulando os dados

## Criando colunas numéricas
"""

url  = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')
dados.head()

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados.head()

dados['Valor_por_ano'] = dados['Valor_por_mes']* 12 + dados['IPTU']
dados.head()

"""## Criando colunas categóricas"""

dados['Descricao'] = dados['Tipo'] + dados['Bairro']
dados.head()

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
dados.head()

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
dados.head()

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
dados.head()

dados.to_csv('dados_completos_dev.csv', index=False, sep=';')

