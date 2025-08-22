# Análise de Dados COVID-19

Este repositório contém um script Python para análise de dados relacionados à COVID-19, utilizando dados de casos confirmados e mortes em todo o mundo. O objetivo é explorar e visualizar as tendências da pandemia em diferentes países.

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dados

Os dados utilizados neste projeto são provenientes do repositório [CSSEGISandData](https://github.com/CSSEGISandData/COVID-19), que fornece informações atualizadas sobre casos confirmados e mortes por COVID-19 em todo o mundo.

## Instalação

Para executar este projeto, você precisará ter o Python instalado em sua máquina. Além disso, é recomendável criar um ambiente virtual e instalar as dependências necessárias. Siga os passos abaixo:

1. Clone o repositório:
```bash
git clone https://github.com/seu_usuario/Analise_Covid.git
cd Analise_Covid
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

Instale as dependências:

```bash
pip install pandas numpy matplotlib seaborn
```

Para executar a análise, basta rodar o script Paises_Covid.py:

```bash
python Paises_Covid.py
```

O script irá carregar os dados, realizar as análises e gerar visualizações dos casos confirmados e taxas de mortalidade para os países selecionados.

Análises Realizadas
O script realiza as seguintes análises:

Número de países únicos com dados disponíveis.
Casos confirmados e mortes para países selecionados (Brasil, Itália, EUA) na data mais recente.
Agrupamento de dados por país para calcular totais de infectados e mortos.
Cálculo da taxa de mortalidade por país.
Visualizações gráficas das tendências de casos e taxas de mortalidade.

Contribuições
Contribuições são bem-vindas! Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas.

Contato
Para mais informações, entre em contato com cordeiro.almeida@hotmail.com
