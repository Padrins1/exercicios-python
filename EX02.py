preco = float(input("Digite o preço do carro: "))

# À vista com desconto
avista = preco * 0.8
print(f"O preço final à vista com desconto 20% é: R$ {avista:.2f}")

parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
acrescimos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

for i in range(len(parcelas)):
    total = preco * (1 + acrescimos[i]/100)
    valor_parcela = total / parcelas[i]

    print(f"O preço final parcelado em {parcelas[i]}x é de R$ {total:.2f} com parcelas de R$ {valor_parcela:.2f}")