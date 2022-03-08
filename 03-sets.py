"""Exercício 1:

Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
obs: indicados nas variaveis "ingles" e "frances"

Faça um programa que responda as seguintes perguntas:

1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?


    
ingles = ["João Alves dos Santos", "Maria Magalhães", "Antônio da Silva Ferreira", 
"José Júnior Jarbas", "Henrique da Silva Sauro","Joaquina Ferreira da Silva", "Fabiana Aparecida Bianco",
"Marrone Gutierres","Carlos Magno Farad","Antônio da Silva Júnior Amaral"]

frances = ["João Alves dos Santos","Antônio da Silva Ferreira","Fernanda Abdala Mohamed",
"Abner Mignon Alib","Alisson Figueiredo","Henrique da Silva Sauro",
"Maria Magalhães","Marrone Gutierres","Joaquina Ferreira da Silva"]


conj_ing = set(ingles)
conj_fr = set(frances)

#1.	Quantos alunos estão matriculados na escola, no total?

total = conj_ing | conj_fr #união
total = len(total)

print(f"O total de alunos é: {total}")


#2.	Quantos e quais estão matriculados APENAS em INGLES?

conj_ing_apenas = conj_ing - conj_fr 
total_ing = len(conj_ing_apenas)
print(f"O total de alunos APENAS de inglês é: {total_ing} e são eles: \n{conj_ing_apenas}")


#3.	Quantos e quais estão matriculados APENAS em FRANCES?

conj_fr_apenas = conj_fr - conj_ing
total_fr = len(conj_fr_apenas)
print(f"O total de alunos APENAS de francês é: {total_fr} e são eles: \n{conj_fr_apenas}")


#4.	Quantos e quais estão matriculados EM AMBOS os cursos?

conj_AMBOS = conj_ing & conj_fr
total_AMBOS = len(conj_AMBOS)

print(f"O total de alunos EM AMBOS os cursos é: {total_AMBOS} e são eles: \n{conj_AMBOS}")

__________________________________________________________________________________


Exercício 2:

Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.

d = {"DF": "Distrito Federal",
"ES": "Espírito Santo",  
"MG": "Minas Gerais", 
"RJ": "Rio de Janeiro",    
"SC": "Santa Catarina", 
"SP": "São Paulo",
"AC": "Acre",
"AM": "Amazonas",    
"AL": "Alagoas",    
"BA": "Bahia",
"CE": "Ceará",   
"GO": "Goiás",    
"MA": "Maranhão",    
"PA": "Pará",
"PE": "Pernambuco",    
"PI": "Piauí",
"RO": "Rondônia",    
"SE": "Sergipe",  
"TO": "Tocantins",    
"MS": "Mato Grosso do Sul",    
"RN": "Rio Grande do Norte",    
"RS": "Rio Grande do Sul", 
"AP": "Amapá",
"MT": "Mato Grosso",    
"PB": "Paraíba",
"PR": "Paraná",  
"RR": "Roraima"}

while True:
    estado = input("Informe a sigla do estado (0 - sair): ")
    if (estado == "0"):
        break
    elif (estado not in d):
        print("Sigla inexistente!")
    else:
        print(f"O nome completo do estado {estado} é: {d[estado]})
__________________________________________________________________________________

Exercício 3:

Faça um programa que ordene um dicionário por seus valores. 
Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}


from audioop import reverse

d = {"matemática": 87, "física": 81, "química": 83} 

d1= dict(sorted(d.items(), key=lambda item: item[1],reverse=True))

print(d1)
__________________________________________________________________________________


Exercício 4:

Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}

dict = {1: "vermelho", 2: "azul", 3: "marrom"}

for item in dict:
   print(f"{item}: {len(dict[item])}")

__________________________________________________________________________________

Exercício 5:

Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. 
Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20

dict = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

maior = 0

chave_maior = ""
chave_menor = ""

for i in sorted(dict, key = dict.get):
    if dict[i] > maior:
        maior = dict[i]
        chave_maior = i

menor = maior

for i in sorted(dict, key = dict.get):
    if dict[i] < menor:
        menor = dict[i]
        chave_menor = i


print(chave_maior, maior)
print(chave_menor, menor)
"""



