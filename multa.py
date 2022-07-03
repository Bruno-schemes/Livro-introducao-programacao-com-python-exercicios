km = int(input("Digite sua velocidade:  "))

multa = 5

if km > 80:
    maior = (km  - 80) * 5 
    print(f"Você ultrapassou o limite de velocidade, sual multa é de: {maior}")

if km <= 80:
    print("você está dentro do limite de velocidade")