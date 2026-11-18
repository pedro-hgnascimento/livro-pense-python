import time
segundos = time.time()
print(f"Quantidade original de segundos: {segundos:.1f} segundos")

minutos = segundos / 60
segundos = segundos % 60

horas = minutos / 60
minutos = minutos % 60

dias = horas / 24
horas = horas % 24

anos = dias / 365
dias = dias % 365

print(f"Quantidade de anos: {anos:.1f}")
print(f"Quantidade de dias: {dias:.1f}")
print(f"Quantidade de horas: {horas:.1f}")
print(f"Quantidade de minutos: {minutos:.1f}")
print(f"Quantidade de segundos: {segundos:.1f}")
