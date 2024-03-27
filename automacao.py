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
import pyautogui
from time import sleep
import pandas
from helper import formata_float_str_moeda

# Time pause after each command for pyautogui
pyautogui.PAUSE = 1

# Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = 'thuurdamasceno@gmail.com'
senha = 'xande1301'
tabela = pandas.read_csv('produtos.csv')

# Abrindo o Chrome
pyautogui.press('win')
sleep(1)
pyautogui.write('chrome')
pyautogui.press('enter')

# Digitando o link e acessado o sistema
pyautogui.hotkey('ctrl', 'l')
pyautogui.write(link)
pyautogui.press('enter')

# Pausar para carregar a página de Login
sleep(5)

# Inserir email
pyautogui.click(x=2030, y=825, clicks=1, button='left')
pyautogui.write(email)

# Inserir senha
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')

# Pausa para carregar a página de inserção de Produtos
sleep(5)

for linha in tabela.index:
    # Inserindo o Código do produto
    pyautogui.click(x=1990, y=711)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # Inserindo a Marca do Produto
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    # Inserindo o Tipo do Produto
    pyautogui.write(tipo := tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    # Inserindo a a Categoria do Produto
    pyautogui.write(categoria := str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # Inserindo o Preço Unitário do Produto
    pyautogui.write(preco_unit :=
                    formata_float_str_moeda(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # Inserindo o Custo do Produto
    pyautogui.write(custo := formata_float_str_moeda(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # Inserindo as Observações do Produto
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    else:
        pass
    pyautogui.press('tab')

    # Pressionar 'Enter' para enviar
    pyautogui.press('enter')

    # Voltar ao início da página
    pyautogui.scroll(5000)
