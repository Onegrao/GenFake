#Gerador de info
#Objetivo:Gerar informações fake para usar em testes e exporta-lo de diferentes formas
from faker import Faker
import random
import json
#Inicializando a bibilioteca Faker
fake = Faker()
#Gerando Nome e idade aleatorios
nome = fake.name()
cidade = fake.city()
#Definindo um grupo de materias 
materias = ["Matematica","Fisica","Portugues","Ciencias"]

#Sorteando uma materia atraves da lib random
materia = random.choice(materias)

#Dados que serao inseridos
dados = {
    "nome": nome,
    "cidade": cidade,
"cursos":materia,
    "ativo": True
}

# Nome do arquivo onde os dados serão salvos
nome_arquivo = "dados.json"

# Criar e escrever no arquivo JSON
with open(nome_arquivo, "r") as arquivo:
        #Carregando o arquivo Json
        lista = json.load(arquivo)
        #Verificando se é uma lista(Mutavel)
        if not isinstance(lista, list):
                lista = []

#Adicionando os dados gerados no final da lista vinda do arquivo JSON
lista.append(dados)        

#Reformatando a lista para Json
with open(nome_arquivo, "w") as arquivo:
    json.dump(lista, arquivo, indent=4)  # 'indent=4' para formatar o JSON com indentação

print(f"Dados escritos com sucesso no arquivo {nome_arquivo}")


