# Checkpoint 1

## Carregar módulos
"""

## Commented out IPython magic to ensure Python compatibility.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

"""## Carregar dados"""

path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
path_dead =  'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

dados_paises_covid = pd.read_csv(path)
dados_paises_covid_dead = pd.read_csv(path_dead)

dados_paises_covid

"""## Ajustes

- Nomes das colunas
"""

dados_paises_covid.rename(columns={"Province/State": "province",
                                   "Country/Region": "country"},
                          inplace=True)

dados_paises_covid_dead.rename(columns={"Province/State": "province",
                                        "Country/Region": "country"},
                               inplace=True)

dados_paises_covid_dead.columns

"""- Reajustar dados"""

dados_paises_covid = dados_paises_covid.melt(id_vars=['province', 'country', 'Lat', 'Long'],
                                             var_name = 'date',
                                             value_name = 'infected')

dados_paises_covid_dead = dados_paises_covid_dead.melt(id_vars=['province', 'country', 'Lat', 'Long'],
                                                       var_name = 'date',
                                                       value_name = 'dead')

dados_paises_covid_dead.tail()

dados_paises_covid_dead.dtypes

"""- Ajustar datas"""

dados_paises_covid['date'] = pd.to_datetime(dados_paises_covid['date'],
                                            infer_datetime_format='True')

dados_paises_covid_dead['date'] = pd.to_datetime(dados_paises_covid_dead['date'],
                                                 infer_datetime_format='True')

dados_paises_covid.tail()

dados_paises_covid_dead.tail()

dados_paises_covid_dead.dtypes

"""- Combinar os datasets"""

dados_paises_covid.shape

dados_paises_covid_dead.shape

dados_covid = pd.merge(dados_paises_covid, dados_paises_covid_dead,
                       on = ['province', 'country',	'Lat',	'Long',	'date'],
                       how = 'inner')

dados_covid.head()

dados_covid.shape

"""## Aqui começa o trabalho

## Questão 1
"""

len(dados_covid['country'].unique()) - 4

dados_covid['country'].unique()

dados_covid['country']

"""###Questão 2"""

paises_selecionados = ['Brazil', 'Italy', 'US']

data_max = np.max(dados_covid['date'])
data_max

dados_covid[(dados_covid['country'].isin(paises_selecionados)) & \
            (dados_covid['date'] == data_max)]

"""###Questão 3"""

data_max = np.max(dados_covid['date'])
data_max

dados_filtrados = dados_covid[dados_covid['date'] == data_max].reset_index(drop=True)

paises_agrupados = dados_filtrados.groupby('country') \
                .agg(infected = pd.NamedAgg('infected', 'sum'),
                     dead = pd.NamedAgg('dead', 'sum')) \
                     .reset_index()

paises_agrupados.sort_values('infected', ascending = False).head(10)

paises_agrupados.sort_values('dead', ascending = False).head(10)

"""###Questão 4"""

data_max = np.max(dados_covid['date'])

paises_agrupados = dados_filtrados.groupby('country') \
                .agg(infected = pd.NamedAgg('infected', 'sum'),
                     dead = pd.NamedAgg('dead', 'sum')) \
                     .reset_index()

paises_agrupados['mort_rate'] = paises_agrupados['dead'] / paises_agrupados['infected']

paises_agrupados.sort_values('mort_rate', ascending = False).head(11)

"""###Questão 5"""

dados_covid_resumo = dados_covid.groupby(['date', 'country']) \
                                .agg(infected = pd.NamedAgg('infected', 'sum'),
                                      dead = pd.NamedAgg('dead', 'sum')) \
                                .reset_index()

paises_selecionados = ['Brazil', 'US']

dados_filtrados = dados_covid_resumo[dados_covid_resumo['country'].isin(paises_selecionados)]

dados_filtrados.head()

dados_filtrados.pivot(index = 'date',
                      columns = 'country',
                      values = 'infected' )

dados_covid[(dados_covid['country'].isin(paises_selecionados)) & \
            (dados_covid['date'] == data_max)]

























