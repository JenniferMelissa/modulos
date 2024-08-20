#modulo é um arquivo que voce criar e importa no programa principal

#import 1 forma, traz tudo
#import cinematica as cn

#import 2 forma, escolhe algumas(boa pra quando usa poucas, roda mais rapido, ocupa menas memororria e o arquivo fica menor)
#from cinematica import mostrar_menu, calcular_ep

#import 3 forma, traz todas as funcoes
from cinematica import *

#mostra menu na tela, assim, precisa chamar o metodo e depois a funcao
while True:
    mostrar_menu()

    opcao = input('Opção do usuário: ')

    match opcao:
        case '1':
            m = float(input('Informe a massa em kg: ').replace('.',','))
            h = float(input('Informe a altura: ').replace('.',','))
            print(f'Energia potencial: {calcular_ep(m,h):,.2f} J.')
            continue
        case '2':
            m = float(input('Informe a massa em kg: ').replace('.',','))
            v = float(input('Informe a velocidade em m/s: ').replace(',','.'))
            print(f'Energia cinética: {calcular_ec(m,v):,.2f} J.')
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida!')
            continue