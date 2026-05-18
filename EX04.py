print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

tipo = int(input("Digite o tipo (1, 2 ou 3): "))

if tipo not in [1, 2, 3]:
    print("Tipo inválido!")
else:
    valor = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias: "))

    if tipo == 2 or tipo == 3:
        print("Isento de imposto de renda.")
    else:
        # CDB paga IR
        if dias <= 180:
            aliquota = 22.5
        elif dias <= 360:
            aliquota = 20
        elif dias <= 720:
            aliquota = 17.5
        else:
            aliquota = 15

        imposto = valor * (aliquota / 100)

        print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")