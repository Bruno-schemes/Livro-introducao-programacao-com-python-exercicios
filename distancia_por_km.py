desejado = int(input("Digite a distancia que pretende percorrer: "))

pequenas = 0.50
longas = 0.45

if desejado <= 200:
    valor = desejado * pequenas
    print(f"{valor} a pagar")


    
if desejado > 200:
    valor = desejado * longas
    print(f"{valor:6.2f} a pagar")

