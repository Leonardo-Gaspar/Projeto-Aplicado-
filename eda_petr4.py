import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('petr4.csv', header=1)

df.columns = ['date', 'close', 'high', 'low', 'open', 'volume']

print("\n Dataset carregado com sucesso!")

df['date'] = pd.to_datetime(df['date'])

df.columns = df.columns.str.lower()

df = df.dropna()

print("\n Dados tratados!")

print("\n Primeiras linhas:")
print(df.head())

print("\n Informações gerais:")
print(df.info())

print("\n Dimensão do dataset:")
print(df.shape)

print("\n Verificando valores nulos:")
print(df.isnull().sum())

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
elif 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

df.columns = df.columns.str.lower()

df = df.dropna()

print("\n Dados tratados!")

print("\n Estatísticas descritivas:")
print(df.describe())

if 'date' in df.columns and 'close' in df.columns:
    plt.figure()
    df.sort_values('date').plot(x='date', y='close')
    plt.title('Preço de Fechamento PETR4 ao longo do tempo')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.grid()
    plt.show()

if 'date' in df.columns and 'volume' in df.columns:
    plt.figure()
    df.sort_values('date').plot(x='date', y='volume')
    plt.title('Volume de Negociação ao longo do tempo')
    plt.xlabel('Data')
    plt.ylabel('Volume')
    plt.grid()
    plt.show()

colunas = ['open', 'high', 'low', 'close']

colunas_existentes = [col for col in colunas if col in df.columns]

if len(colunas_existentes) > 1:
    print("\n Correlação entre preços:")
    print(df[colunas_existentes].corr())

print("\n INSIGHTS:")

if 'close' in df.columns:
    media = df['close'].mean()
    maximo = df['close'].max()
    minimo = df['close'].min()

    print(f"- Preço médio de fechamento: {media:.2f}")
    print(f"- Preço máximo observado: {maximo:.2f}")
    print(f"- Preço mínimo observado: {minimo:.2f}")

print("\n Análise exploratória concluída!")