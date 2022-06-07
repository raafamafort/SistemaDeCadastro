from SistemaDeCadastro.lib.cores import *


def linha():
    print("-" * 40)


def cabecalho(msg):
    linha()
    print(msg.center(55))
    linha()


def leiaInt(msg):
    while True:
        try:
            opc = int(input(msg))
        except(ValueError, TypeError):
            print(red("ERROR! Digite um número valido!"))
            continue
        else:
            return opc


def menu(lista):
    cabecalho(neg(gre("MENU PRINCIPAL")))
    c = 1
    for item in lista:
        print(f'{yel(c)} - {blue(item)}')
        c += 1
    linha()
    opc = leiaInt(cia('Sua Opção: '))
    return opc
