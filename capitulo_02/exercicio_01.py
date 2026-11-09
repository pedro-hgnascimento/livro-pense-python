# Volume da esfera com raio 5
print((4/3) * 3.14 * (5**3))

# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. 
# O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. 
# Qual é o custo total de atacado para 60 cópias?
preco_capa = 24.95
desconto = 0.40
quantidade = 60
preco_descontado = preco_capa * (1 - desconto)
custo_transporte = 3.00 + (0.75 * (quantidade - 1))
custo_total = (preco_descontado * quantidade) + custo_transporte
print(custo_total)

# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), 
# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, 
# que horas chego em casa para o café da manhã?
hora_saida = (6 * 60 + 52) * 60  # Convertendo para segundos
tempo_primeiro_km = 8 * 60 + 15  # Tempo para o primeiro quilômetro em segundos
tempo_tres_km = 3 * (7 * 60 + 12)  # Tempo para os três quilômetros em segundos
tempo_ultimo_km = 8 * 60 + 15  # Tempo para o último quilômetro em segundos
tempo_total = tempo_primeiro_km + tempo_tres_km + tempo_ultimo_km
hora_chegada = hora_saida + tempo_total
hora_chegada_horas = hora_chegada // 3600 # Divisão inteira para obter as horas
hora_chegada_minutos = (hora_chegada % 3600) // 60 # Resto da divisão para obter os minutos
print(f"Hora de chegada: {hora_chegada_horas}:{hora_chegada_minutos:.02f}")

