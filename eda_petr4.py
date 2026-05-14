import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

print("\nCarregando dataset...")

df = pd.read_csv('petr4.csv')

print("Dataset carregado com sucesso!")

df.columns = df.columns.str.lower()

print("\nColunas encontradas:")
print(df.columns)

df['date'] = pd.to_datetime(df['date'])

colunas_numericas = ['open', 'high', 'low', 'close', 'volume']

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

df = df.dropna()

print("\nDados tratados com sucesso!")

print("\nPrimeiras linhas:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

print("\nDimensão do dataset:")
print(df.shape)

print("\nValores nulos:")
print(df.isnull().sum())

print("\nEstatísticas descritivas:")
print(df.describe())

df['retorno_diario'] = df['close'].pct_change()

df['media_movel_20'] = df['close'].rolling(window=20).mean()

df['volatilidade_20'] = df['retorno_diario'].rolling(window=20).std()

plt.figure(figsize=(14, 6))

plt.plot(df['date'], df['close'], label='Preço de Fechamento')
plt.plot(df['date'], df['media_movel_20'], label='Média Móvel 20')

plt.title('Preço de Fechamento PETR4')
plt.xlabel('Data')
plt.ylabel('Preço')

plt.legend()
plt.grid()

plt.show()

plt.figure(figsize=(14, 6))

plt.plot(df['date'], df['volume'])

plt.title('Volume de Negociações PETR4')
plt.xlabel('Data')
plt.ylabel('Volume')

plt.grid()

plt.show()

plt.figure(figsize=(14, 6))

plt.plot(df['date'], df['retorno_diario'])

plt.title('Retorno Diário PETR4')
plt.xlabel('Data')
plt.ylabel('Retorno')

plt.grid()

plt.show()

plt.figure(figsize=(14, 6))

plt.plot(df['date'], df['volatilidade_20'])

plt.title('Volatilidade Móvel (20 dias)')
plt.xlabel('Data')
plt.ylabel('Volatilidade')

plt.grid()

plt.show()

plt.figure(figsize=(10, 6))

df['close'].hist(bins=30)

plt.title('Distribuição dos Preços de Fechamento')
plt.xlabel('Preço')
plt.ylabel('Frequência')

plt.grid()

plt.show()

print("\nCorrelação entre preços:")

correlacao = df[['open', 'high', 'low', 'close']].corr()

print(correlacao)

print("\n================ INSIGHTS ================\n")

media = df['close'].mean()
maximo = df['close'].max()
minimo = df['close'].min()

print(f"Preço médio de fechamento: {media:.2f}")
print(f"Maior preço registrado: {maximo:.2f}")
print(f"Menor preço registrado: {minimo:.2f}")

maior_volume = df['volume'].max()

print(f"Maior volume negociado: {maior_volume:.0f}")

volatilidade_media = df['volatilidade_20'].mean()

print(f"Volatilidade média: {volatilidade_media:.4f}")

retorno_medio = df['retorno_diario'].mean()

print(f"Retorno diário médio: {retorno_medio:.6f}")

print("\nAnálise exploratória concluída com sucesso!")
