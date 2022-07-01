
dias = int(input("Quantos dias você procrastinou? ")) # Calcula total em segundos

sec_dias = 86400 # quantidade de segundos que tem um dia
sec_hora = 3600 # quantidade de segundos que tem uma hora
sec_min = 60 # quantidade de segundos que tem um min

hour = int(input("Quantas horas? "))
min = int(input("Quantos minutos? "))
segundos = int(input("Quantos segundos? "))

calcday = dias * sec_dias 
calchora = hour * sec_hora
calcsegundos = min * sec_min + segundos
result = calcday + calchora + calcsegundos

print(f"{result} segundos da sua vida que você perdeu")

