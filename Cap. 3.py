"""
______________________________________________________________________________________________
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.


salario = float(input("Informe o valor do salário: "))
porcentagem = float(input("Informe o valor do aumento em porcentagem (%): "))

aumento = salario * porcentagem/100

novo_salario = salario + aumento

print(f"O valor do aumento é de {aumento} reais")
print(f"O novo salario é de {novo_salario} reais")
______________________________________________________________________________________________
"""



"""
______________________________________________________________________________________________
Escreva um programa que calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
#Pergunta a distância

dist_km = float(input("Informe a distância a percorrer (km): "))
velocidade = float(input("Informe a velocidade a percorrer (km/h): "))

tempo_h = dist_km / velocidade

print (f"A duração dessa viagem é de {tempo_h:.0f} horas")

tempo_h_seg = tempo_h * (60 * 60)

#Calculando o tempo calculado em dias

tempo_dias = tempo_h_seg /(3600 * 24)


#Calculando o tempo em horas da parte decimal do cálculo de dias
tempo_seg_restante =  tempo_h_seg % 86400

tempo_horas = tempo_seg_restante / 3600

#Calculando o tempo em minutos da parte decimal do cálculo de horas
tempo_seg_restante1 = tempo_seg_restante % 3600

tempo_min = tempo_seg_restante1 / 60

#Calculando o tempo em segundos da parte decimal do cálculo de minutos
tempo_seg_final = tempo_seg_restante1 % 60

print (f"A duração dessa viagem é de {tempo_dias:.0f} dias, {tempo_horas:.0f} horas, {tempo_min:.0f} minutos e {tempo_seg_final:.0f} segundos")
______________________________________________________________________________________________
"""


"""
Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:
     9 x C
 F = ----- + 32
       5
temp_C = float(input("Informe a temperatura em ºC: "))
temp_F = (9 * temp_C)/5 + 32

print(f"A temperatura correspondente em ºF é: {temp_F:.2f}")
"""

"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.


km_percorrido = float(input("Informe a qtd de km percorrido: "))
dias_alugado = float(input("Informe a qtd de dias alugado: "))

dias_pagar = dias_alugado * 60
km_pagar = km_percorrido * 0.15

total_pagar = dias_pagar + km_pagar

print(f"Total a pagar: {total_pagar:.2f}")

"""
"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, 
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

cigarros_dia = float(input("Quantos cigarros você fuma por dia?"))
anos_fumando = float(input("Há quantos anos você fuma?"))

tempo_perd_dia = ((10 * cigarros_dia) / (24 * 60)) * 365 * anos_fumando

print(f"O fumante perderá {tempo_perd_dia:.0f} dias")



