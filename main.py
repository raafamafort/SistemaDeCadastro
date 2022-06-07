# IMPORT
from SistemaDeCadastro.lib.sistema import *
from SistemaDeCadastro.lib.arquivotxt import *
from time import sleep

# LISTAS DE PESSOAS CADASTRADAS
arq = 'PessoasCadastradas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

# PROGRAMA
cabecalho(gre(neg("SISTEMA DE CADASTRO")))
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho(gre(neg('NOVO CADASTRO')))
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho(gre(neg('Saindo do sistema... Até logo!')))
        break
    else:
        print(red("ERROR! Digite uma opção válida!"))
    sleep(1)
