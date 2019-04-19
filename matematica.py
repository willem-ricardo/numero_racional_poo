""" FUNÇÃO PROGRESSÃO ARITMÉTICA """
def p_artimetica(num_termos, termo_inicial, razao):
    for i in range(num_termos):
        print(termo_inicial)
        termo_inicial += razao

""" FUNÇÃO PROGRESSÃO GEOMÉTRICA """
def p_artimetica(num_termos, termo_inicial, razao):
    for i in range(num_termos):
        print(termo_inicial)
        termo_inicial *= razao

""" FUNÇÃO EXPONENCIAL """
def exponencial(base, expoente):
    resultado = 1;
    for i in range(expoente):
        resultado *= base
    return resultado

""" FUNÇÃO FATORIAL """
def fatorial(valor):
    fatorial = 1
    for i in range(1, valor+1):
        fatorial *= i
        print(fatorial)

""" FUNÇÃO FIBONACCI """
def fibonacci(valor):
    primeiro=0
    segundo=1
    for i in range(valor):
        if i == 0 or i == 1:
            print(i)
        else:
            aux = primeiro + segundo
            primeiro = segundo
            segundo = aux
            print(segundo)
