import pyautogui as pai
from time import sleep
import pandas as pd

#sleep(4)

#print(pai.position())

# Campo de email Página de Login
# x=2012, y=826

# Campo de Código do produto Página de Inserção dos Produtos
# x=2001, y=708

tabela = pd.read_csv('produtos.csv')


def formata_float_str_moeda(valor: float) -> str:
    valor: str = f'R$ {valor:,.2f}'
    valor: str = valor.replace('.', ',')
    return valor


# custo = tabela.loc[tabela.index[1], 'custo']
# print(formata_float_str_moeda(custo := tabela.loc[tabela.index[1], 'custo']))
