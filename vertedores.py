''''
Funções de calculo de vazão de verdedores
'''


def verdedor_triangular(H):

    return 1.4*(H**(5/2))

def verdedor_retangular(H,L):

    return 1.84*L*(H**(3/2))