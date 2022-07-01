percorrido = float(input("Quantidade de km percorridos: "))
dias = int(input("Dias com o carro: "))

aluguel = 60
km = 0.15

valor1 = percorrido * km
valor2 = aluguel * dias

resultado = valor1 + valor2
print(f"Quantia total é de: {resultado}")