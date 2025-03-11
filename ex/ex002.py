#aprendendo type()
a = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(a))

#aprendendo .is
print("Só tem espaços? ", a.isspace())
print("São números? ", a.isnumeric())
print("São letras? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("São letras maiúsculas? ", a.isupper())
print("São letras minúsculas? ", a.islower())

"""
Tudo que vai dentro do () são parâmetros 
Se vier antes do () são métodos ou função 
"""