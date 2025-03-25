"""
Primeiro Exercício: Soma de elementos pares

Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
elementos pares contidos nela.

Exemplo: [2,4,10,3,9,7,15,22]

Saída: A soma dos pares é: x
"""

def somar_pares(lista_de_numeros):
    resultado = 0
    for numero in lista_de_numeros:  
        if numero % 2 == 0: 
            resultado += numero 
    return resultado

lista = [1,2,3,4,5,6,7,8,9,10] 

print(f'A soma dos números pares é = {somar_pares(lista)}')