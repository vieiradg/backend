"""
Segundo Exercício: Ordenação de Tuplas

Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.

Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)

Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”)
"""

#sort() - modifica a lista original pora uma lista ordenada
#sorted() - retorna a minha lista + uma nova lista ordenada.
#lambda - é como se fosse uma variavel anonima no js
#iteravel - Todo tipo de dado que contém mais de um item dentro dele (lista, dicionários e tuplas)

def ordenar_tuplas(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key= lambda tupla: tupla[1])
    return lista_ordenada

lista_de_tuplas = [('Samuel', 23), ('Karynne', 35), ('Diego', 28)]

print(f'A lista de tuplas ordenada por idade: {ordenar_tuplas(lista_de_tuplas)}')