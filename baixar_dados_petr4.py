import yfinance as yf

TICKER = 'PETR4.SA'
DATA_INICIAL = '2000-01-01'
DATA_FINAL = '2025-02-09'

print("Baixando dados da PETR4...")

df = yf.download(
    TICKER,
    start=DATA_INICIAL,
    end=DATA_FINAL
)

df.reset_index(inplace=True)

df.to_csv('petr4.csv', index=False)

print("CSV gerado com sucesso!")
print(f"Total de registros: {len(df)}")
