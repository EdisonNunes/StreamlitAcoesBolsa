import pandas as pd
import yfinance as yf

st.write(st.__version__)

def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2022-01-01", end="2025-01-02")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

def carregar_tickers_acoes():
    base_tickers = pd.read_csv('IBOV2.csv', sep=';', encoding='utf-8')
    
    tickers = list(base_tickers['Código'])
    tickers = [item + '.SA' for item in tickers]  # Coloca .SA no final de cada ticker
    nomes = list(base_tickers['Ação'])
        
    return tickers, nomes

acoes, nomes = carregar_tickers_acoes()
print(nomes[0])
nomes_empresas={}
for i, empresa in enumerate(acoes):
    nomes_empresas[empresa] = nomes[i]
    

print(nomes_empresas)