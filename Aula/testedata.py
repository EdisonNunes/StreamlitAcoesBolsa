from datetime import timedelta, date
import yfinance as yf
import pandas as pd


def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    hoje = date.today()
    dtfinal = hoje.strftime('%Y-%m-%d')
    cotacoes_acao = dados_acao.history(period="1d", start="2022-01-01", end=dtfinal)
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao


def carregar_tickers_acoes():
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    base_tickers = base_tickers.sort_values('Código')
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    nomes = list(base_tickers['Ação'])
    return tickers, nomes

acoes, nomes = carregar_tickers_acoes()
#dados = carregar_dados(acoes)
#print(acoes)

empresas = ['IVVB11', 'XRPH11.SA', 'XFIX11.SA']
dados = carregar_dados(empresas)
print(dados)