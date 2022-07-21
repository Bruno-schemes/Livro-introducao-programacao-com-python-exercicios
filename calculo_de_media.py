notas = [6,7,5,8,9] #lista de notas
soma = 0 # variavel que vai guardar a soma
x = 0 # acumulador

while x < 5: #enquanto x < do que 5, repetir a soma
    soma += notas[x] # vai somar a variavel notas de numero em numero até x chegar a 5.
    x += 1 # vai acumular até 5
print(f"Média: {soma/ x:5.2f}") # por fim irá printar a soma e dividir por 5    