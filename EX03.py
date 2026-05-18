divida = float(input("Digite o valor da dívida: "))

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

for i in range(len(parcelas)):
    valor_juros = divida * (juros[i] / 100)
    total = divida + valor_juros
    valor_parcela = total / parcelas[i]

    print(f"Total: R$ {total:.2f} | Juros: R$ {valor_juros:.2f} | Parcelas: {parcelas[i]} | Valor da parcela: R$ {valor_parcela:.2f}")