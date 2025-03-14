'''Dicionários'''
#mutavel, desordenados (sair fora da ordem), chave: valor
#a chave é unica: os valores podem ser de qualquer tipo

dados_pessoais = {'nome_completo': 'Lucas Gomes', 
                  'cpf' : '000.000.000-00', 
                  'email' : 'fulano@gmail.com', 
                  'idade' : 18
                  }

dados_pessoais2 = {'nome_completo': 'Luca', 
                  'cpf' : '000.111.000-00', 
                  'email' : 'fulanogil@gmail.com', 
                  'idade' : 19}

print(dados_pessoais)

#(dados_pessoais.keys()) retorna as chaves presentes no dicionario (nome_completo, email, cpf, idade)

#(dados_pessoais.values()) retorna os valores (Lucas Gomes, 000.000.000-00, fulano@gmail.com, 18)

#(dados_pessoais['nome_completo']) - retorna um valor relacionado a chave porém se a chave n existir da erro
#(dados_pessoais.get['nome_completo']) retorna um none caso a chave não exista, porém o cod não para de rodar 

#(dados_pessoais['nome_completo']) = 'Diego' - substituir o valor do nome completo para Diego ou caso não tenha o cod ira criar um valor do 0.

#del dados_pessoais('nome_completo'), para excluir uma chave // (dados_pessoais.pop('nome_completo')) - retorna o valor associado a chave

#dados_pessoais.update(dados_pessoais2) - atualiza o dicionario, compara os dicionarios e caso tenha chaves iguais ele substitui e caso tenha diferente ele concatena

