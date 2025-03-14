import csv #manipular os arquivos csv
import time #tempo
import os # fincionalidades dp terminal

print ("-"*70)
nome_completo = input("Digite seu nome completo: ")
print("-"*70)
data_de_nascimento = input("Digote sua data de nascimento (DD/MM/AAAA): ")
print("-"*70)
cpf = input("Diegite seu CPF (exemplo 000.000.000-00): ")

with open("ficha_cadastro.csv", "a") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome_completo, data_de_nascimento, cpf])
print()

print("****************************************")
print("* Cadastro realizado com sucesso! *")
print("****************************************")

os.system("clear")

for i in range(0,10)
    print(f"Gerando arquivo em: {i+1}" + Fore.GREEN)
    time.sleep(1)
    os.system("clear")

with open("ficja_cadastro.csv", "r") as arquivo:
    dados = csv.reader(arquivo)
    for linha in dados:
        print(linha)
        print("-"*70)

#a - // r - // w -