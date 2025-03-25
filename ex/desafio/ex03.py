#keys = values, trás todos os valores 

def contar_frequencia(palavras):
    lista = palavras.split(' ') #split() transforma a string numa lista
    dicionario = {} # cria um dicionário
    for palavra in lista: 
        if not palavra in dicionario.keys():
            dicionario[palavra] = lista.count(palavra)
    return dicionario

linguagens = 'javascript python html css javascript python javascript'

print(f'dicionario : {contar_frequencia(linguagens)}')