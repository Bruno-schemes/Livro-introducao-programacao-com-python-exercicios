cigarros = int(input("Cigarros fumados por dia: "))
anos = float(input("Quantos anos você fuma: "))

min = 10

calculo = anos * 365 * cigarros * 10

red = calculo / (24 * 60)

print(f"{red:3.2f}")