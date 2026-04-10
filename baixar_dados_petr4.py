import yfinance as yf

df = yf.download('PETR4.SA', start='2000-01-01', end='2025-02-09')

df.reset_index(inplace=True)

df.to_csv('petr4.csv', index=False)

print("CSV gerado com sucesso!")