from compras.interface import *
from compras.arquivo import *

arq = 'cliente.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)


while True:
    resposta = menu(['ver produtos', 'cadastrar produto', 'fechar sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabeçalho('novo cadastro', 42)
        produto = str(input('digite o produto: '))
        preço = float(input('digite o preço do produto: '))
        cadastro(arq, produto, preço)
    elif resposta == 3:
        cabeçalho('fim do programa', 42)
        break
