#modulo é um arquivo que voce criar e importa no programa principal
#é como uma biblioteca


#menu
def mostrar_menu():
    print(' 1 - Calcular energia potencial.')
    print(' 2 - Calcular energia cinética.')
    print(' 3 - Sair do programa.')

#def seguido do nome da funcao
#entre parenteses tem as parametros que serao utilizadas, poder ser vazio ou nao
def calcular_ep(m, h):
    ep = m*9.8*h
    return ep

def calcular_ec(m, v):
    ec = (m*(v**2))/2
    return ec

