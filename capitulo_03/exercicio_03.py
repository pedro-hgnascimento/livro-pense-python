def linha(tamanho=1):
    print('+', end='')
    print(' - - - - +' * tamanho)

def linha_interna(tamanho=1):
    print('|', end='')
    print('         |' * tamanho)

def corpo(tamanho=1):
    linha_interna(tamanho)
    linha_interna(tamanho)
    linha_interna(tamanho)
    linha_interna(tamanho)

def grid22():
    linha(2)
    corpo(2)
    linha(2)
    corpo(2)
    linha(2)

def grid44():
    linha(4)
    corpo(4)
    linha(4)
    corpo(4)
    linha(4)
    corpo(4)
    linha(4)
    corpo(4)
    linha(4)

grid22()
print()
grid44()