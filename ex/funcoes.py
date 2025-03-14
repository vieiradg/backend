#função sem parametros e sem retorno
def somar_dois_numeros():
    n1 = 10
    n2 = 12.5
    print(n1 + n2)

somar_dois_numeros()

print('*'*50)

#função com parametros e sem retorno
def somar_dois_numeros(n1: int, n2: int):
    print(n1 + n2)
    n1 = input('digite um n: ')
    n2 = input('digite outro n: ')

somar_dois_numeros(n1, n2)

print('*'*50)

#função com parametro e retornos (funções com retorno precisa de uma variavel pra armazenar)
def multiplicar_dois_numeros(n1, n2):
    return n1*n2
resultado = multiplicar_dois_numeros(10, 2)
print(resultado)

print('*'*50)

#funçao sem parametro e com retorno
def retornar():
    n1 = 10
    n2 = 20
    return n1, n2  #separar por , ou () vira tupla e com [] vira lista

retorno_da_funcao = retornar()
print(retorno_da_funcao)

print('*'*50)

#sintaxe para uma função com mts valores como parametros usando o args
def somar(*numeros):
    print(type(numeros))
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

resultado_da_soma = somar(1,2,3,4,5,6,7,8, 90)
print(resultado_da_soma)

