dias = ["segunda-feira", "terca-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
votos = [0, 0, 0, 0, 0]

n = int(input("Informe o número de colaboradores: "))

for i in range(n):
    voto = input("Informe o dia da sua preferência: ").lower()

    if voto in dias:
        index = dias.index(voto)
        votos[index] += 1
    else:
        print("Dia inválido!")

maior = max(votos)

# Verifica empate
empates = []
for i in range(len(votos)):
    if votos[i] == maior:
        empates.append(dias[i])

if len(empates) > 1:
    print("Houve empate entre:", ", ".join(empates))
else:
    print("O dia escolhido pelos colaboradores é:", empates[0])