from SistemaDeCadastro.lib.sistema import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('', end='')


def lerArquivo(nome):
    a = open(nome, 'rt')
    cabecalho(neg(gre("PESSOAS CADASTRADAS")))
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{neg(dado[0]):<40}{neg(dado[1]):>3} anos')
    a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    a = open(arq, 'at')
    a.write(f'{nome};{idade}\n')
    print(f'Novo registro de {yel(neg(nome))} adicionado.')
    a.close()
