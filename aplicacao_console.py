from vertedores import verdedor_retangular,verdedor_triangular

print('Calculo de vazão com vertedores')

tipo = input('Selecione o tipo de  vertedor: "tr" para triangular ou "re" para retangular. ')

if tipo == 'tr':

    print('Verdedor trinagular selecionado')

    H = float(input('Digite o valor de H em metros: '))

    Q = verdedor_triangular(H)

    print("{0} m3/s".format(Q))

elif tipo == 're':

    print('Verdedor retangular selecionado')

    H = float(input('Digite o valor de H em metros: '))

    L = float(input('Digite o valor de L em metros: '))

    Q = verdedor_retangular(H,L)

    print("{0} m3/s".format(Q))

else:

    print('Não foi possível identificar o vertedor')