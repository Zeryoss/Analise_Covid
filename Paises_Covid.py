# Checkpoint 1

## Carregar módulos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Carregar dados
try:
    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    path_dead =  'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

    dados_paises_covid = pd.read_csv(path)
    dados_paises_covid_dead = pd.read_csv(path_dead)
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")

## Ajustes
# Nomes das colunas
dados_paises_covid.rename(columns={"Province/State": "province",
                                   "Country/Region": "country"},
                          inplace=True)

dados_paises_covid_dead.rename(columns={"Province/State": "province",
                                        "Country/Region": "country"},
                               inplace=True)

# Reajustar dados
dados_paises_covid = dados_paises_covid.melt(id_vars=['province', 'country', 'Lat', 'Long'],
                                             var_name='date',
                                             value_name='infected')

dados_paises_covid_dead = dados_paises_covid_dead.melt(id_vars=['province', 'country', 'Lat', 'Long'],
                                                       var_name='date',
                                                       value_name='dead')

# Ajustar datas
dados_paises_covid['date'] = pd.to_datetime(dados_paises_covid['date'], infer_datetime_format='True')
dados_paises_covid_dead['date'] = pd.to_datetime(dados_paises_covid_dead['date'], infer_datetime_format='True')

# Combinar os datasets
dados_covid = pd.merge(dados_paises_covid, dados_paises_covid_dead,
                       on=['province', 'country', 'Lat', 'Long', 'date'],
                       how='inner')

## Aqui começa o trabalho

# Questão 1
num_paises = len(dados_covid['country'].unique()) - 4
print(f"Número de países únicos (excluindo províncias): {num_paises}")

# Questão 2
paises_selecionados = ['Brazil', 'Italy', 'US']
data_max = np.max(dados_covid['date'])
print(f"Data mais recente: {data_max}")

dados_ultimos = dados_covid[(dados_covid['country'].isin(paises_selecionados)) & (dados_covid['date'] == data_max)]
print(dados_ultimos)

# Questão 3
dados_filtrados = dados_covid[dados_covid['date'] == data_max].reset_index(drop=True)
paises_agrupados = dados_filtrados.groupby('country') \
                .agg(infected=pd.NamedAgg('infected', 'sum'),
                     dead=pd.NamedAgg('dead', 'sum')) \
                     .reset_index()

print("Top 10 países por infectados:")
print(paises_agrupados.sort_values('infected', ascending=False).head(10))

print("Top 10 países por mortes:")
print(paises_agrupados.sort_values('dead', ascending=False).head(10))

# Questão 4
paises_agrupados['mort_rate'] = paises_agrupados['dead'] / paises_agrupados['infected']
print("Top 11 países por taxa de mortalidade:")
print(paises_agrupados.sort_values('mort_rate', ascending=False).head(11))

# Questão 5
dados_covid_resumo = dados_covid.groupby(['date', 'country']) \
                                .agg(infected=pd.NamedAgg('infected', 'sum'),
                                      dead=pd.NamedAgg('dead', 'sum')) \
                                .reset_index()

dados_filtrados = dados_covid_resumo[dados_covid_resumo['country'].isin(paises_selecionados)]
print(dados_filtrados.head())

# Visualização dos dados
plt.figure(figsize=(12, 6))
sns.lineplot(data=dados_filtrados, x='date', y='infected', hue='country', marker='o')
plt.title('Casos Confirmados de COVID-19 ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Casos Confirmados')
plt.legend(title='País')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualização da taxa de mortalidade
plt.figure(figsize=(12, 6))
sns.barplot(data=paises_agrupados.sort_values('mort_rate', ascending=False).head(10), x='country', y='mort_rate')
plt.title('Taxa de Mortalidade por País (Top 10)')
plt.xlabel('País')
plt.ylabel('Taxa de Mortalidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
