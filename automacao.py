"""
# Passo a Passo do projeto

1 - Entrar no sistema da empresa:
    -> https://dlp.hashtagtreinamentos.com/python/intensivao/login

2 - Fazer login no sistema:
    -> Inserir email e senha;

3 - Importar a base de dados:
    -> Arquivo CSV entregue pelo cliente;

4 - Cadastrar um produto:
    -> Inserir o código do Produto (Caixa de Escolha 1);
    -> Inserir Marca do Produto (Caixa de Escolha 2);
    -> Inserir Tipo do produto (Caixa de Escolha 3);
    -> Inserir Categoria do Produto (Caixa de Escolha 4);
    -> Inserir Preço Unitário do Produto (Caixa de Escolha 5);
    -> Inserir Custo do Produto (Caixa de Escolha 6);
    -> Inserir as Observações Referentes ao Produto (Caixa de Escolha 7)

5 - Repetir o processo de cadastro de produto até acabar a lista de produtos
no arquivo CSV passado pelo cliente:

#############################################################
##               *** COMANDOS PYAUTOGUI ***                ##
#############################################################
##  * pyautogui.click -> clicar em algum lugar da tela *   ##
##  * pyautogui.write -> escrever um texto *               ##
##  * pyautogui.press -> Pressionar umatecla no teclado *  ##
#############################################################

"""
import pyautogui as gui
from time import sleep
import pandas as pd
from helper import formata_float_str_moeda

# Time pause after each command for pyautogui
gui.PAUSE = 1

# Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = 'thuurdamasceno@gmail.com'
senha = 'xande1301'
tabela = pd.read_csv('produtos.csv')

# Abrindo o Chrome
gui.press('win')
sleep(1)
gui.write('chrome')
gui.press('enter')

# Digitando o link e acessado o sistema
gui.hotkey('ctrl', 'l')
gui.write(link)
gui.press('enter')

# Pausar para carregar a página de Login
sleep(2)

# Inserir email
gui.click(x=2030, y=825, clicks=1, button='left')
gui.write(email)

# Inserir senha
gui.press('tab')
gui.write(senha)
gui.press('enter')

# Pausa para carregar a página de inserção de Produtos
sleep(2)

for linha in tabela.index:
    # Inserindo o Código do produto
    gui.click(x=1990, y=711, clicks=1, button='left')
    codigo = tabela.loc[linha, 'codigo']
    gui.write(codigo)
    gui.press('tab')

    # Inserindo a Marca do Produto
    marca = tabela.loc[linha, 'marca']
    gui.write(marca)
    gui.press('tab')

    # Inserindo o Tipo do Produto
    gui.write(tipo := tabela.loc[linha, 'tipo'])
    gui.press('tab')

    # Inserindo a a Categoria do Produto
    gui.write(categoria := str(tabela.loc[linha, 'categoria']))
    gui.press('tab')

    # Inserindo o Preço Unitário do Produto
    gui.write(preco_unit :=
                    formata_float_str_moeda(tabela.loc[linha, 'preco_unitario']))
    gui.press('tab')

    # Inserindo o Custo do Produto
    gui.write(custo := formata_float_str_moeda(tabela.loc[linha, 'custo']))
    gui.press('tab')

    # Inserindo as Observações do Produto
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        gui.write(obs)
    else:
        pass
    gui.press('tab')

    # Pressionar 'Enter' para enviar
    gui.press('enter')

    # Voltar ao início da página
    gui.scroll(5000)
