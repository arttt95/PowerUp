import pandas as pd


tabela = pd.read_csv('produtos.csv')


def formata_float_str_moeda(valor: float) -> str:
    valor: str = f'R$ {valor:,.2f}'
    valor: str = valor.replace('.', ',')
    return valor


# custo = tabela.loc[tabela.index[1], 'custo']
# print(formata_float_str_moeda(custo := tabela.loc[tabela.index[1], 'custo']))
