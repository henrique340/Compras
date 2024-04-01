from compras.interface import *

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro')


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def ler_arquivo(nome):
    global dado
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arq')
    else:
        cabeçalho('compras', 42)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastro(arq, item, preço):
    try:
        a = open(arq, 'at')
    except:
        print('não foi possível abrir')
    else:
        try:
            a.write(f'{item}; R${preço:.2f}\n')
        except:
            print('erro ao inserir dado')
        else:
            print(f'{item} adicionado com sucesso')

def cabeçalho(txt, tam):
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)


def menu(lista):
    cabeçalho('Loja YUJI', 42)
    c = 1
    for item in lista:
        print(f'{c} - {item} ')
        c += 1
    print('-' * 42)
    opção = int(input('opção: '))
    return opção


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
