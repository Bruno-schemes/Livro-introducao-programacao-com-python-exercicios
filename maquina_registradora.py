
v = 0
while True:
    produto = int(input("Digite o código do produto: "))
    if produto == 0:
        print(f"Você terminou as compras \nTotal: R$ {v:2.2f}")
        break   
    elif produto == 1:
        codigo = 0.50
        v += codigo
        print(f"{v:2.2f}")
    elif produto == 2:
        codigo = 1.00
        v += codigo
        print(f"{v:2.2f}")
    elif produto == 3:
        codigo = 4.00
        v += codigo
        print(f"{v:2.2f}")
    elif produto == 5:
        codigo = 7.00
        v += codigo
        print(f"{v:2.2f}")
    elif produto == 9:
        codigo = 8.00
        v += codigo
        print(f"{v:2.2f}")
    else:
        print("Código inválido")     
 