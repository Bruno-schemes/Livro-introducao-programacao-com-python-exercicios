salario = float(input("Digite o salário: "))
base = salario 
imposto = 0

if base > 2000:

        imposto = imposto + ((base - 3000) * 0.35)
        base = 4500
        print(imposto)
if base > 1000:
    imposto = imposto + ((base - 1000)* 0.20)
    print(f"Salario: R${salario:6.2f} Imposto a pagar: R${imposto:5.2f}")



    # 500 - 0
    # 1000 - 0
    # 1500 - 100
    # 2000 - 200
    # 2500 - 300
    # 3000 - 400
    # 3500 - 500
    # 4000 - 600 e assim por diante...
