"""
Oitavo Exercício: Verificador de Palíndromos

Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
pode ser lida da mesma forma de trás para frente) e False caso contrário.

Exemplo:

entrada = "radar"
Saída: True
"""

palavra = input('Digite uma palavra: ')

if palavra == palavra[::-1]: # :inicio :fim : escolhi para a palavra ir do normal ao indice -1 ou seja vai inverter a palavra
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')
